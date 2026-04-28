import base64
import binascii
import os
import httpx
from constants import get_github_pr_url, get_github_pr_files_url

class GitHubAPIError(Exception):
    def __init__(self, message: str, status_code: int):
        self.message = message
        self.status_code = status_code

class GitHubAPI:
    def __init__(self):
        self.token = os.getenv("GITHUB_API_TOKEN")
        if not self.token:
            raise ValueError("GITHUB_API_TOKEN not found")

    def _get_headers(self):
        headers = {}
        if self.token:
            headers["Authorization"] = f"token {self.token}"
        return headers

    async def fetch_pr_files_diff(self, owner: str, repo: str, pr: int, page: int = 1):
        url = get_github_pr_files_url(owner, repo, pr)
        params = {
            "per_page": 100,
            "page": page
        }
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(url, headers=self._get_headers(), timeout=30.0, params=params)
            if response.status_code == 200:
                return response.json()
            elif response.status_code == 404:
                raise GitHubAPIError(status_code=404, message="PR not found")
            elif response.status_code == 403:
                raise GitHubAPIError(status_code=403, message="GitHub API rate limit exceeded")
            else:
                raise GitHubAPIError(status_code=502, message=f"GitHub API error: {response.status_code}")
        except httpx.TimeoutException:
            raise GitHubAPIError(status_code=504, message="GitHub API timeout")
        except httpx.RequestError as e:
            raise GitHubAPIError(status_code=500, message=str(e))

    async def fetch_pr(self, owner: str, repo: str, pr: int):
        url = get_github_pr_url(owner, repo, pr)
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(url, headers=self._get_headers(), timeout=30.0)
            if response.status_code == 200:
                return response.json()
            elif response.status_code == 404:
                raise GitHubAPIError(status_code=404, message="PR not found")
            elif response.status_code == 403:
                raise GitHubAPIError(status_code=403, message="GitHub API rate limit exceeded")
            else:
                raise GitHubAPIError(status_code=502, message=f"GitHub API error: {response.status_code}")
        except httpx.TimeoutException:
            raise GitHubAPIError(status_code=504, message="GitHub API timeout")
        except httpx.RequestError as e:
            raise GitHubAPIError(status_code=500, message=str(e))

    async def fetch_repo_content(self, url: str) -> dict:
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(url, headers=self._get_headers(), timeout=30.0)
            if response.status_code == 200:
                return response.json()
            elif response.status_code == 404:
                raise GitHubAPIError(status_code=404, message="Repo not found")
            elif response.status_code == 403:
                raise GitHubAPIError(status_code=403, message="GitHub API rate limit exceeded")
            else:
                raise GitHubAPIError(status_code=502, message=f"GitHub API error: {response.status_code}")
        except httpx.TimeoutException:
            raise GitHubAPIError(status_code=504, message="GitHub API timeout")
        except httpx.RequestError as e:
            raise GitHubAPIError(status_code=500, message=str(e))

    async def fetch_file_content(self, url: str) -> dict:
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(url, headers=self._get_headers(), timeout=30.0)
            if response.status_code == 200:
                data = response.json()
                content = data.get("content", "")
                if not content:
                    return ""
                decoded = base64.b64decode(content)
                return decoded.decode("utf-8")
            elif response.status_code == 404:
                raise GitHubAPIError(status_code=404, message="File not found")
            elif response.status_code == 403:
                raise GitHubAPIError(status_code=403, message="GitHub API rate limit exceeded")
            else:
                raise GitHubAPIError(status_code=502, message=f"GitHub API error: {response.status_code}")
        except binascii.Error as e:
            raise GitHubAPIError(status_code=400, message=f"The content for the file at {url} is not a valid base64 encoding: {e}")
        except UnicodeDecodeError:
            raise GitHubAPIError(status_code=400, message=f"The content for the file at {url} is not a valid base64 encoding")
        except httpx.TimeoutException:
            raise GitHubAPIError(status_code=504, message="GitHub API timeout")
        except httpx.RequestError as e:
            raise GitHubAPIError(status_code=500, message=str(e))
