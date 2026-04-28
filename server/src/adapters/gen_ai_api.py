import os
import httpx
from src.constants import GEN_AI_MODEL, GEN_AI_API_URL, get_gen_ai_prompt

class GenAIAPIError(Exception):
    def __init__(self, message: str, status_code: int):
        self.message = message
        self.status_code = status_code

class GenAIAPI:
    def __init__(self):
        self.api_key = os.getenv("GEN_AI_API_KEY")
        if not self.api_key:
            raise ValueError("GEN_AI_API_KEY environment variable is not set")

    async def fetch(self, prompt: str) -> str:
        try:
            headers = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.api_key}"
            }
            
            body = {
                "model": GEN_AI_MODEL,
                "messages": [
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            }

            async with httpx.AsyncClient() as client:
                response = await client.post(GEN_AI_API_URL, headers=headers, json=body, timeout=30)

            if response.status_code == 200:
                data = response.json()
                content = data.get("choices", [{}])[0].get("message", {}).get("content", "")
                if not content:
                    raise GenAIAPIError("GenAI API error: invalid response", 500)
                return content

            elif response.status_code == 404:
                raise GenAIAPIError("GenAI API model not found", 404)

            elif response.status_code == 403:
                raise GenAIAPIError("GenAI API rate limit exceeded", 403,)

            else:
                raise GenAIAPIError(f"GenAI API API error: {response.status_code}", 502)

        except httpx.TimeoutException:
            raise GenAIAPIError("GenAI API API timeout", 504)

        except httpx.RequestError as e:
            raise GenAIAPIError(str(e), 500)
