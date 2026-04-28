import tree_sitter
import tree_sitter_python
from typing import List

class PythonDiffParser:
    def __init__(self):
        self.language = tree_sitter.Language(tree_sitter_python.language())
        self.parser = tree_sitter.Parser(self.language)

    def extract_added_code(self, patch: str) -> str:
        if not patch:
            return ""
            
        lines = []
        for line in patch.splitlines():
            if line.startswith('@@'):
                parts = line.split('@@')
                if len(parts) >= 3:
                    context_hint = parts[2].strip()
                    if context_hint.startswith('def ') or context_hint.startswith('class '):
                        if context_hint.endswith('('):
                            context_hint += '): pass'
                        elif not context_hint.endswith(':'):
                            context_hint += ': pass'
                        else:
                            context_hint += ' pass'
                        lines.append(context_hint)
            elif line.startswith('+') and not line.startswith('+++'):
                lines.append(line[1:])
        return "\n".join(lines)

    def parse_diff(self, filename: str, patch: str) -> List[str]:
        code = self.extract_added_code(patch)
        if not code.strip():
            return []

        tree = self.parser.parse(bytes(code, "utf8"))
        results = []

        def traverse(node, context=None):
            if node.type in ('function_definition', 'async_function_definition'):
                name_node = node.child_by_field_name('name')
                if name_node:
                    name = name_node.text.decode('utf8')
                    if context:
                        results.append(f"{filename}::{context}::{name}")
                    else:
                        results.append(f"{filename}::{name}")
            elif node.type == 'class_definition':
                name_node = node.child_by_field_name('name')
                if name_node:
                    name = name_node.text.decode('utf8')
                    results.append(f"{filename}::{name}")
                    for child in node.children:
                        if child.type == 'block':
                            for statement in child.children:
                                if statement.type  in ('function_definition', 'async_function_definition'):
                                    method_name_node = statement.child_by_field_name('name')
                                    if method_name_node:
                                        method_name = method_name_node.text.decode('utf8')
                                        results.append(f"{filename}::{name}::{method_name}")
                                        
            for child in node.children:
                if node.type not in ('class_definition', 'function_definition', 'async_function_definition'):
                    traverse(child, context)

        traverse(tree.root_node)
        
        seen = set()
        deduped = []
        for item in results:
            if item not in seen:
                seen.add(item)
                deduped.append(item)
                
        return deduped

    def get_text(self, n) -> str:
        return n.text.decode("utf8") if n else ""

    def extract_definitions(self, code: str, filename: str) -> List[str]:
        tree = self.parser.parse(bytes(code, "utf8"))
        results = []

        def traverse(node, context=None):
            if node.type in ('function_definition', 'async_function_definition'):
                name_node = node.child_by_field_name('name')
                if name_node:
                    name = self.get_text(name_node)
                    if context:
                        results.append(f"{filename}::{context}::{name}")
                    else:
                        results.append(f"{filename}::{name}")
            elif node.type == 'class_definition':
                name_node = node.child_by_field_name('name')
                if name_node:
                    name = self.get_text(name_node)
                    results.append(f"{filename}::{name}")
                    for child in node.children:
                        if child.type == 'block':
                            for statement in child.children:
                                if statement.type in ('function_definition', 'async_function_definition'):
                                    method_name_node = statement.child_by_field_name('name')
                                    if method_name_node:
                                        method_name = self.get_text(method_name_node)
                                        results.append(f"{filename}::{name}::{method_name}")

            for child in node.children:
                if node.type not in ('class_definition', 'function_definition', 'async_function_definition'):
                    traverse(child, context)

        traverse(tree.root_node)
        
        seen = set()
        return [x for x in results if not (x in seen or seen.add(x))]

    def extract_imports(self, code: str, filename: str) -> dict:
        tree = self.parser.parse(bytes(code, "utf8"))
        resolution_map = {}
        
        import os
        current_dir = os.path.dirname(filename)
        
        for node in tree.root_node.children:
            if node.type == "import_statement":
                for child in node.children:
                    if child.type == "dotted_name":
                        name = self.get_text(child)
                        resolution_map[name] = name.replace(".", "/") + ".py"
                    elif child.type == "aliased_import":
                        dotted_name = self.get_text(child.child_by_field_name("name"))
                        alias = self.get_text(child.child_by_field_name("alias"))
                        resolution_map[alias] = dotted_name.replace(".", "/") + ".py"
            elif node.type == "import_from_statement":
                module_name = ""
                is_relative = False
                dots = 0
                
                for child in node.children:
                    if child.type == "module_name":
                        module_name = self.get_text(child)
                    elif child.type == "dotted_name" and child.prev_sibling and child.prev_sibling.type == "from":
                        module_name = self.get_text(child)
                    elif child.type == "relative_import":
                        for c in child.children:
                            if c.type == "import_prefix":
                                dots = len(self.get_text(c))
                            elif c.type == "dotted_name":
                                module_name = self.get_text(c)
                        is_relative = True
                        
                if is_relative:
                    parts = current_dir.split("/") if current_dir else []
                    if dots > 1:
                        parts = parts[:-(dots-1)]
                    if module_name:
                        parts.extend(module_name.split("."))
                    module_path = "/".join(parts) + ".py"
                else:
                    module_path = module_name.replace(".", "/") + ".py" if module_name else ""
                    
                for child in node.children:
                    if child.type == "dotted_name" and child.prev_sibling and child.prev_sibling.type == "import":
                        name = self.get_text(child)
                        resolution_map[name] = f"{module_path}::{name}"
                    elif child.type == "aliased_import":
                        name = ""
                        alias = ""
                        for c in child.children:
                            if c.type == "dotted_name" and not name:
                                name = self.get_text(c)
                            elif c.type == "identifier":
                                alias = self.get_text(c)
                        if alias and name:
                            resolution_map[alias] = f"{module_path}::{name}"
                            
        return resolution_map

    def extract_dependency_info(self, code: str, filename: str) -> dict:
        tree = self.parser.parse(bytes(code, "utf8"))
        
        info = {
            "assignments": {},  # "filename::Class" -> {"self.attr": "value_or_param"}
            "calls": [],        # [{"caller": "...", "callee_name": "...", "args": [...]}]
            "params": {}        # "filename::Class::method" -> ["param1", "param2"]
        }
        
        def traverse(node, current_class=None, current_func=None):
            caller = current_func if current_func else current_class
            if not caller:
                caller = filename

            if node.type in ('function_definition', 'async_function_definition'):
                name_node = node.child_by_field_name('name')
                if name_node:
                    name = self.get_text(name_node)
                    new_func = f"{current_class}::{name}" if current_class else f"{filename}::{name}"
                    
                    params_node = node.child_by_field_name('parameters')
                    if params_node:
                        params = []
                        for child in params_node.children:
                            if child.type == 'identifier':
                                params.append(self.get_text(child))
                            elif child.type == 'typed_parameter':
                                non_punct = [c for c in child.children if c.type not in (':', ',')]
                                if len(non_punct) >= 2:
                                    param_name = self.get_text(non_punct[0])
                                    param_type = self.get_text(non_punct[1])
                                    params.append((param_name, param_type))
                                elif len(non_punct) == 1:
                                    params.append(self.get_text(non_punct[0]))
                            elif child.type == 'parameter':
                                non_punct = [c for c in child.children if c.type not in (',',)]
                                if len(non_punct) >= 1:
                                    params.append(self.get_text(non_punct[0]))
                            elif child.type == 'default_parameter':
                                non_punct = [c for c in child.children if c.type not in ('=', ',')]
                                if len(non_punct) >= 1:
                                    params.append(self.get_text(non_punct[0]))
                            elif child.type == 'typed_default_parameter':
                                non_punct = [c for c in child.children if c.type not in (':', ',', '=')]
                                if len(non_punct) >= 2:
                                    param_name = self.get_text(non_punct[0])
                                    param_type = self.get_text(non_punct[1])
                                    params.append((param_name, param_type))
                                elif len(non_punct) == 1:
                                    params.append(self.get_text(non_punct[0]))

                        info["params"][new_func] = params

                    for child in node.children:
                        traverse(child, current_class, new_func)
                return

            elif node.type == 'class_definition':
                name_node = node.child_by_field_name('name')
                if name_node:
                    name = self.get_text(name_node)
                    new_class = f"{filename}::{name}"
                    for child in node.children:
                        traverse(child, new_class, None)
                return

            elif node.type == 'assignment':
                left = node.child_by_field_name('left')
                right = node.child_by_field_name('right')
                if left and right and current_class and current_func and current_func.endswith('::__init__'):
                    left_text = self.get_text(left)
                    if left_text.startswith('self.'):
                        if right.type == 'call':
                            func_node = right.child_by_field_name('function')
                            right_text = self.get_text(func_node) if func_node else self.get_text(right)
                        else:
                            right_text = self.get_text(right)
                        if current_class not in info["assignments"]:
                            info["assignments"][current_class] = {}
                        info["assignments"][current_class][left_text] = right_text
            
            elif node.type == 'call':
                func_node = node.child_by_field_name('function')
                args_node = node.child_by_field_name('arguments')
                if func_node:
                    callee_name = self.get_text(func_node)
                    args = []
                    if args_node:
                        for child in args_node.children:
                            if child.type not in ('(', ')', ','):
                                args.append(self.get_text(child))
                    info["calls"].append({
                        "caller": caller,
                        "callee_name": callee_name,
                        "args": args
                    })

            for child in node.children:
                traverse(child, current_class, current_func)

        traverse(tree.root_node)
        return info
