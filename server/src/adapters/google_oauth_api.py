import base64
import httpx
import os
import secrets

from src.constants import GOOGLE_OAUTH_TOKEN_URL, GOOGLE_OAUTH_USER_INFO_URL

class GoogleAPIError(Exception):
    def __init__(self, message: str, status_code: int):
        self.message = message
        self.status_code = status_code

class GoogleOAuthAPI:
    def __init__(self):
        self.GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")
        self.GOOGLE_CLIENT_SECRET = os.getenv("GOOGLE_CLIENT_SECRET")
        self.GOOGLE_REDIRECT_URI = os.getenv("GOOGLE_REDIRECT_URI")
        if not self.GOOGLE_CLIENT_ID or not self.GOOGLE_CLIENT_SECRET or not self.GOOGLE_REDIRECT_URI:
            raise ValueError("Please set the GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET and GOOGLE_REDIRECT_URI environment variables")

    def generate_password(self, n_bytes: int = 32) -> str:
        random_bytes = secrets.token_bytes(n_bytes)
        return base64.urlsafe_b64encode(random_bytes).decode('utf-8').rstrip("=")

    async def fetch_user_info(self, code: str) -> dict:
        async with httpx.AsyncClient() as client:
            token_res = await client.post(
                GOOGLE_OAUTH_TOKEN_URL,
                data={
                    "code": code,
                    "client_id": self.GOOGLE_CLIENT_ID,
                    "client_secret": self.GOOGLE_CLIENT_SECRET,
                    "redirect_uri": self.GOOGLE_REDIRECT_URI,
                    "grant_type": "authorization_code",
                },
            )
            
            if token_res.status_code != 200:
                raise GoogleAPIError("Failed to authenticate with Google", 401)
                
            token_json = token_res.json()
            access_token = token_json.get("access_token")

            if not access_token:
                raise GoogleAPIError("Invalid OAuth code", 401)

            user_res = await client.get(
                GOOGLE_OAUTH_USER_INFO_URL,
                headers={"Authorization": f"Bearer {access_token}"},
            )
            
            if user_res.status_code != 200:
                raise GoogleAPIError("Failed to fetch user information from Google", 401)
                
            user = user_res.json()

            user_data = {
                "email": user.get("email"),
                "first_name": user.get("given_name"),
                "last_name": user.get("family_name"),
                "password": self.generate_password()
            }

            return user_data
        