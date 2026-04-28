import json
from pydantic import BaseModel
from fastapi import Request
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from services import PRService, PRError

class BlastRadiusRequest(BaseModel):
    owner: str
    repo: str
    pr_number: int

class PRController():
    def __init__(self, pr_service: PRService):
        self.pr_service = pr_service

    def register_routes(self, app: FastAPI):
        @app.get("/api/v1/get_blast_radius/{owner}/{repo}/{pr_number}")
        async def get_blast_radius(request: Request, owner: str, repo: str, pr_number: int):
            async def event_generator():
                try:
                    user = request.state.user
                    if not user:
                        yield f"data: {json.dumps({'error': 'Unauthorized', 'status': 401})}\n\n"
                        return

                    if not owner or not repo or not pr_number:
                        yield f"data: {json.dumps({'error': 'Missing required fields', 'status': 400})}\n\n"
                        return

                    if await request.is_disconnected():
                        return

                    yield f"data: {json.dumps({'status': 'FETCHING_PR_NODES', 'message': 'Fetching Pull Requests file changes...'})}\n\n"
                    page = 1 # TODO: Implement pagination
                    nodes = await self.pr_service.get_pr_file_change_nodes(owner, repo, pr_number, page)
                    
                    if await request.is_disconnected():
                        return
                    
                    yield f"data: {json.dumps({'status': 'FOUND_PR_NODES', 'nodes': nodes})}\n\n"

                    if await request.is_disconnected():
                        return
                    
                    yield f"data: {json.dumps({'status': 'CRAWLING_REPO', 'message': f'Creating graph for {owner}/{repo}...'})}\n\n"
                    content, graph_nodes = await self.pr_service.fetch_repo_content(owner, repo, pr_number)
                    
                    if await request.is_disconnected():
                        return
                    
                    yield f"data: {json.dumps({'status': 'CRAWLED_REPO', 'content': content})}\n\n"

                    if await request.is_disconnected():
                        return

                    yield f"data: {json.dumps({'status': 'COMPUTING_BLAST_RADIUS', 'message': 'Computing blast radius...'})}\n\n"
                    res, llm_payload = await self.pr_service.compute_blast_radius(nodes, content.get("graph", {}), graph_nodes)
                    
                    if await request.is_disconnected():
                        return

                    yield f"data: {json.dumps({'status': 'COMPUTED_BLAST_RADIUS', 'res': res, 'llm_payload': llm_payload})}\n\n"

                    if await request.is_disconnected():
                        return

                    yield f"data: {json.dumps({'status': 'COMPUTING_GEN_AI_REPORT', 'message': 'Generating risk assessment report...'})}\n\n"
                    gen_ai_report = await self.pr_service.get_gen_ai_report(llm_payload, pr_number)
                    
                    if await request.is_disconnected():
                        return

                    yield f"data: {json.dumps({'status': 'COMPUTED_GEN_AI_REPORT', 'gen_ai_report': gen_ai_report})}\n\n"

                except PRError as e:
                    yield f"data: {json.dumps({'error': e.message, 'status': e.status_code})}\n\n"
                except Exception as e:
                    yield f"data: {json.dumps({'error': str(e), 'status': 500})}\n\n"

            return StreamingResponse(
                event_generator(),
                media_type="text/event-stream",
                headers={
                    "Cache-Control": "no-cache",
                    "Connection": "keep-alive",
                    "X-Accel-Buffering": "no"
                }
            )
