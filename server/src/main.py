import os
import uvicorn
from src.server import Server
from dotenv import load_dotenv

load_dotenv()

server = Server()

def main():
    PORT = int(os.getenv("PORT", 5000))
    PROD = os.getenv("PROD", "false") == "true"

    uvicorn.run('main:server.app', host='0.0.0.0', port=PORT, reload=not PROD)


if __name__ == "__main__":
    main()