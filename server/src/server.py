import os
from helpers.db import engine
from helpers.db import Base
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from controllers import AuthController

class Server():

    def __init__(self):
        self.app = FastAPI()

        @self.app.on_event("startup")
        async def startup():
            async with engine.begin() as conn:
                await conn.run_sync(Base.metadata.create_all)

        FRONTEND_URL = os.getenv("FRONTEND_URL")

        self.app.add_middleware(
            CORSMiddleware,
            allow_origins=[FRONTEND_URL],
            allow_credentials=True,   # 🔥 REQUIRED
            allow_methods=["*"],
            allow_headers=["*"],
        )

        # Auth
        self.auth_controller = AuthController()

        self.register_routes()

    def register_routes(self):
        self.auth_controller.register_routes(self.app)
