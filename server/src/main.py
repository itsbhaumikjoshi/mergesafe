import os
import uvicorn
from server import Server
from dotenv import load_dotenv

load_dotenv()

server = Server()

def main():
    port = int(os.getenv("PORT", 5000))
    host = os.getenv("HOST", "localhost")
    prod = os.getenv("PROD", "false") == "true"
    
    app_target = "main:server.app" if not prod else server.app
    uvicorn.run(app_target, host=host, port=port, reload=not prod)


if __name__ == "__main__":
    main()