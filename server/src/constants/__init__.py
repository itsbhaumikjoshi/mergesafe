def get_github_pr_files_url(owner: str, repo: str, pr: int):
    return f'https://api.github.com/repos/{owner}/{repo}/pulls/{pr}/files'

def get_github_pr_url(owner: str, repo: str, pr: int):
    return f'https://api.github.com/repos/{owner}/{repo}/pulls/{pr}'

def get_github_repo_content_for_branch(owner: str, repo: str, branch: str):
    return f'https://api.github.com/repos/{owner}/{repo}/contents?ref={branch}'

def get_gen_ai_prompt(payload: str, pr_number: int) -> str:
    return f"""
        You are a senior software engineer performing a pre-merge blast radius analysis.
        You will receive structured static analysis data about a pull request and must
        produce a precise, actionable engineering report.

        ## Understanding the Payload

        You will receive a JSON object with these fields:

        **changed_symbols**
        List of fully-qualified symbols that were modified in this PR.
        Format: "file/path.py::ClassName::method_name" or "file/path.py::function_name"
        These are the SOURCE of potential impact.

        **direct_callers**
        For each changed symbol, the list of symbols that DIRECTLY call it.
        If a symbol has no entry here, nothing in the codebase directly calls it.

        **transitive**
        For each changed symbol, ALL symbols affected — directly and indirectly.
        This is the true blast radius: follow A calls B calls C calls D.
        A symbol appearing here means it WILL be affected if the changed symbol breaks.

        **depths**
        How many layers deep the ripple propagates for each changed symbol.
        depth=1 means only direct callers are affected.
        depth=3 means the change ripples through 3 layers of the call stack.
        Higher depth = harder to reason about = higher risk.

        **layers_crossed**
        Which architectural layers each change ripples into.
        Layers: "controller" (API layer), "service" (business logic),
                "repository" (database), "adapter" (external APIs), "helper" (utilities)
        Crossing more layers = higher blast radius.

        **risk_scores**
        Per-symbol risk: LOW / MEDIUM / HIGH / CRITICAL
        Computed from: number of affected symbols + depth + layers crossed.

        **overall_risk**
        The highest risk score across all changed symbols.

        ## Interpreting Symbols

        A symbol like "server/src/services/auth_service.py::AuthService::login" means:
        - File: server/src/services/auth_service.py
        - Class: AuthService
        - Method: login
        - Layer: service (inferred from "services" in path)

        A symbol like "server/src/constants/__init__.py::get_github_pr_url" means:
        - File: server/src/constants/__init__.py
        - Function: get_github_pr_url (module-level, no class)
        - Layer: helper/utility

        ## What "transitive" Means in Practice

        If changed_symbol = "JWTService::sign"
        and transitive = ["AuthService::login", "AuthController::login"]

        It means: JWTService::sign → called by AuthService::login → called by AuthController::login
        A bug in JWTService::sign will propagate to AuthService::login AND AuthController::login.
        The /login API endpoint is therefore at risk.

        ## Output Format

        Produce a structured engineering report with exactly these sections.
        Be specific. Use exact symbol names. Never invent callers or impacts not present in the data.
        
        Analyze the following blast radius payload for PR #{pr_number} and produce a report.

        ## Payload
        ```json
        {payload}
        ```

        ## Report Structure

        ### 1. Executive Summary (2-3 sentences)
        State the overall risk level, how many symbols changed, how many are affected transitively,
        and whether any user-facing endpoints are in the blast radius.

        ### 2. Changed Symbols Breakdown
        For each symbol in `changed_symbols`:
        - **Symbol**: the exact qualified name
        - **Layer**: which architectural layer it belongs to
        - **Risk**: its risk score
        - **Direct callers**: who calls it immediately
        - **Transitive impact**: the full ripple — list each affected symbol and explain
        the chain in plain English (A → B → C format)
        - **Verdict**: one sentence on what breaks if this symbol has a bug

        ### 3. Blast Radius Heatmap
        A ranked table of the most dangerous changed symbols, ordered by:
        1. Number of transitively affected symbols (descending)
        2. Depth (descending)
        3. Number of layers crossed (descending)

        Format as:
        | Symbol | Affected Count | Depth | Layers | Risk |
        |--------|---------------|-------|--------|------|

        ### 4. User-Facing Impact
        Identify which changes ripple up to controllers (API endpoints).
        For each affected controller method, state:
        - Which endpoint it represents (infer from method name e.g. login → POST /login)
        - Which changed symbol caused the impact
        - What the user-visible risk is

        ### 5. Safe Zones
        List symbols in the codebase that are NOT in any transitive set.
        These are the parts of the system confirmed safe from this PR.

        ### 6. Merge Recommendations
        Concrete, ordered action items before this PR is merged.
        Each item must reference specific symbol names from the payload.
        Format as a numbered checklist.
        Do not give generic advice. Every item must be traceable to the data.

        ---
        Be surgical. Be specific. Do not pad the report.
        If a section has nothing to report (e.g. no user-facing impact), say "None identified" and move on.
        """


GEN_AI_MODEL = 'llama-3.1-8b-instant'
GEN_AI_API_URL = 'https://api.groq.com/openai/v1/chat/completions'
GOOGLE_OAUTH_TOKEN_URL = 'https://oauth2.googleapis.com/token'
GOOGLE_OAUTH_USER_INFO_URL = 'https://openidconnect.googleapis.com/v1/userinfo'