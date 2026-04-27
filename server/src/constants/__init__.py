def get_github_pr_files_url(owner: str, repo: str, pr: int):
    return f'https://api.github.com/repos/{owner}/{repo}/pulls/{pr}/files'

def get_github_pr_url(owner: str, repo: str, pr: int):
    return f'https://api.github.com/repos/{owner}/{repo}/pulls/{pr}'

def get_github_repo_content_for_branch(owner: str, repo: str, branch: str):
    return f'https://api.github.com/repos/{owner}/{repo}/contents?ref={branch}'

GOOGLE_OAUTH_TOKEN_URL = 'https://oauth2.googleapis.com/token'
GOOGLE_OAUTH_USER_INFO_URL = 'https://openidconnect.googleapis.com/v1/userinfo'