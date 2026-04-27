from pydantic import BaseModel
from fastapi import Request
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from services import PRService, PRError

class BlastRadiusRequest(BaseModel):
    owner: str
    repo: str
    pr_number: int

class PRController():
    def __init__(self, pr_service: PRService):
        self.pr_service = pr_service

    def register_routes(self, app: FastAPI):
        @app.post("/api/v1/compute_blast_radius")
        async def compute(request: Request, data: BlastRadiusRequest):
            try:
                user = request.state.user
                if not user:
                    return JSONResponse(status_code=401, content={"message": "Unauthorized"})

                owner = data.owner
                repo = data.repo
                pr_number = data.pr_number

                if not owner or not repo or not pr_number:
                    return JSONResponse(status_code=400, content={"message": "Missing required fields"})

                page = 1 # TODO: Implement pagination
                grph = await self.pr_service.fetch_repo_content(owner, repo, pr_number)
                nodes = await self.pr_service.get_pr_file_change_nodes(owner, repo, pr_number, page)
                res = await self.pr_service.compute_blast_radius(nodes, grph.get("graph", {}), grph.get("nodes", []))
                return {
                    "graph":grph,
                    "nodes":nodes,
                    "result": res
                }
            except PRError as e:
                return JSONResponse(status_code=e.status_code, content={"message": e.message})
            except Exception as e:
                return JSONResponse(status_code=500, content={"message": str(e)})