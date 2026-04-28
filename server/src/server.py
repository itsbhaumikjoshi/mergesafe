import os
from helpers.db import engine, Base
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from controllers import * 
from services import *
from adapters import *
from parsers import *

class Server():

    def __init__(self):
        IS_PROD = os.getenv("prod") == "true"
        self.app = FastAPI(
            docs_url=None if IS_PROD else "/docs",
            redoc_url=None if IS_PROD else "/redoc",
            openapi_url=None if IS_PROD else "/openapi.json"
        )

        @self.app.on_event("startup")
        async def startup():
            async with engine.begin() as conn:
                await conn.run_sync(Base.metadata.create_all)

        FRONTEND_URL = os.getenv("FRONTEND_URL", "http://localhost:3000")

        self.app.add_middleware(
            CORSMiddleware,
            allow_origins=[FRONTEND_URL],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )

        # Auth
        secret = os.getenv("JWT_SECRET", "supersecret")
        jwt_service = JWTService(secret)
        auth_service = AuthService(jwt_service)
        google_oauth_api = GoogleOAuthAPI()
        oauth_service = OAuthService(jwt_service, google_oauth_api)
        self.auth_controller = AuthController(auth_service)
        self.oauth_controller = OAuthController(oauth_service, FRONTEND_URL)

        #PR
        github_api = GitHubAPI()
        gen_ai_api = GenAIAPI()
        python_parser = PythonDiffParser()
        pr_service = PRService(github_api, gen_ai_api, python_parser)
        self.pr_controller = PRController(pr_service)

        self.register_routes()

    def register_routes(self):
        self.auth_controller.register_routes(self.app)
        self.oauth_controller.register_routes(self.app)
        self.pr_controller.register_routes(self.app)