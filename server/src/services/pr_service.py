import asyncio
import heapq
import json
import urllib.parse
from typing import List, Dict, Set

from src.adapters import GenAIAPI, GenAIAPIError, GitHubAPI, GitHubAPIError
from src.constants import get_gen_ai_prompt, get_github_repo_content_for_branch
from src.mock import MOCK_DATA
from src.parsers.python_parser import PythonDiffParser

class PRError(Exception):
    def __init__(self, message: str, status_code: int):
        self.message = message
        self.status_code = status_code

class PRService():
    def __init__(self, github_api: GitHubAPI, gen_ai_api: GenAIAPI, python_parser: PythonDiffParser):
        self.github_api = github_api
        self.gen_ai_api = gen_ai_api
        self.python_parser = python_parser

    async def get_pr_file_change_nodes(self, owner: str, repo: str, pr_number: int, page: int = 1) -> List[str]:
        if owner == "mock" and repo == "mock" and pr_number == 1:
            await asyncio.sleep(3)
            return MOCK_DATA.get("nodes")
        try:
            files = await self.github_api.fetch_pr_files_diff(owner, repo, pr_number, page)
            all_changes = []
            for file in files:
                filename = file.get("filename", "")
                patch = file.get("patch", None)
                
                if filename.endswith(".py") and patch is not None:
                    changes = self.python_parser.parse_diff(filename, patch)
                    all_changes.extend(changes)
                    
            seen = set()
            deduped = []
            for item in all_changes:
                if item not in seen:
                    seen.add(item)
                    deduped.append(item)
                    
            return deduped
        except GitHubAPIError as e:
            raise PRError(e.message, e.status_code)
        except Exception as e:
            raise PRError(str(e), 500)

    def clean_llm_json(self, text: str) -> str:
        text = text.strip()
        if text.startswith("```"):
            text = text.split("```")[1]
            text = text.replace("json", "", 1).strip()
        if text.endswith("```"):
            text = text.rsplit("```", 1)[0].strip()
        return text

    def get_all_affected(self, symbol, graph, visited=None):
        if visited is None:
            visited = set()
        if symbol in visited:
            return visited
        visited.add(symbol)
        for caller in graph.get(symbol, []):
            self.get_all_affected(caller, graph, visited)
        return visited

    def get_depth(self, symbol, graph, depth=0, visited=None):
        if visited is None:
            visited = set()
        if symbol in visited or symbol not in graph:
            return depth
        visited.add(symbol)
        return max(
            (self.get_depth(caller, graph, depth + 1, visited) for caller in graph[symbol]),
            default=depth
        )

    def get_layer(self, node):
        parts = node.split("/")
        if "services" in parts:     return "service"
        if "controllers" in parts:  return "controller"
        if "repositories" in parts: return "repository"
        if "adapters" in parts:     return "adapter"
        if "helpers" in parts:      return "helper"
        return "other"

    def score(self, changed, direct_callers, transitive, depths, layers_crossed):
        n_direct   = len(direct_callers.get(changed, []))
        n_total    = len(transitive.get(changed, []))
        depth      = depths.get(changed, 0)
        n_layers   = len(layers_crossed.get(changed, []))

        if n_total >= 5 or depth >= 3 or n_layers >= 3:  return "CRITICAL"
        if n_total >= 3 or depth >= 2 or n_layers >= 2:  return "HIGH"
        if n_total >= 1 or depth >= 1:                    return "MEDIUM"
        return "LOW"

    async def compute_blast_radius(self, changed_nodes: list, graph: dict, nodes: list) -> dict:
        try:

            direct_callers = {}
            for changed in changed_nodes:
                if changed in graph:
                    direct_callers[changed] = graph[changed]

            transitive = {}
            for changed in changed_nodes:
                affected = self.get_all_affected(changed, graph)
                affected.discard(changed)  # don't include the symbol itself
                transitive[changed] = list(affected)

            depths = {changed: self.get_depth(changed, graph) for changed in changed_nodes}

            layers_crossed = {}
            for changed, affected in transitive.items():
                layers = set(self.get_layer(n) for n in affected)
                layers_crossed[changed] = list(layers)

            risk_scores = {c: self.score(c, direct_callers, transitive, depths, layers_crossed) for c in changed_nodes}
            overall_risk = max((self.score(r, direct_callers, transitive, depths, layers_crossed) for r in changed_nodes), 
                                        key=lambda s: ["LOW","MEDIUM","HIGH","CRITICAL"].index(s)) if changed_nodes else "LOW"

            changed_nodes.sort(key=lambda x: depths[x], reverse=True)
            
            res = {
                "changed_symbols":  changed_nodes,
                "direct_callers":   direct_callers,
                "transitive":       transitive,
                "depths":           depths,
                "layers_crossed":   layers_crossed,
                "risk_scores":      risk_scores,
                "overall_risk":     overall_risk
            }

            # If there are many critical/high risk nodes, we should only choose the top 10 nodes.
            # Else we include all.
            
            heap = []
            if len(changed_nodes) > 10:
                for node, depth in depths.items():
                    heapq.heappush(heap, (depth, node))
                    if len(heap) > 10:
                        heapq.heappop(heap)

            top_10_nodes: Set[str] = set()

            for _, node in heap:
                top_10_nodes.add(node)


            llm_payload = {
                "changed_symbols": [node for node in changed_nodes if node in top_10_nodes],
                "transitive": {node: transitive[node] for node in changed_nodes if node in top_10_nodes},
                "depths": {node: depths[node] for node in changed_nodes if node in top_10_nodes},
                "risk_scores": {node: risk_scores[node] for node in changed_nodes if node in top_10_nodes},
                "overall_risk": overall_risk
            }

            return res, llm_payload
        except Exception as e:
            raise PRError(str(e), 500)

    async def get_gen_ai_report(self, risk_payload: dict, pr_number: int) -> dict:
        try:
            payload = json.dumps({
                "changed_symbols":  risk_payload["changed_symbols"],
                "transitive":       risk_payload["transitive"],
                "depths":           risk_payload["depths"],
                "risk_scores":      risk_payload["risk_scores"],
                "overall_risk":     risk_payload["overall_risk"]
            })
            content = await self.gen_ai_api.fetch(get_gen_ai_prompt(payload, pr_number))
            return content
        except GenAIAPIError as e:
            raise PRError(e.message, e.status_code)
        except Exception as e:
            raise PRError(str(e), 500)

    async def fetch_repo_content(
        self,
        owner: str,
        repo: str,
        pr_number: int,
        max_depth: int = 5
    ) -> Dict[str, List[str]]:

        if owner == "mock" and repo == "mock" and pr_number == 1:
            await asyncio.sleep(3)
            return MOCK_DATA.get("graph", {}).get("graph", {}), MOCK_DATA.get("graph", {}).get("nodes", [])

        try:
            pr_data = await self.github_api.fetch_pr(owner, repo, pr_number)
            branch = pr_data.get("head", {}).get("ref", "main")

            if pr_data.get("state") != "open":
                raise PRError("PR is not open", 400)

            if pr_data.get("user", {}).get("login") == "":
                raise PRError("PR is not from user", 400)
            
            queue = [(get_github_repo_content_for_branch(owner, repo, branch), 0)]
            file_cache: Dict[str, str] = {}
            all_python_urls: Set[str] = set()
            nodes: Set[str] = set()
            name_index: Dict[str, List[str]] = {}

            while queue:
                url, depth = queue.pop(0)
                if depth > max_depth:
                    continue
                    
                try:
                    contents = await self.github_api.fetch_repo_content(url)
                except Exception:
                    continue
                    
                if isinstance(contents, list):
                    for item in contents:
                        if item.get("type") == "dir":
                            queue.append((item.get("url"), depth + 1))
                        elif item.get("type") == "file" and item.get("name", "").endswith(".py"):
                            try:
                                if item.get("url") in all_python_urls:
                                    continue
                                all_python_urls.add(item.get("url"))
                                file_content = await self.github_api.fetch_file_content(item.get("url"))
                                file_cache[item.get("url")] = file_content
                                defs = self.python_parser.extract_definitions(file_content, item.get("path"))
                                for d in defs:
                                    nodes.add(d)
                                    name = d.split("::")[-1]
                                    if name not in name_index:
                                        name_index[name] = []
                                    name_index[name].append(d)
                            except Exception:
                                continue
            
            file_data = {}
            for url, content in file_cache.items():
                parsed_url = urllib.parse.urlparse(url)
                parts = parsed_url.path.split('/contents/')
                if len(parts) < 2:
                    continue
                file_path = parts[-1]
                
                imports = self.python_parser.extract_imports(content, file_path)
                
                fixed_imports = {}
                for k, v in imports.items():
                    if "::" in v:
                        path_part, name_part = v.split("::", 1)
                        if name_part in name_index:
                            matched = False
                            for n in name_index[name_part]:
                                if n.split("::")[0].endswith(path_part):
                                    fixed_imports[k] = n
                                    matched = True
                                    break
                            if not matched and len(name_index[name_part]) == 1:
                                fixed_imports[k] = name_index[name_part][0]
                            elif not matched:
                                fixed_imports[k] = v
                        else:
                            fixed_imports[k] = v
                    else:
                        matched = False
                        for u in all_python_urls:
                            if u.endswith(v):
                                u_parts = urllib.parse.urlparse(u).path.split('/contents/')
                                if len(u_parts) >= 2:
                                    fixed_imports[k] = u_parts[-1]
                                    matched = True
                                    break
                        if not matched:
                            fixed_imports[k] = v
                imports = fixed_imports

                info = self.python_parser.extract_dependency_info(content, file_path)
                file_data[file_path] = {
                    "imports": imports,
                    "info": info
                }

            adjacency_graph: Dict[str, Set[str]] = {}
            unresolved_calls = []

            def add_edge(caller, callee):
                if callee not in adjacency_graph:
                    adjacency_graph[callee] = set()
                adjacency_graph[callee].add(caller)

            for file_path, data in file_data.items():
                imports = data["imports"]
                
                info = data["info"]
                assignments = info.get("assignments", {})
                params = info.get("params", {})
                
                for call in info.get("calls", []):
                    caller = call["caller"]
                    callee_name = call["callee_name"]
                    
                    resolved = None
                    
                    if "." in callee_name:
                        parts = callee_name.split(".")
                        obj = parts[0]
                        method = ".".join(parts[1:])
                        
                        if obj == "self":
                            if "::" in caller:
                                class_name = "::".join(caller.split("::")[:-1])
                                
                                if len(parts) == 2:
                                    candidate = f"{class_name}::{method}"
                                    if candidate in nodes:
                                        resolved = candidate
                                
                                if not resolved:
                                    attr_name = f"self.{parts[1]}"
                                    if class_name in assignments:
                                        if attr_name in assignments[class_name]:
                                            source = assignments[class_name][attr_name]
                                            init_method = f"{class_name}::__init__"
                                            
                                            if init_method in params:
                                                p_type = None
                                                for p in params[init_method]:
                                                    if isinstance(p, tuple) and p[0] == source:
                                                        p_type = p[1]
                                                        break
                                                    elif isinstance(p, str) and p == source:
                                                        for import_name in imports:
                                                            if import_name.lower().replace("_", "") == source.lower().replace("_", ""):
                                                                p_type = import_name
                                                                break
                                                    if p_type:
                                                        break
                                            if not p_type:
                                                if source in imports:
                                                    p_type = source
                                                elif source in name_index and len(name_index[source]) == 1:
                                                    p_type = source
                                            
                                            if p_type:
                                                class_node = None
                                                if p_type in imports:
                                                    class_node = imports[p_type]
                                                elif p_type in name_index:
                                                    if len(name_index[p_type]) == 1:
                                                        class_node = name_index[p_type][0]
                                                
                                                if class_node:
                                                    candidate_method = f"{class_node}::{'.'.join(parts[2:])}"
                                                    if candidate_method in nodes:
                                                        resolved = candidate_method
                        else:
                            if obj in imports:
                                base = imports[obj]
                                candidate = f"{base}::{method}"
                                if candidate in nodes:
                                    resolved = candidate
                                else:
                                    for i in range(len(parts), 0, -1):
                                        prefix = ".".join(parts[:i])
                                        if prefix in imports:
                                            base = imports[prefix]
                                            suffix = "::" + "::".join(parts[i:]) if len(parts) > i else ""
                                            cand = base + suffix
                                            if cand in nodes:
                                                resolved = cand
                                                break
                    else:
                        candidate = f"{file_path}::{callee_name}"
                        if candidate in nodes:
                            resolved = candidate
                            
                        if not resolved and "::" in caller:
                            class_name = "::".join(caller.split("::")[:-1])
                            candidate = f"{class_name}::{callee_name}"
                            if candidate in nodes:
                                resolved = candidate

                        if not resolved and callee_name in imports:
                            base = imports[callee_name]
                            if base in nodes:
                                resolved = base
                                
                            candidate_init = f"{base}::__init__"
                            if candidate_init in nodes:
                                resolved = candidate_init

                        if not resolved and callee_name in name_index:
                            matches = name_index[callee_name]
                            if len(matches) == 1:
                                resolved = matches[0]
                                candidate_init = f"{resolved}::__init__"
                                if candidate_init in nodes:
                                    resolved = candidate_init

                    if resolved and resolved in nodes:
                        add_edge(caller, resolved)
                    else:
                        unresolved_calls.append({
                            "caller": caller,
                            "call": callee_name,
                            "reason": "Could not resolve confidently"
                        })

            graph_content = {
                "graph": {k: list(v) for k, v in adjacency_graph.items()},
                "names": {key: value for key, value in name_index.items()}
            }
            graph_nodes = nodes
            return graph_content, graph_nodes

        except GitHubAPIError as e:
            raise PRError(e.message, e.status_code)
        except Exception as e:
            raise PRError(str(e), 500)