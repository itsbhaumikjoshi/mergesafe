MOCK_DATA = {
  "nodes": [
    "server/src/adapters/github_api.py::GitHubAPIError",
    "server/src/adapters/github_api.py::GitHubAPIError::__init__",
    "server/src/adapters/github_api.py::GitHubAPI",
    "server/src/adapters/github_api.py::GitHubAPI::__init__",
    "server/src/adapters/github_api.py::GitHubAPI::_get_headers",
    "server/src/adapters/github_api.py::GitHubAPI::fetch_pr_files_diff",
    "server/src/adapters/github_api.py::GitHubAPI::fetch_pr",
    "server/src/adapters/github_api.py::GitHubAPI::fetch_repo_content",
    "server/src/adapters/github_api.py::GitHubAPI::fetch_file_content",
    "server/src/adapters/google_oauth_api.py::GoogleAPIError",
    "server/src/adapters/google_oauth_api.py::GoogleAPIError::__init__",
    "server/src/adapters/google_oauth_api.py::GoogleOAuthAPI",
    "server/src/adapters/google_oauth_api.py::GoogleOAuthAPI::__init__",
    "server/src/adapters/google_oauth_api.py::GoogleOAuthAPI::generate_password",
    "server/src/adapters/google_oauth_api.py::GoogleOAuthAPI::fetch_user_info",
    "server/src/constants/__init__.py::get_github_pr_files_url",
    "server/src/constants/__init__.py::get_github_pr_url",
    "server/src/constants/__init__.py::get_github_repo_content_for_branch",
    "server/src/controllers/auth_controller.py::LoginRequest",
    "server/src/controllers/auth_controller.py::RegisterRequest",
    "server/src/controllers/auth_controller.py::AuthController",
    "server/src/controllers/auth_controller.py::AuthController::__init__",
    "server/src/controllers/auth_controller.py::AuthController::register_routes",
    "server/src/controllers/oauth_controller.py::OAuthController",
    "server/src/controllers/oauth_controller.py::OAuthController::__init__",
    "server/src/controllers/oauth_controller.py::OAuthController::register_routes",
    "server/src/controllers/pr_controller.py::BlastRadiusRequest",
    "server/src/controllers/pr_controller.py::PRController",
    "server/src/controllers/pr_controller.py::PRController::__init__",
    "server/src/controllers/pr_controller.py::PRController::register_routes",
    "server/src/helpers/db.py::get_db",
    "server/src/main.py::main",
    "server/src/models/user.py::User",
    "server/src/parsers/python_parser.py::PythonDiffParser",
    "server/src/parsers/python_parser.py::PythonDiffParser::__init__",
    "server/src/parsers/python_parser.py::PythonDiffParser::extract_added_code",
    "server/src/parsers/python_parser.py::PythonDiffParser::parse_diff",
    "server/src/parsers/python_parser.py::PythonDiffParser::get_text",
    "server/src/parsers/python_parser.py::PythonDiffParser::extract_definitions",
    "server/src/parsers/python_parser.py::PythonDiffParser::extract_imports",
    "server/src/parsers/python_parser.py::PythonDiffParser::extract_dependency_info",
    "server/src/repositories/user_repo.py::UserRepo",
    "server/src/repositories/user_repo.py::UserRepo::__init__",
    "server/src/repositories/user_repo.py::UserRepo::find_by_email",
    "server/src/repositories/user_repo.py::UserRepo::find_by_id",
    "server/src/repositories/user_repo.py::UserRepo::create_user",
    "server/src/repositories/user_repo.py::UserRepo::exists_by_email",
    "server/src/server.py::Server",
    "server/src/server.py::Server::__init__",
    "server/src/server.py::Server::register_routes",
    "server/src/services/auth_service.py::AuthError",
    "server/src/services/auth_service.py::AuthError::__init__",
    "server/src/services/auth_service.py::AuthService",
    "server/src/services/auth_service.py::AuthService::__init__",
    "server/src/services/auth_service.py::AuthService::hash_password",
    "server/src/services/auth_service.py::AuthService::verify_password",
    "server/src/services/auth_service.py::AuthService::login",
    "server/src/services/auth_service.py::AuthService::register",
    "server/src/services/auth_service.py::AuthService::get_current_user",
    "server/src/services/jwt_service.py::JWTService",
    "server/src/services/jwt_service.py::JWTService::__init__",
    "server/src/services/jwt_service.py::JWTService::sign",
    "server/src/services/jwt_service.py::JWTService::verify",
    "server/src/services/oauth_service.py::OAuthError",
    "server/src/services/oauth_service.py::OAuthError::__init__",
    "server/src/services/oauth_service.py::OAuthService",
    "server/src/services/oauth_service.py::OAuthService::__init__",
    "server/src/services/oauth_service.py::OAuthService::google_oauth",
    "server/src/services/pr_service.py::PRError",
    "server/src/services/pr_service.py::PRError::__init__",
    "server/src/services/pr_service.py::PRService",
    "server/src/services/pr_service.py::PRService::__init__",
    "server/src/services/pr_service.py::PRService::get_pr_file_change_nodes",
    "server/src/services/pr_service.py::PRService::get_all_affected",
    "server/src/services/pr_service.py::PRService::get_depth",
    "server/src/services/pr_service.py::PRService::get_layer",
    "server/src/services/pr_service.py::PRService::score",
    "server/src/services/pr_service.py::PRService::compute_blast_radius",
    "server/src/services/pr_service.py::PRService::fetch_repo_content"
  ],
  "graph": {
    "graph": {
      "server/src/server.py::Server::__init__": [
        "server/src/main.py"
      ],
      "server/src/main.py::main": [
        "server/src/main.py"
      ],
      "server/src/services/jwt_service.py::JWTService::__init__": [
        "server/src/server.py::Server::__init__"
      ],
      "server/src/services/auth_service.py::AuthService::__init__": [
        "server/src/server.py::Server::__init__"
      ],
      "server/src/adapters/google_oauth_api.py::GoogleOAuthAPI::__init__": [
        "server/src/server.py::Server::__init__"
      ],
      "server/src/services/oauth_service.py::OAuthService::__init__": [
        "server/src/server.py::Server::__init__"
      ],
      "server/src/controllers/auth_controller.py::AuthController::__init__": [
        "server/src/server.py::Server::__init__"
      ],
      "server/src/controllers/oauth_controller.py::OAuthController::__init__": [
        "server/src/server.py::Server::__init__"
      ],
      "server/src/adapters/github_api.py::GitHubAPI::__init__": [
        "server/src/server.py::Server::__init__"
      ],
      "server/src/services/pr_service.py::PRService::__init__": [
        "server/src/server.py::Server::__init__"
      ],
      "server/src/controllers/pr_controller.py::PRController::__init__": [
        "server/src/server.py::Server::__init__"
      ],
      "server/src/server.py::Server::register_routes": [
        "server/src/server.py::Server::__init__"
      ],
      "server/src/controllers/auth_controller.py::AuthController::register_routes": [
        "server/src/server.py::Server::register_routes"
      ],
      "server/src/controllers/oauth_controller.py::OAuthController::register_routes": [
        "server/src/server.py::Server::register_routes"
      ],
      "server/src/controllers/pr_controller.py::PRController::register_routes": [
        "server/src/server.py::Server::register_routes"
      ],
      "server/src/constants/__init__.py::get_github_pr_files_url": [
        "server/src/adapters/github_api.py::GitHubAPI::fetch_pr_files_diff"
      ],
      "server/src/adapters/github_api.py::GitHubAPI::_get_headers": [
        "server/src/adapters/github_api.py::GitHubAPI::fetch_pr_files_diff",
        "server/src/adapters/github_api.py::GitHubAPI::fetch_pr",
        "server/src/adapters/github_api.py::GitHubAPI::fetch_file_content",
        "server/src/adapters/github_api.py::GitHubAPI::fetch_repo_content"
      ],
      "server/src/adapters/github_api.py::GitHubAPIError": [
        "server/src/adapters/github_api.py::GitHubAPI::fetch_pr_files_diff",
        "server/src/adapters/github_api.py::GitHubAPI::fetch_pr",
        "server/src/adapters/github_api.py::GitHubAPI::fetch_file_content",
        "server/src/adapters/github_api.py::GitHubAPI::fetch_repo_content"
      ],
      "server/src/constants/__init__.py::get_github_pr_url": [
        "server/src/adapters/github_api.py::GitHubAPI::fetch_pr"
      ],
      "server/src/adapters/google_oauth_api.py::GoogleAPIError": [
        "server/src/adapters/google_oauth_api.py::GoogleOAuthAPI::fetch_user_info"
      ],
      "server/src/adapters/google_oauth_api.py::GoogleOAuthAPI::generate_password": [
        "server/src/adapters/google_oauth_api.py::GoogleOAuthAPI::fetch_user_info"
      ],
      "server/src/services/auth_service.py::AuthService::get_current_user": [
        "server/src/controllers/auth_controller.py::AuthController::auth_middleware"
      ],
      "server/src/services/auth_service.py::AuthService::login": [
        "server/src/controllers/auth_controller.py::AuthController::login"
      ],
      "server/src/services/auth_service.py::AuthService::register": [
        "server/src/controllers/auth_controller.py::AuthController::register"
      ],
      "server/src/services/oauth_service.py::OAuthService::google_oauth": [
        "server/src/controllers/oauth_controller.py::OAuthController::oauth_google"
      ],
      "server/src/services/pr_service.py::PRService::fetch_repo_content": [
        "server/src/controllers/pr_controller.py::PRController::compute"
      ],
      "server/src/services/pr_service.py::PRService::get_pr_file_change_nodes": [
        "server/src/controllers/pr_controller.py::PRController::compute"
      ],
      "server/src/services/pr_service.py::PRService::compute_blast_radius": [
        "server/src/controllers/pr_controller.py::PRController::compute"
      ],
      "server/src/parsers/python_parser.py::PythonDiffParser::extract_added_code": [
        "server/src/parsers/python_parser.py::PythonDiffParser::parse_diff"
      ],
      "server/src/parsers/python_parser.py::PythonDiffParser::get_text": [
        "server/src/parsers/python_parser.py::PythonDiffParser::traverse",
        "server/src/parsers/python_parser.py::PythonDiffParser::extract_imports"
      ],
      "server/src/models/user.py::User": [
        "server/src/repositories/user_repo.py::UserRepo::create_user"
      ],
      "server/src/repositories/user_repo.py::UserRepo::find_by_email": [
        "server/src/repositories/user_repo.py::UserRepo::exists_by_email"
      ],
      "server/src/repositories/user_repo.py::UserRepo::__init__": [
        "server/src/services/auth_service.py::AuthService::register",
        "server/src/services/auth_service.py::AuthService::get_current_user",
        "server/src/services/auth_service.py::AuthService::login",
        "server/src/services/oauth_service.py::OAuthService::google_oauth"
      ],
      "server/src/services/auth_service.py::AuthService::verify_password": [
        "server/src/services/auth_service.py::AuthService::login"
      ],
      "server/src/services/auth_service.py::AuthError": [
        "server/src/services/auth_service.py::AuthService::register",
        "server/src/services/auth_service.py::AuthService::login"
      ],
      "server/src/services/jwt_service.py::JWTService::sign": [
        "server/src/services/auth_service.py::AuthService::register",
        "server/src/services/auth_service.py::AuthService::login",
        "server/src/services/oauth_service.py::OAuthService::google_oauth"
      ],
      "server/src/services/auth_service.py::AuthService::hash_password": [
        "server/src/services/auth_service.py::AuthService::register"
      ],
      "server/src/services/jwt_service.py::JWTService::verify": [
        "server/src/services/auth_service.py::AuthService::get_current_user"
      ],
      "server/src/adapters/google_oauth_api.py::GoogleOAuthAPI::fetch_user_info": [
        "server/src/services/oauth_service.py::OAuthService::google_oauth"
      ],
      "server/src/parsers/python_parser.py::PythonDiffParser::__init__": [
        "server/src/services/pr_service.py::PRService::__init__"
      ],
      "server/src/adapters/github_api.py::GitHubAPI::fetch_pr_files_diff": [
        "server/src/services/pr_service.py::PRService::get_pr_file_change_nodes"
      ],
      "server/src/parsers/python_parser.py::PythonDiffParser::parse_diff": [
        "server/src/services/pr_service.py::PRService::get_pr_file_change_nodes"
      ],
      "server/src/services/pr_service.py::PRService::get_all_affected": [
        "server/src/services/pr_service.py::PRService::get_all_affected",
        "server/src/services/pr_service.py::PRService::compute_blast_radius"
      ],
      "server/src/services/pr_service.py::PRService::get_depth": [
        "server/src/services/pr_service.py::PRService::get_depth",
        "server/src/services/pr_service.py::PRService::compute_blast_radius"
      ],
      "server/src/services/pr_service.py::PRService::get_layer": [
        "server/src/services/pr_service.py::PRService::compute_blast_radius"
      ],
      "server/src/services/pr_service.py::PRService::score": [
        "server/src/services/pr_service.py::PRService::compute_blast_radius"
      ],
      "server/src/adapters/github_api.py::GitHubAPI::fetch_pr": [
        "server/src/services/pr_service.py::PRService::fetch_repo_content"
      ],
      "server/src/services/pr_service.py::PRError": [
        "server/src/services/pr_service.py::PRService::fetch_repo_content"
      ],
      "server/src/constants/__init__.py::get_github_repo_content_for_branch": [
        "server/src/services/pr_service.py::PRService::fetch_repo_content"
      ],
      "server/src/adapters/github_api.py::GitHubAPI::fetch_repo_content": [
        "server/src/services/pr_service.py::PRService::fetch_repo_content"
      ],
      "server/src/adapters/github_api.py::GitHubAPI::fetch_file_content": [
        "server/src/services/pr_service.py::PRService::fetch_repo_content"
      ],
      "server/src/parsers/python_parser.py::PythonDiffParser::extract_definitions": [
        "server/src/services/pr_service.py::PRService::fetch_repo_content"
      ],
      "server/src/parsers/python_parser.py::PythonDiffParser::extract_imports": [
        "server/src/services/pr_service.py::PRService::fetch_repo_content"
      ],
      "server/src/parsers/python_parser.py::PythonDiffParser::extract_dependency_info": [
        "server/src/services/pr_service.py::PRService::fetch_repo_content"
      ]
    },
    "unresolved_calls": [
      {
        "caller": "server/src/main.py",
        "call": "load_dotenv",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/main.py::main",
        "call": "int",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/main.py::main",
        "call": "os.getenv",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/main.py::main",
        "call": "os.getenv",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/main.py::main",
        "call": "os.getenv",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/main.py::main",
        "call": "uvicorn.run",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/server.py::Server::__init__",
        "call": "FastAPI",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/server.py::Server::__init__",
        "call": "self.app.on_event",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/server.py::Server::startup",
        "call": "engine.begin",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/server.py::Server::startup",
        "call": "conn.run_sync",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/server.py::Server::__init__",
        "call": "os.getenv",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/server.py::Server::__init__",
        "call": "self.app.add_middleware",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/server.py::Server::__init__",
        "call": "os.getenv",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/adapters/github_api.py::GitHubAPI::__init__",
        "call": "os.getenv",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/adapters/github_api.py::GitHubAPI::__init__",
        "call": "ValueError",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/adapters/github_api.py::GitHubAPI::fetch_pr_files_diff",
        "call": "httpx.AsyncClient",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/adapters/github_api.py::GitHubAPI::fetch_pr_files_diff",
        "call": "client.get",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/adapters/github_api.py::GitHubAPI::fetch_pr_files_diff",
        "call": "response.json",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/adapters/github_api.py::GitHubAPI::fetch_pr_files_diff",
        "call": "str",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/adapters/github_api.py::GitHubAPI::fetch_pr",
        "call": "httpx.AsyncClient",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/adapters/github_api.py::GitHubAPI::fetch_pr",
        "call": "client.get",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/adapters/github_api.py::GitHubAPI::fetch_pr",
        "call": "response.json",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/adapters/github_api.py::GitHubAPI::fetch_pr",
        "call": "str",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/adapters/github_api.py::GitHubAPI::fetch_repo_content",
        "call": "httpx.AsyncClient",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/adapters/github_api.py::GitHubAPI::fetch_repo_content",
        "call": "client.get",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/adapters/github_api.py::GitHubAPI::fetch_repo_content",
        "call": "response.json",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/adapters/github_api.py::GitHubAPI::fetch_repo_content",
        "call": "str",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/adapters/github_api.py::GitHubAPI::fetch_file_content",
        "call": "httpx.AsyncClient",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/adapters/github_api.py::GitHubAPI::fetch_file_content",
        "call": "client.get",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/adapters/github_api.py::GitHubAPI::fetch_file_content",
        "call": "response.json",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/adapters/github_api.py::GitHubAPI::fetch_file_content",
        "call": "data.get",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/adapters/github_api.py::GitHubAPI::fetch_file_content",
        "call": "base64.b64decode",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/adapters/github_api.py::GitHubAPI::fetch_file_content",
        "call": "decoded.decode",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/adapters/github_api.py::GitHubAPI::fetch_file_content",
        "call": "str",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/adapters/google_oauth_api.py::GoogleOAuthAPI::__init__",
        "call": "os.getenv",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/adapters/google_oauth_api.py::GoogleOAuthAPI::__init__",
        "call": "os.getenv",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/adapters/google_oauth_api.py::GoogleOAuthAPI::__init__",
        "call": "os.getenv",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/adapters/google_oauth_api.py::GoogleOAuthAPI::__init__",
        "call": "ValueError",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/adapters/google_oauth_api.py::GoogleOAuthAPI::generate_password",
        "call": "secrets.token_bytes",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/adapters/google_oauth_api.py::GoogleOAuthAPI::generate_password",
        "call": "base64.urlsafe_b64encode(random_bytes).decode('utf-8').rstrip",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/adapters/google_oauth_api.py::GoogleOAuthAPI::generate_password",
        "call": "base64.urlsafe_b64encode(random_bytes).decode",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/adapters/google_oauth_api.py::GoogleOAuthAPI::generate_password",
        "call": "base64.urlsafe_b64encode",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/adapters/google_oauth_api.py::GoogleOAuthAPI::fetch_user_info",
        "call": "httpx.AsyncClient",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/adapters/google_oauth_api.py::GoogleOAuthAPI::fetch_user_info",
        "call": "client.post",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/adapters/google_oauth_api.py::GoogleOAuthAPI::fetch_user_info",
        "call": "token_res.json",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/adapters/google_oauth_api.py::GoogleOAuthAPI::fetch_user_info",
        "call": "token_json.get",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/adapters/google_oauth_api.py::GoogleOAuthAPI::fetch_user_info",
        "call": "client.get",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/adapters/google_oauth_api.py::GoogleOAuthAPI::fetch_user_info",
        "call": "user_res.json",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/adapters/google_oauth_api.py::GoogleOAuthAPI::fetch_user_info",
        "call": "user.get",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/adapters/google_oauth_api.py::GoogleOAuthAPI::fetch_user_info",
        "call": "user.get",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/adapters/google_oauth_api.py::GoogleOAuthAPI::fetch_user_info",
        "call": "user.get",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/controllers/auth_controller.py::AuthController::register_routes",
        "call": "app.middleware",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/controllers/auth_controller.py::AuthController::auth_middleware",
        "call": "request.cookies.get",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/controllers/auth_controller.py::AuthController::auth_middleware",
        "call": "AsyncSessionLocal",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/controllers/auth_controller.py::AuthController::auth_middleware",
        "call": "call_next",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/controllers/auth_controller.py::AuthController::register_routes",
        "call": "app.post",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/controllers/auth_controller.py::AuthController::login",
        "call": "Depends",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/controllers/auth_controller.py::AuthController::login",
        "call": "response.set_cookie",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/controllers/auth_controller.py::AuthController::login",
        "call": "JSONResponse",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/controllers/auth_controller.py::AuthController::login",
        "call": "JSONResponse",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/controllers/auth_controller.py::AuthController::login",
        "call": "str",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/controllers/auth_controller.py::AuthController::register_routes",
        "call": "app.post",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/controllers/auth_controller.py::AuthController::register",
        "call": "Depends",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/controllers/auth_controller.py::AuthController::register",
        "call": "data.model_dump",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/controllers/auth_controller.py::AuthController::register",
        "call": "response.set_cookie",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/controllers/auth_controller.py::AuthController::register",
        "call": "JSONResponse",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/controllers/auth_controller.py::AuthController::register",
        "call": "JSONResponse",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/controllers/auth_controller.py::AuthController::register",
        "call": "str",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/controllers/auth_controller.py::AuthController::register_routes",
        "call": "app.post",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/controllers/auth_controller.py::AuthController::logout",
        "call": "response.delete_cookie",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/controllers/auth_controller.py::AuthController::register_routes",
        "call": "app.get",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/controllers/auth_controller.py::AuthController::get_me",
        "call": "JSONResponse",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/controllers/oauth_controller.py::OAuthController::register_routes",
        "call": "app.get",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/controllers/oauth_controller.py::OAuthController::oauth_google",
        "call": "Depends",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/controllers/oauth_controller.py::OAuthController::oauth_google",
        "call": "request.query_params.get",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/controllers/oauth_controller.py::OAuthController::oauth_google",
        "call": "JSONResponse",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/controllers/oauth_controller.py::OAuthController::oauth_google",
        "call": "RedirectResponse",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/controllers/oauth_controller.py::OAuthController::oauth_google",
        "call": "res.set_cookie",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/controllers/oauth_controller.py::OAuthController::oauth_google",
        "call": "JSONResponse",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/controllers/oauth_controller.py::OAuthController::oauth_google",
        "call": "JSONResponse",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/controllers/oauth_controller.py::OAuthController::oauth_google",
        "call": "JSONResponse",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/controllers/oauth_controller.py::OAuthController::oauth_google",
        "call": "str",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/controllers/pr_controller.py::PRController::register_routes",
        "call": "app.post",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/controllers/pr_controller.py::PRController::compute",
        "call": "JSONResponse",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/controllers/pr_controller.py::PRController::compute",
        "call": "JSONResponse",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/controllers/pr_controller.py::PRController::compute",
        "call": "grph.get",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/controllers/pr_controller.py::PRController::compute",
        "call": "grph.get",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/controllers/pr_controller.py::PRController::compute",
        "call": "JSONResponse",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/controllers/pr_controller.py::PRController::compute",
        "call": "JSONResponse",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/controllers/pr_controller.py::PRController::compute",
        "call": "str",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/helpers/db.py",
        "call": "load_dotenv",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/helpers/db.py",
        "call": "os.getenv",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/helpers/db.py",
        "call": "ValueError",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/helpers/db.py",
        "call": "create_async_engine",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/helpers/db.py",
        "call": "async_sessionmaker",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/helpers/db.py",
        "call": "declarative_base",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/helpers/db.py::get_db",
        "call": "AsyncSessionLocal",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/models/user.py::User",
        "call": "Column",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/models/user.py::User",
        "call": "UUID",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/models/user.py::User",
        "call": "Column",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/models/user.py::User",
        "call": "String",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/models/user.py::User",
        "call": "Column",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/models/user.py::User",
        "call": "String",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/models/user.py::User",
        "call": "Column",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/models/user.py::User",
        "call": "String",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/models/user.py::User",
        "call": "Column",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/models/user.py::User",
        "call": "String",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/models/user.py::User",
        "call": "Column",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/models/user.py::User",
        "call": "DateTime",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/models/user.py::User",
        "call": "func.now",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/models/user.py::User",
        "call": "Column",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/models/user.py::User",
        "call": "DateTime",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/models/user.py::User",
        "call": "func.now",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/models/user.py::User",
        "call": "func.now",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/parsers/python_parser.py::PythonDiffParser::__init__",
        "call": "tree_sitter.Language",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/parsers/python_parser.py::PythonDiffParser::__init__",
        "call": "tree_sitter_python.language",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/parsers/python_parser.py::PythonDiffParser::__init__",
        "call": "tree_sitter.Parser",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/parsers/python_parser.py::PythonDiffParser::extract_added_code",
        "call": "patch.splitlines",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/parsers/python_parser.py::PythonDiffParser::extract_added_code",
        "call": "line.startswith",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/parsers/python_parser.py::PythonDiffParser::extract_added_code",
        "call": "line.split",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/parsers/python_parser.py::PythonDiffParser::extract_added_code",
        "call": "len",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/parsers/python_parser.py::PythonDiffParser::extract_added_code",
        "call": "parts[2].strip",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/parsers/python_parser.py::PythonDiffParser::extract_added_code",
        "call": "context_hint.startswith",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/parsers/python_parser.py::PythonDiffParser::extract_added_code",
        "call": "context_hint.startswith",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/parsers/python_parser.py::PythonDiffParser::extract_added_code",
        "call": "context_hint.endswith",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/parsers/python_parser.py::PythonDiffParser::extract_added_code",
        "call": "context_hint.endswith",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/parsers/python_parser.py::PythonDiffParser::extract_added_code",
        "call": "lines.append",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/parsers/python_parser.py::PythonDiffParser::extract_added_code",
        "call": "line.startswith",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/parsers/python_parser.py::PythonDiffParser::extract_added_code",
        "call": "line.startswith",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/parsers/python_parser.py::PythonDiffParser::extract_added_code",
        "call": "lines.append",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/parsers/python_parser.py::PythonDiffParser::extract_added_code",
        "call": "\"\\n\".join",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/parsers/python_parser.py::PythonDiffParser::parse_diff",
        "call": "code.strip",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/parsers/python_parser.py::PythonDiffParser::parse_diff",
        "call": "self.parser.parse",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/parsers/python_parser.py::PythonDiffParser::parse_diff",
        "call": "bytes",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/parsers/python_parser.py::PythonDiffParser::traverse",
        "call": "node.child_by_field_name",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/parsers/python_parser.py::PythonDiffParser::traverse",
        "call": "name_node.text.decode",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/parsers/python_parser.py::PythonDiffParser::traverse",
        "call": "results.append",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/parsers/python_parser.py::PythonDiffParser::traverse",
        "call": "results.append",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/parsers/python_parser.py::PythonDiffParser::traverse",
        "call": "node.child_by_field_name",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/parsers/python_parser.py::PythonDiffParser::traverse",
        "call": "name_node.text.decode",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/parsers/python_parser.py::PythonDiffParser::traverse",
        "call": "results.append",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/parsers/python_parser.py::PythonDiffParser::traverse",
        "call": "statement.child_by_field_name",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/parsers/python_parser.py::PythonDiffParser::traverse",
        "call": "method_name_node.text.decode",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/parsers/python_parser.py::PythonDiffParser::traverse",
        "call": "results.append",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/parsers/python_parser.py::PythonDiffParser::traverse",
        "call": "traverse",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/parsers/python_parser.py::PythonDiffParser::parse_diff",
        "call": "traverse",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/parsers/python_parser.py::PythonDiffParser::parse_diff",
        "call": "set",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/parsers/python_parser.py::PythonDiffParser::parse_diff",
        "call": "seen.add",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/parsers/python_parser.py::PythonDiffParser::parse_diff",
        "call": "deduped.append",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/parsers/python_parser.py::PythonDiffParser::get_text",
        "call": "n.text.decode",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/parsers/python_parser.py::PythonDiffParser::extract_definitions",
        "call": "self.parser.parse",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/parsers/python_parser.py::PythonDiffParser::extract_definitions",
        "call": "bytes",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/parsers/python_parser.py::PythonDiffParser::traverse",
        "call": "node.child_by_field_name",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/parsers/python_parser.py::PythonDiffParser::traverse",
        "call": "results.append",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/parsers/python_parser.py::PythonDiffParser::traverse",
        "call": "results.append",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/parsers/python_parser.py::PythonDiffParser::traverse",
        "call": "node.child_by_field_name",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/parsers/python_parser.py::PythonDiffParser::traverse",
        "call": "results.append",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/parsers/python_parser.py::PythonDiffParser::traverse",
        "call": "statement.child_by_field_name",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/parsers/python_parser.py::PythonDiffParser::traverse",
        "call": "results.append",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/parsers/python_parser.py::PythonDiffParser::traverse",
        "call": "traverse",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/parsers/python_parser.py::PythonDiffParser::extract_definitions",
        "call": "traverse",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/parsers/python_parser.py::PythonDiffParser::extract_definitions",
        "call": "set",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/parsers/python_parser.py::PythonDiffParser::extract_definitions",
        "call": "seen.add",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/parsers/python_parser.py::PythonDiffParser::extract_imports",
        "call": "self.parser.parse",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/parsers/python_parser.py::PythonDiffParser::extract_imports",
        "call": "bytes",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/parsers/python_parser.py::PythonDiffParser::extract_imports",
        "call": "os.path.dirname",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/parsers/python_parser.py::PythonDiffParser::extract_imports",
        "call": "name.replace",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/parsers/python_parser.py::PythonDiffParser::extract_imports",
        "call": "child.child_by_field_name",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/parsers/python_parser.py::PythonDiffParser::extract_imports",
        "call": "child.child_by_field_name",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/parsers/python_parser.py::PythonDiffParser::extract_imports",
        "call": "dotted_name.replace",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/parsers/python_parser.py::PythonDiffParser::extract_imports",
        "call": "len",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/parsers/python_parser.py::PythonDiffParser::extract_imports",
        "call": "current_dir.split",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/parsers/python_parser.py::PythonDiffParser::extract_imports",
        "call": "parts.extend",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/parsers/python_parser.py::PythonDiffParser::extract_imports",
        "call": "module_name.split",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/parsers/python_parser.py::PythonDiffParser::extract_imports",
        "call": "\"/\".join",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/parsers/python_parser.py::PythonDiffParser::extract_imports",
        "call": "module_name.replace",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/parsers/python_parser.py::PythonDiffParser::extract_dependency_info",
        "call": "self.parser.parse",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/parsers/python_parser.py::PythonDiffParser::extract_dependency_info",
        "call": "bytes",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/parsers/python_parser.py::PythonDiffParser::traverse",
        "call": "node.child_by_field_name",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/parsers/python_parser.py::PythonDiffParser::traverse",
        "call": "node.child_by_field_name",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/parsers/python_parser.py::PythonDiffParser::traverse",
        "call": "params.append",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/parsers/python_parser.py::PythonDiffParser::traverse",
        "call": "len",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/parsers/python_parser.py::PythonDiffParser::traverse",
        "call": "params.append",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/parsers/python_parser.py::PythonDiffParser::traverse",
        "call": "len",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/parsers/python_parser.py::PythonDiffParser::traverse",
        "call": "params.append",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/parsers/python_parser.py::PythonDiffParser::traverse",
        "call": "len",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/parsers/python_parser.py::PythonDiffParser::traverse",
        "call": "params.append",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/parsers/python_parser.py::PythonDiffParser::traverse",
        "call": "len",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/parsers/python_parser.py::PythonDiffParser::traverse",
        "call": "params.append",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/parsers/python_parser.py::PythonDiffParser::traverse",
        "call": "len",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/parsers/python_parser.py::PythonDiffParser::traverse",
        "call": "params.append",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/parsers/python_parser.py::PythonDiffParser::traverse",
        "call": "len",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/parsers/python_parser.py::PythonDiffParser::traverse",
        "call": "params.append",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/parsers/python_parser.py::PythonDiffParser::traverse",
        "call": "traverse",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/parsers/python_parser.py::PythonDiffParser::traverse",
        "call": "node.child_by_field_name",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/parsers/python_parser.py::PythonDiffParser::traverse",
        "call": "traverse",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/parsers/python_parser.py::PythonDiffParser::traverse",
        "call": "node.child_by_field_name",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/parsers/python_parser.py::PythonDiffParser::traverse",
        "call": "node.child_by_field_name",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/parsers/python_parser.py::PythonDiffParser::traverse",
        "call": "current_func.endswith",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/parsers/python_parser.py::PythonDiffParser::traverse",
        "call": "left_text.startswith",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/parsers/python_parser.py::PythonDiffParser::traverse",
        "call": "right.child_by_field_name",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/parsers/python_parser.py::PythonDiffParser::traverse",
        "call": "node.child_by_field_name",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/parsers/python_parser.py::PythonDiffParser::traverse",
        "call": "node.child_by_field_name",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/parsers/python_parser.py::PythonDiffParser::traverse",
        "call": "args.append",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/parsers/python_parser.py::PythonDiffParser::traverse",
        "call": "info[\"calls\"].append",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/parsers/python_parser.py::PythonDiffParser::traverse",
        "call": "traverse",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/parsers/python_parser.py::PythonDiffParser::extract_dependency_info",
        "call": "traverse",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/repositories/user_repo.py::UserRepo::find_by_email",
        "call": "self.session.execute",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/repositories/user_repo.py::UserRepo::find_by_email",
        "call": "select(User).filter",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/repositories/user_repo.py::UserRepo::find_by_email",
        "call": "select",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/repositories/user_repo.py::UserRepo::find_by_email",
        "call": "result.scalars().first",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/repositories/user_repo.py::UserRepo::find_by_email",
        "call": "result.scalars",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/repositories/user_repo.py::UserRepo::find_by_id",
        "call": "self.session.execute",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/repositories/user_repo.py::UserRepo::find_by_id",
        "call": "select(User).filter",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/repositories/user_repo.py::UserRepo::find_by_id",
        "call": "select",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/repositories/user_repo.py::UserRepo::find_by_id",
        "call": "result.scalars().first",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/repositories/user_repo.py::UserRepo::find_by_id",
        "call": "result.scalars",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/repositories/user_repo.py::UserRepo::create_user",
        "call": "self.session.add",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/repositories/user_repo.py::UserRepo::create_user",
        "call": "self.session.commit",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/repositories/user_repo.py::UserRepo::create_user",
        "call": "self.session.refresh",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/services/auth_service.py::AuthService::hash_password",
        "call": "bcrypt.gensalt",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/services/auth_service.py::AuthService::hash_password",
        "call": "bcrypt.hashpw(password.encode('utf-8'), salt).decode",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/services/auth_service.py::AuthService::hash_password",
        "call": "bcrypt.hashpw",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/services/auth_service.py::AuthService::hash_password",
        "call": "password.encode",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/services/auth_service.py::AuthService::verify_password",
        "call": "bcrypt.checkpw",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/services/auth_service.py::AuthService::verify_password",
        "call": "plain_password.encode",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/services/auth_service.py::AuthService::verify_password",
        "call": "hashed_password.encode",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/services/auth_service.py::AuthService::login",
        "call": "repo.find_by_email",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/services/auth_service.py::AuthService::login",
        "call": "str",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/services/auth_service.py::AuthService::register",
        "call": "repo.exists_by_email",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/services/auth_service.py::AuthService::register",
        "call": "repo.create_user",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/services/auth_service.py::AuthService::register",
        "call": "str",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/services/auth_service.py::AuthService::get_current_user",
        "call": "payload.get",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/services/auth_service.py::AuthService::get_current_user",
        "call": "repo.find_by_id",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/services/jwt_service.py::JWTService::sign",
        "call": "payload.copy",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/services/jwt_service.py::JWTService::sign",
        "call": "datetime.utcnow",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/services/jwt_service.py::JWTService::sign",
        "call": "timedelta",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/services/jwt_service.py::JWTService::sign",
        "call": "data.update",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/services/jwt_service.py::JWTService::sign",
        "call": "datetime.utcnow",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/services/jwt_service.py::JWTService::sign",
        "call": "jwt.encode",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/services/jwt_service.py::JWTService::verify",
        "call": "jwt.decode",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/services/jwt_service.py::JWTService::verify",
        "call": "Exception",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/services/jwt_service.py::JWTService::verify",
        "call": "str",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/services/oauth_service.py::OAuthService::google_oauth",
        "call": "repo.find_by_email",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/services/oauth_service.py::OAuthService::google_oauth",
        "call": "user_data.get",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/services/oauth_service.py::OAuthService::google_oauth",
        "call": "repo.create_user",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/services/oauth_service.py::OAuthService::google_oauth",
        "call": "str",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/services/pr_service.py::PRService::get_pr_file_change_nodes",
        "call": "file.get",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/services/pr_service.py::PRService::get_pr_file_change_nodes",
        "call": "file.get",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/services/pr_service.py::PRService::get_pr_file_change_nodes",
        "call": "filename.endswith",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/services/pr_service.py::PRService::get_pr_file_change_nodes",
        "call": "all_changes.extend",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/services/pr_service.py::PRService::get_pr_file_change_nodes",
        "call": "set",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/services/pr_service.py::PRService::get_pr_file_change_nodes",
        "call": "seen.add",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/services/pr_service.py::PRService::get_pr_file_change_nodes",
        "call": "deduped.append",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/services/pr_service.py::PRService::get_all_affected",
        "call": "set",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/services/pr_service.py::PRService::get_all_affected",
        "call": "visited.add",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/services/pr_service.py::PRService::get_all_affected",
        "call": "graph.get",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/services/pr_service.py::PRService::get_depth",
        "call": "set",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/services/pr_service.py::PRService::get_depth",
        "call": "visited.add",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/services/pr_service.py::PRService::get_depth",
        "call": "max",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/services/pr_service.py::PRService::get_layer",
        "call": "node.split",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/services/pr_service.py::PRService::score",
        "call": "len",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/services/pr_service.py::PRService::score",
        "call": "direct_callers.get",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/services/pr_service.py::PRService::score",
        "call": "len",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/services/pr_service.py::PRService::score",
        "call": "transitive.get",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/services/pr_service.py::PRService::score",
        "call": "depths.get",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/services/pr_service.py::PRService::score",
        "call": "len",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/services/pr_service.py::PRService::score",
        "call": "layers_crossed.get",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/services/pr_service.py::PRService::compute_blast_radius",
        "call": "affected.discard",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/services/pr_service.py::PRService::compute_blast_radius",
        "call": "list",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/services/pr_service.py::PRService::compute_blast_radius",
        "call": "transitive.items",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/services/pr_service.py::PRService::compute_blast_radius",
        "call": "set",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/services/pr_service.py::PRService::compute_blast_radius",
        "call": "list",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/services/pr_service.py::PRService::compute_blast_radius",
        "call": "max",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/services/pr_service.py::PRService::compute_blast_radius",
        "call": "[\"LOW\",\"MEDIUM\",\"HIGH\",\"CRITICAL\"].index",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/services/pr_service.py::PRService::fetch_repo_content",
        "call": "pr_data.get(\"head\", {}).get",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/services/pr_service.py::PRService::fetch_repo_content",
        "call": "pr_data.get",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/services/pr_service.py::PRService::fetch_repo_content",
        "call": "pr_data.get",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/services/pr_service.py::PRService::fetch_repo_content",
        "call": "pr_data.get(\"user\", {}).get",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/services/pr_service.py::PRService::fetch_repo_content",
        "call": "pr_data.get",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/services/pr_service.py::PRService::fetch_repo_content",
        "call": "set",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/services/pr_service.py::PRService::fetch_repo_content",
        "call": "set",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/services/pr_service.py::PRService::fetch_repo_content",
        "call": "queue.pop",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/services/pr_service.py::PRService::fetch_repo_content",
        "call": "isinstance",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/services/pr_service.py::PRService::fetch_repo_content",
        "call": "item.get",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/services/pr_service.py::PRService::fetch_repo_content",
        "call": "queue.append",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/services/pr_service.py::PRService::fetch_repo_content",
        "call": "item.get",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/services/pr_service.py::PRService::fetch_repo_content",
        "call": "item.get",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/services/pr_service.py::PRService::fetch_repo_content",
        "call": "item.get(\"name\", \"\").endswith",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/services/pr_service.py::PRService::fetch_repo_content",
        "call": "item.get",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/services/pr_service.py::PRService::fetch_repo_content",
        "call": "item.get",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/services/pr_service.py::PRService::fetch_repo_content",
        "call": "all_python_urls.add",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/services/pr_service.py::PRService::fetch_repo_content",
        "call": "item.get",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/services/pr_service.py::PRService::fetch_repo_content",
        "call": "item.get",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/services/pr_service.py::PRService::fetch_repo_content",
        "call": "item.get",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/services/pr_service.py::PRService::fetch_repo_content",
        "call": "item.get",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/services/pr_service.py::PRService::fetch_repo_content",
        "call": "nodes.add",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/services/pr_service.py::PRService::fetch_repo_content",
        "call": "d.split",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/services/pr_service.py::PRService::fetch_repo_content",
        "call": "name_index[name].append",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/services/pr_service.py::PRService::fetch_repo_content",
        "call": "file_cache.items",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/services/pr_service.py::PRService::fetch_repo_content",
        "call": "urllib.parse.urlparse",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/services/pr_service.py::PRService::fetch_repo_content",
        "call": "parsed_url.path.split",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/services/pr_service.py::PRService::fetch_repo_content",
        "call": "len",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/services/pr_service.py::PRService::fetch_repo_content",
        "call": "imports.items",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/services/pr_service.py::PRService::fetch_repo_content",
        "call": "v.split",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/services/pr_service.py::PRService::fetch_repo_content",
        "call": "n.split(\"::\")[0].endswith",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/services/pr_service.py::PRService::fetch_repo_content",
        "call": "n.split",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/services/pr_service.py::PRService::fetch_repo_content",
        "call": "len",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/services/pr_service.py::PRService::fetch_repo_content",
        "call": "u.endswith",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/services/pr_service.py::PRService::fetch_repo_content",
        "call": "urllib.parse.urlparse(u).path.split",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/services/pr_service.py::PRService::fetch_repo_content",
        "call": "urllib.parse.urlparse",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/services/pr_service.py::PRService::fetch_repo_content",
        "call": "len",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/services/pr_service.py::PRService::add_edge",
        "call": "set",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/services/pr_service.py::PRService::add_edge",
        "call": "adjacency_graph[callee].add",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/services/pr_service.py::PRService::fetch_repo_content",
        "call": "file_data.items",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/services/pr_service.py::PRService::fetch_repo_content",
        "call": "info.get",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/services/pr_service.py::PRService::fetch_repo_content",
        "call": "info.get",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/services/pr_service.py::PRService::fetch_repo_content",
        "call": "info.get",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/services/pr_service.py::PRService::fetch_repo_content",
        "call": "callee_name.split",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/services/pr_service.py::PRService::fetch_repo_content",
        "call": "\".\".join",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/services/pr_service.py::PRService::fetch_repo_content",
        "call": "\"::\".join",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/services/pr_service.py::PRService::fetch_repo_content",
        "call": "caller.split",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/services/pr_service.py::PRService::fetch_repo_content",
        "call": "len",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/services/pr_service.py::PRService::fetch_repo_content",
        "call": "isinstance",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/services/pr_service.py::PRService::fetch_repo_content",
        "call": "isinstance",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/services/pr_service.py::PRService::fetch_repo_content",
        "call": "import_name.lower().replace",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/services/pr_service.py::PRService::fetch_repo_content",
        "call": "import_name.lower",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/services/pr_service.py::PRService::fetch_repo_content",
        "call": "source.lower().replace",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/services/pr_service.py::PRService::fetch_repo_content",
        "call": "source.lower",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/services/pr_service.py::PRService::fetch_repo_content",
        "call": "len",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/services/pr_service.py::PRService::fetch_repo_content",
        "call": "len",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/services/pr_service.py::PRService::fetch_repo_content",
        "call": "'.'.join",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/services/pr_service.py::PRService::fetch_repo_content",
        "call": "range",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/services/pr_service.py::PRService::fetch_repo_content",
        "call": "len",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/services/pr_service.py::PRService::fetch_repo_content",
        "call": "\".\".join",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/services/pr_service.py::PRService::fetch_repo_content",
        "call": "\"::\".join",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/services/pr_service.py::PRService::fetch_repo_content",
        "call": "len",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/services/pr_service.py::PRService::fetch_repo_content",
        "call": "\"::\".join",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/services/pr_service.py::PRService::fetch_repo_content",
        "call": "caller.split",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/services/pr_service.py::PRService::fetch_repo_content",
        "call": "len",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/services/pr_service.py::PRService::fetch_repo_content",
        "call": "add_edge",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/services/pr_service.py::PRService::fetch_repo_content",
        "call": "unresolved_calls.append",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/services/pr_service.py::PRService::fetch_repo_content",
        "call": "list",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/services/pr_service.py::PRService::fetch_repo_content",
        "call": "adjacency_graph.items",
        "reason": "Could not resolve confidently"
      },
      {
        "caller": "server/src/services/pr_service.py::PRService::fetch_repo_content",
        "call": "str",
        "reason": "Could not resolve confidently"
      }
    ],
    "nodes": [
      "server/src/adapters/github_api.py::GitHubAPIError",
      "server/src/adapters/google_oauth_api.py::GoogleAPIError::__init__",
      "server/src/parsers/python_parser.py::PythonDiffParser::extract_definitions",
      "server/src/parsers/python_parser.py::PythonDiffParser::extract_dependency_info",
      "server/src/adapters/github_api.py::GitHubAPI::_get_headers",
      "server/src/adapters/github_api.py::GitHubAPI::fetch_pr_files_diff",
      "server/src/controllers/pr_controller.py::BlastRadiusRequest",
      "server/src/services/auth_service.py::AuthService::hash_password",
      "server/src/repositories/user_repo.py::UserRepo::find_by_id",
      "server/src/adapters/google_oauth_api.py::GoogleOAuthAPI::fetch_user_info",
      "server/src/constants/__init__.py::get_github_pr_files_url",
      "server/src/server.py::Server",
      "server/src/adapters/github_api.py::GitHubAPI::fetch_pr",
      "server/src/services/pr_service.py::PRError",
      "server/src/parsers/python_parser.py::PythonDiffParser",
      "server/src/services/jwt_service.py::JWTService::__init__",
      "server/src/repositories/user_repo.py::UserRepo",
      "server/src/main.py::main",
      "server/src/controllers/auth_controller.py::AuthController::register_routes",
      "server/src/services/auth_service.py::AuthService::__init__",
      "server/src/server.py::Server::__init__",
      "server/src/constants/__init__.py::get_github_repo_content_for_branch",
      "server/src/repositories/user_repo.py::UserRepo::exists_by_email",
      "server/src/adapters/github_api.py::GitHubAPI::fetch_repo_content",
      "server/src/services/auth_service.py::AuthService",
      "server/src/services/pr_service.py::PRService::get_pr_file_change_nodes",
      "server/src/services/pr_service.py::PRService",
      "server/src/adapters/google_oauth_api.py::GoogleOAuthAPI::__init__",
      "server/src/services/pr_service.py::PRService::get_layer",
      "server/src/adapters/github_api.py::GitHubAPIError::__init__",
      "server/src/repositories/user_repo.py::UserRepo::__init__",
      "server/src/parsers/python_parser.py::PythonDiffParser::extract_imports",
      "server/src/server.py::Server::register_routes",
      "server/src/services/pr_service.py::PRError::__init__",
      "server/src/helpers/db.py::get_db",
      "server/src/services/oauth_service.py::OAuthService",
      "server/src/services/pr_service.py::PRService::get_all_affected",
      "server/src/parsers/python_parser.py::PythonDiffParser::extract_added_code",
      "server/src/services/jwt_service.py::JWTService::verify",
      "server/src/services/pr_service.py::PRService::score",
      "server/src/services/oauth_service.py::OAuthError",
      "server/src/models/user.py::User",
      "server/src/adapters/github_api.py::GitHubAPI::fetch_file_content",
      "server/src/services/oauth_service.py::OAuthError::__init__",
      "server/src/services/pr_service.py::PRService::get_depth",
      "server/src/adapters/google_oauth_api.py::GoogleOAuthAPI::generate_password",
      "server/src/repositories/user_repo.py::UserRepo::find_by_email",
      "server/src/controllers/oauth_controller.py::OAuthController",
      "server/src/controllers/pr_controller.py::PRController::__init__",
      "server/src/constants/__init__.py::get_github_pr_url",
      "server/src/adapters/github_api.py::GitHubAPI",
      "server/src/controllers/auth_controller.py::AuthController::__init__",
      "server/src/services/pr_service.py::PRService::__init__",
      "server/src/services/auth_service.py::AuthError",
      "server/src/parsers/python_parser.py::PythonDiffParser::__init__",
      "server/src/services/auth_service.py::AuthService::verify_password",
      "server/src/controllers/pr_controller.py::PRController::register_routes",
      "server/src/controllers/oauth_controller.py::OAuthController::__init__",
      "server/src/parsers/python_parser.py::PythonDiffParser::parse_diff",
      "server/src/services/auth_service.py::AuthService::register",
      "server/src/controllers/auth_controller.py::RegisterRequest",
      "server/src/services/oauth_service.py::OAuthService::__init__",
      "server/src/parsers/python_parser.py::PythonDiffParser::get_text",
      "server/src/adapters/github_api.py::GitHubAPI::__init__",
      "server/src/controllers/auth_controller.py::LoginRequest",
      "server/src/services/pr_service.py::PRService::compute_blast_radius",
      "server/src/services/auth_service.py::AuthService::login",
      "server/src/services/oauth_service.py::OAuthService::google_oauth",
      "server/src/adapters/google_oauth_api.py::GoogleAPIError",
      "server/src/services/auth_service.py::AuthError::__init__",
      "server/src/controllers/oauth_controller.py::OAuthController::register_routes",
      "server/src/services/jwt_service.py::JWTService",
      "server/src/repositories/user_repo.py::UserRepo::create_user",
      "server/src/services/auth_service.py::AuthService::get_current_user",
      "server/src/controllers/pr_controller.py::PRController",
      "server/src/services/jwt_service.py::JWTService::sign",
      "server/src/services/pr_service.py::PRService::fetch_repo_content",
      "server/src/adapters/google_oauth_api.py::GoogleOAuthAPI",
      "server/src/controllers/auth_controller.py::AuthController"
    ],
    "names": {
      "main": [
        "server/src/main.py::main"
      ],
      "Server": [
        "server/src/server.py::Server"
      ],
      "__init__": [
        "server/src/server.py::Server::__init__",
        "server/src/adapters/github_api.py::GitHubAPIError::__init__",
        "server/src/adapters/github_api.py::GitHubAPI::__init__",
        "server/src/adapters/google_oauth_api.py::GoogleAPIError::__init__",
        "server/src/adapters/google_oauth_api.py::GoogleOAuthAPI::__init__",
        "server/src/controllers/auth_controller.py::AuthController::__init__",
        "server/src/controllers/oauth_controller.py::OAuthController::__init__",
        "server/src/controllers/pr_controller.py::PRController::__init__",
        "server/src/parsers/python_parser.py::PythonDiffParser::__init__",
        "server/src/repositories/user_repo.py::UserRepo::__init__",
        "server/src/services/auth_service.py::AuthError::__init__",
        "server/src/services/auth_service.py::AuthService::__init__",
        "server/src/services/jwt_service.py::JWTService::__init__",
        "server/src/services/oauth_service.py::OAuthError::__init__",
        "server/src/services/oauth_service.py::OAuthService::__init__",
        "server/src/services/pr_service.py::PRError::__init__",
        "server/src/services/pr_service.py::PRService::__init__"
      ],
      "register_routes": [
        "server/src/server.py::Server::register_routes",
        "server/src/controllers/auth_controller.py::AuthController::register_routes",
        "server/src/controllers/oauth_controller.py::OAuthController::register_routes",
        "server/src/controllers/pr_controller.py::PRController::register_routes"
      ],
      "GitHubAPIError": [
        "server/src/adapters/github_api.py::GitHubAPIError"
      ],
      "GitHubAPI": [
        "server/src/adapters/github_api.py::GitHubAPI"
      ],
      "_get_headers": [
        "server/src/adapters/github_api.py::GitHubAPI::_get_headers"
      ],
      "fetch_pr_files_diff": [
        "server/src/adapters/github_api.py::GitHubAPI::fetch_pr_files_diff"
      ],
      "fetch_pr": [
        "server/src/adapters/github_api.py::GitHubAPI::fetch_pr"
      ],
      "fetch_repo_content": [
        "server/src/adapters/github_api.py::GitHubAPI::fetch_repo_content",
        "server/src/services/pr_service.py::PRService::fetch_repo_content"
      ],
      "fetch_file_content": [
        "server/src/adapters/github_api.py::GitHubAPI::fetch_file_content"
      ],
      "GoogleAPIError": [
        "server/src/adapters/google_oauth_api.py::GoogleAPIError"
      ],
      "GoogleOAuthAPI": [
        "server/src/adapters/google_oauth_api.py::GoogleOAuthAPI"
      ],
      "generate_password": [
        "server/src/adapters/google_oauth_api.py::GoogleOAuthAPI::generate_password"
      ],
      "fetch_user_info": [
        "server/src/adapters/google_oauth_api.py::GoogleOAuthAPI::fetch_user_info"
      ],
      "get_github_pr_files_url": [
        "server/src/constants/__init__.py::get_github_pr_files_url"
      ],
      "get_github_pr_url": [
        "server/src/constants/__init__.py::get_github_pr_url"
      ],
      "get_github_repo_content_for_branch": [
        "server/src/constants/__init__.py::get_github_repo_content_for_branch"
      ],
      "LoginRequest": [
        "server/src/controllers/auth_controller.py::LoginRequest"
      ],
      "RegisterRequest": [
        "server/src/controllers/auth_controller.py::RegisterRequest"
      ],
      "AuthController": [
        "server/src/controllers/auth_controller.py::AuthController"
      ],
      "OAuthController": [
        "server/src/controllers/oauth_controller.py::OAuthController"
      ],
      "BlastRadiusRequest": [
        "server/src/controllers/pr_controller.py::BlastRadiusRequest"
      ],
      "PRController": [
        "server/src/controllers/pr_controller.py::PRController"
      ],
      "get_db": [
        "server/src/helpers/db.py::get_db"
      ],
      "User": [
        "server/src/models/user.py::User"
      ],
      "PythonDiffParser": [
        "server/src/parsers/python_parser.py::PythonDiffParser"
      ],
      "extract_added_code": [
        "server/src/parsers/python_parser.py::PythonDiffParser::extract_added_code"
      ],
      "parse_diff": [
        "server/src/parsers/python_parser.py::PythonDiffParser::parse_diff"
      ],
      "get_text": [
        "server/src/parsers/python_parser.py::PythonDiffParser::get_text"
      ],
      "extract_definitions": [
        "server/src/parsers/python_parser.py::PythonDiffParser::extract_definitions"
      ],
      "extract_imports": [
        "server/src/parsers/python_parser.py::PythonDiffParser::extract_imports"
      ],
      "extract_dependency_info": [
        "server/src/parsers/python_parser.py::PythonDiffParser::extract_dependency_info"
      ],
      "UserRepo": [
        "server/src/repositories/user_repo.py::UserRepo"
      ],
      "find_by_email": [
        "server/src/repositories/user_repo.py::UserRepo::find_by_email"
      ],
      "find_by_id": [
        "server/src/repositories/user_repo.py::UserRepo::find_by_id"
      ],
      "create_user": [
        "server/src/repositories/user_repo.py::UserRepo::create_user"
      ],
      "exists_by_email": [
        "server/src/repositories/user_repo.py::UserRepo::exists_by_email"
      ],
      "AuthError": [
        "server/src/services/auth_service.py::AuthError"
      ],
      "AuthService": [
        "server/src/services/auth_service.py::AuthService"
      ],
      "hash_password": [
        "server/src/services/auth_service.py::AuthService::hash_password"
      ],
      "verify_password": [
        "server/src/services/auth_service.py::AuthService::verify_password"
      ],
      "login": [
        "server/src/services/auth_service.py::AuthService::login"
      ],
      "register": [
        "server/src/services/auth_service.py::AuthService::register"
      ],
      "get_current_user": [
        "server/src/services/auth_service.py::AuthService::get_current_user"
      ],
      "JWTService": [
        "server/src/services/jwt_service.py::JWTService"
      ],
      "sign": [
        "server/src/services/jwt_service.py::JWTService::sign"
      ],
      "verify": [
        "server/src/services/jwt_service.py::JWTService::verify"
      ],
      "OAuthError": [
        "server/src/services/oauth_service.py::OAuthError"
      ],
      "OAuthService": [
        "server/src/services/oauth_service.py::OAuthService"
      ],
      "google_oauth": [
        "server/src/services/oauth_service.py::OAuthService::google_oauth"
      ],
      "PRError": [
        "server/src/services/pr_service.py::PRError"
      ],
      "PRService": [
        "server/src/services/pr_service.py::PRService"
      ],
      "get_pr_file_change_nodes": [
        "server/src/services/pr_service.py::PRService::get_pr_file_change_nodes"
      ],
      "get_all_affected": [
        "server/src/services/pr_service.py::PRService::get_all_affected"
      ],
      "get_depth": [
        "server/src/services/pr_service.py::PRService::get_depth"
      ],
      "get_layer": [
        "server/src/services/pr_service.py::PRService::get_layer"
      ],
      "score": [
        "server/src/services/pr_service.py::PRService::score"
      ],
      "compute_blast_radius": [
        "server/src/services/pr_service.py::PRService::compute_blast_radius"
      ]
    }
  },
  "result": {
    "changed_symbols": [
      "server/src/adapters/github_api.py::GitHubAPIError",
      "server/src/adapters/github_api.py::GitHubAPIError::__init__",
      "server/src/adapters/github_api.py::GitHubAPI",
      "server/src/adapters/github_api.py::GitHubAPI::__init__",
      "server/src/adapters/github_api.py::GitHubAPI::_get_headers",
      "server/src/adapters/github_api.py::GitHubAPI::fetch_pr_files_diff",
      "server/src/adapters/github_api.py::GitHubAPI::fetch_pr",
      "server/src/adapters/github_api.py::GitHubAPI::fetch_repo_content",
      "server/src/adapters/github_api.py::GitHubAPI::fetch_file_content",
      "server/src/adapters/google_oauth_api.py::GoogleAPIError",
      "server/src/adapters/google_oauth_api.py::GoogleAPIError::__init__",
      "server/src/adapters/google_oauth_api.py::GoogleOAuthAPI",
      "server/src/adapters/google_oauth_api.py::GoogleOAuthAPI::__init__",
      "server/src/adapters/google_oauth_api.py::GoogleOAuthAPI::generate_password",
      "server/src/adapters/google_oauth_api.py::GoogleOAuthAPI::fetch_user_info",
      "server/src/constants/__init__.py::get_github_pr_files_url",
      "server/src/constants/__init__.py::get_github_pr_url",
      "server/src/constants/__init__.py::get_github_repo_content_for_branch",
      "server/src/controllers/auth_controller.py::LoginRequest",
      "server/src/controllers/auth_controller.py::RegisterRequest",
      "server/src/controllers/auth_controller.py::AuthController",
      "server/src/controllers/auth_controller.py::AuthController::__init__",
      "server/src/controllers/auth_controller.py::AuthController::register_routes",
      "server/src/controllers/oauth_controller.py::OAuthController",
      "server/src/controllers/oauth_controller.py::OAuthController::__init__",
      "server/src/controllers/oauth_controller.py::OAuthController::register_routes",
      "server/src/controllers/pr_controller.py::BlastRadiusRequest",
      "server/src/controllers/pr_controller.py::PRController",
      "server/src/controllers/pr_controller.py::PRController::__init__",
      "server/src/controllers/pr_controller.py::PRController::register_routes",
      "server/src/helpers/db.py::get_db",
      "server/src/main.py::main",
      "server/src/models/user.py::User",
      "server/src/parsers/python_parser.py::PythonDiffParser",
      "server/src/parsers/python_parser.py::PythonDiffParser::__init__",
      "server/src/parsers/python_parser.py::PythonDiffParser::extract_added_code",
      "server/src/parsers/python_parser.py::PythonDiffParser::parse_diff",
      "server/src/parsers/python_parser.py::PythonDiffParser::get_text",
      "server/src/parsers/python_parser.py::PythonDiffParser::extract_definitions",
      "server/src/parsers/python_parser.py::PythonDiffParser::extract_imports",
      "server/src/parsers/python_parser.py::PythonDiffParser::extract_dependency_info",
      "server/src/repositories/user_repo.py::UserRepo",
      "server/src/repositories/user_repo.py::UserRepo::__init__",
      "server/src/repositories/user_repo.py::UserRepo::find_by_email",
      "server/src/repositories/user_repo.py::UserRepo::find_by_id",
      "server/src/repositories/user_repo.py::UserRepo::create_user",
      "server/src/repositories/user_repo.py::UserRepo::exists_by_email",
      "server/src/server.py::Server",
      "server/src/server.py::Server::__init__",
      "server/src/server.py::Server::register_routes",
      "server/src/services/auth_service.py::AuthError",
      "server/src/services/auth_service.py::AuthError::__init__",
      "server/src/services/auth_service.py::AuthService",
      "server/src/services/auth_service.py::AuthService::__init__",
      "server/src/services/auth_service.py::AuthService::hash_password",
      "server/src/services/auth_service.py::AuthService::verify_password",
      "server/src/services/auth_service.py::AuthService::login",
      "server/src/services/auth_service.py::AuthService::register",
      "server/src/services/auth_service.py::AuthService::get_current_user",
      "server/src/services/jwt_service.py::JWTService",
      "server/src/services/jwt_service.py::JWTService::__init__",
      "server/src/services/jwt_service.py::JWTService::sign",
      "server/src/services/jwt_service.py::JWTService::verify",
      "server/src/services/oauth_service.py::OAuthError",
      "server/src/services/oauth_service.py::OAuthError::__init__",
      "server/src/services/oauth_service.py::OAuthService",
      "server/src/services/oauth_service.py::OAuthService::__init__",
      "server/src/services/oauth_service.py::OAuthService::google_oauth",
      "server/src/services/pr_service.py::PRError",
      "server/src/services/pr_service.py::PRError::__init__",
      "server/src/services/pr_service.py::PRService",
      "server/src/services/pr_service.py::PRService::__init__",
      "server/src/services/pr_service.py::PRService::get_pr_file_change_nodes",
      "server/src/services/pr_service.py::PRService::get_all_affected",
      "server/src/services/pr_service.py::PRService::get_depth",
      "server/src/services/pr_service.py::PRService::get_layer",
      "server/src/services/pr_service.py::PRService::score",
      "server/src/services/pr_service.py::PRService::compute_blast_radius",
      "server/src/services/pr_service.py::PRService::fetch_repo_content"
    ],
    "direct_callers": {
      "server/src/adapters/github_api.py::GitHubAPIError": [
        "server/src/adapters/github_api.py::GitHubAPI::fetch_pr_files_diff",
        "server/src/adapters/github_api.py::GitHubAPI::fetch_pr",
        "server/src/adapters/github_api.py::GitHubAPI::fetch_file_content",
        "server/src/adapters/github_api.py::GitHubAPI::fetch_repo_content"
      ],
      "server/src/adapters/github_api.py::GitHubAPI::__init__": [
        "server/src/server.py::Server::__init__"
      ],
      "server/src/adapters/github_api.py::GitHubAPI::_get_headers": [
        "server/src/adapters/github_api.py::GitHubAPI::fetch_pr_files_diff",
        "server/src/adapters/github_api.py::GitHubAPI::fetch_pr",
        "server/src/adapters/github_api.py::GitHubAPI::fetch_file_content",
        "server/src/adapters/github_api.py::GitHubAPI::fetch_repo_content"
      ],
      "server/src/adapters/github_api.py::GitHubAPI::fetch_pr_files_diff": [
        "server/src/services/pr_service.py::PRService::get_pr_file_change_nodes"
      ],
      "server/src/adapters/github_api.py::GitHubAPI::fetch_pr": [
        "server/src/services/pr_service.py::PRService::fetch_repo_content"
      ],
      "server/src/adapters/github_api.py::GitHubAPI::fetch_repo_content": [
        "server/src/services/pr_service.py::PRService::fetch_repo_content"
      ],
      "server/src/adapters/github_api.py::GitHubAPI::fetch_file_content": [
        "server/src/services/pr_service.py::PRService::fetch_repo_content"
      ],
      "server/src/adapters/google_oauth_api.py::GoogleAPIError": [
        "server/src/adapters/google_oauth_api.py::GoogleOAuthAPI::fetch_user_info"
      ],
      "server/src/adapters/google_oauth_api.py::GoogleOAuthAPI::__init__": [
        "server/src/server.py::Server::__init__"
      ],
      "server/src/adapters/google_oauth_api.py::GoogleOAuthAPI::generate_password": [
        "server/src/adapters/google_oauth_api.py::GoogleOAuthAPI::fetch_user_info"
      ],
      "server/src/adapters/google_oauth_api.py::GoogleOAuthAPI::fetch_user_info": [
        "server/src/services/oauth_service.py::OAuthService::google_oauth"
      ],
      "server/src/constants/__init__.py::get_github_pr_files_url": [
        "server/src/adapters/github_api.py::GitHubAPI::fetch_pr_files_diff"
      ],
      "server/src/constants/__init__.py::get_github_pr_url": [
        "server/src/adapters/github_api.py::GitHubAPI::fetch_pr"
      ],
      "server/src/constants/__init__.py::get_github_repo_content_for_branch": [
        "server/src/services/pr_service.py::PRService::fetch_repo_content"
      ],
      "server/src/controllers/auth_controller.py::AuthController::__init__": [
        "server/src/server.py::Server::__init__"
      ],
      "server/src/controllers/auth_controller.py::AuthController::register_routes": [
        "server/src/server.py::Server::register_routes"
      ],
      "server/src/controllers/oauth_controller.py::OAuthController::__init__": [
        "server/src/server.py::Server::__init__"
      ],
      "server/src/controllers/oauth_controller.py::OAuthController::register_routes": [
        "server/src/server.py::Server::register_routes"
      ],
      "server/src/controllers/pr_controller.py::PRController::__init__": [
        "server/src/server.py::Server::__init__"
      ],
      "server/src/controllers/pr_controller.py::PRController::register_routes": [
        "server/src/server.py::Server::register_routes"
      ],
      "server/src/main.py::main": [
        "server/src/main.py"
      ],
      "server/src/models/user.py::User": [
        "server/src/repositories/user_repo.py::UserRepo::create_user"
      ],
      "server/src/parsers/python_parser.py::PythonDiffParser::__init__": [
        "server/src/services/pr_service.py::PRService::__init__"
      ],
      "server/src/parsers/python_parser.py::PythonDiffParser::extract_added_code": [
        "server/src/parsers/python_parser.py::PythonDiffParser::parse_diff"
      ],
      "server/src/parsers/python_parser.py::PythonDiffParser::parse_diff": [
        "server/src/services/pr_service.py::PRService::get_pr_file_change_nodes"
      ],
      "server/src/parsers/python_parser.py::PythonDiffParser::get_text": [
        "server/src/parsers/python_parser.py::PythonDiffParser::traverse",
        "server/src/parsers/python_parser.py::PythonDiffParser::extract_imports"
      ],
      "server/src/parsers/python_parser.py::PythonDiffParser::extract_definitions": [
        "server/src/services/pr_service.py::PRService::fetch_repo_content"
      ],
      "server/src/parsers/python_parser.py::PythonDiffParser::extract_imports": [
        "server/src/services/pr_service.py::PRService::fetch_repo_content"
      ],
      "server/src/parsers/python_parser.py::PythonDiffParser::extract_dependency_info": [
        "server/src/services/pr_service.py::PRService::fetch_repo_content"
      ],
      "server/src/repositories/user_repo.py::UserRepo::__init__": [
        "server/src/services/auth_service.py::AuthService::register",
        "server/src/services/auth_service.py::AuthService::get_current_user",
        "server/src/services/auth_service.py::AuthService::login",
        "server/src/services/oauth_service.py::OAuthService::google_oauth"
      ],
      "server/src/repositories/user_repo.py::UserRepo::find_by_email": [
        "server/src/repositories/user_repo.py::UserRepo::exists_by_email"
      ],
      "server/src/server.py::Server::__init__": [
        "server/src/main.py"
      ],
      "server/src/server.py::Server::register_routes": [
        "server/src/server.py::Server::__init__"
      ],
      "server/src/services/auth_service.py::AuthError": [
        "server/src/services/auth_service.py::AuthService::register",
        "server/src/services/auth_service.py::AuthService::login"
      ],
      "server/src/services/auth_service.py::AuthService::__init__": [
        "server/src/server.py::Server::__init__"
      ],
      "server/src/services/auth_service.py::AuthService::hash_password": [
        "server/src/services/auth_service.py::AuthService::register"
      ],
      "server/src/services/auth_service.py::AuthService::verify_password": [
        "server/src/services/auth_service.py::AuthService::login"
      ],
      "server/src/services/auth_service.py::AuthService::login": [
        "server/src/controllers/auth_controller.py::AuthController::login"
      ],
      "server/src/services/auth_service.py::AuthService::register": [
        "server/src/controllers/auth_controller.py::AuthController::register"
      ],
      "server/src/services/auth_service.py::AuthService::get_current_user": [
        "server/src/controllers/auth_controller.py::AuthController::auth_middleware"
      ],
      "server/src/services/jwt_service.py::JWTService::__init__": [
        "server/src/server.py::Server::__init__"
      ],
      "server/src/services/jwt_service.py::JWTService::sign": [
        "server/src/services/auth_service.py::AuthService::register",
        "server/src/services/auth_service.py::AuthService::login",
        "server/src/services/oauth_service.py::OAuthService::google_oauth"
      ],
      "server/src/services/jwt_service.py::JWTService::verify": [
        "server/src/services/auth_service.py::AuthService::get_current_user"
      ],
      "server/src/services/oauth_service.py::OAuthService::__init__": [
        "server/src/server.py::Server::__init__"
      ],
      "server/src/services/oauth_service.py::OAuthService::google_oauth": [
        "server/src/controllers/oauth_controller.py::OAuthController::oauth_google"
      ],
      "server/src/services/pr_service.py::PRError": [
        "server/src/services/pr_service.py::PRService::fetch_repo_content"
      ],
      "server/src/services/pr_service.py::PRService::__init__": [
        "server/src/server.py::Server::__init__"
      ],
      "server/src/services/pr_service.py::PRService::get_pr_file_change_nodes": [
        "server/src/controllers/pr_controller.py::PRController::compute"
      ],
      "server/src/services/pr_service.py::PRService::get_all_affected": [
        "server/src/services/pr_service.py::PRService::get_all_affected",
        "server/src/services/pr_service.py::PRService::compute_blast_radius"
      ],
      "server/src/services/pr_service.py::PRService::get_depth": [
        "server/src/services/pr_service.py::PRService::get_depth",
        "server/src/services/pr_service.py::PRService::compute_blast_radius"
      ],
      "server/src/services/pr_service.py::PRService::get_layer": [
        "server/src/services/pr_service.py::PRService::compute_blast_radius"
      ],
      "server/src/services/pr_service.py::PRService::score": [
        "server/src/services/pr_service.py::PRService::compute_blast_radius"
      ],
      "server/src/services/pr_service.py::PRService::compute_blast_radius": [
        "server/src/controllers/pr_controller.py::PRController::compute"
      ],
      "server/src/services/pr_service.py::PRService::fetch_repo_content": [
        "server/src/controllers/pr_controller.py::PRController::compute"
      ]
    },
    "transitive": {
      "server/src/adapters/github_api.py::GitHubAPIError": [
        "server/src/adapters/github_api.py::GitHubAPI::fetch_pr_files_diff",
        "server/src/services/pr_service.py::PRService::get_pr_file_change_nodes",
        "server/src/adapters/github_api.py::GitHubAPI::fetch_file_content",
        "server/src/adapters/github_api.py::GitHubAPI::fetch_pr",
        "server/src/services/pr_service.py::PRService::fetch_repo_content",
        "server/src/controllers/pr_controller.py::PRController::compute",
        "server/src/adapters/github_api.py::GitHubAPI::fetch_repo_content"
      ],
      "server/src/adapters/github_api.py::GitHubAPIError::__init__": [],
      "server/src/adapters/github_api.py::GitHubAPI": [],
      "server/src/adapters/github_api.py::GitHubAPI::__init__": [
        "server/src/main.py",
        "server/src/server.py::Server::__init__"
      ],
      "server/src/adapters/github_api.py::GitHubAPI::_get_headers": [
        "server/src/adapters/github_api.py::GitHubAPI::fetch_pr_files_diff",
        "server/src/services/pr_service.py::PRService::get_pr_file_change_nodes",
        "server/src/adapters/github_api.py::GitHubAPI::fetch_file_content",
        "server/src/adapters/github_api.py::GitHubAPI::fetch_pr",
        "server/src/services/pr_service.py::PRService::fetch_repo_content",
        "server/src/controllers/pr_controller.py::PRController::compute",
        "server/src/adapters/github_api.py::GitHubAPI::fetch_repo_content"
      ],
      "server/src/adapters/github_api.py::GitHubAPI::fetch_pr_files_diff": [
        "server/src/controllers/pr_controller.py::PRController::compute",
        "server/src/services/pr_service.py::PRService::get_pr_file_change_nodes"
      ],
      "server/src/adapters/github_api.py::GitHubAPI::fetch_pr": [
        "server/src/controllers/pr_controller.py::PRController::compute",
        "server/src/services/pr_service.py::PRService::fetch_repo_content"
      ],
      "server/src/adapters/github_api.py::GitHubAPI::fetch_repo_content": [
        "server/src/services/pr_service.py::PRService::fetch_repo_content",
        "server/src/controllers/pr_controller.py::PRController::compute"
      ],
      "server/src/adapters/github_api.py::GitHubAPI::fetch_file_content": [
        "server/src/controllers/pr_controller.py::PRController::compute",
        "server/src/services/pr_service.py::PRService::fetch_repo_content"
      ],
      "server/src/adapters/google_oauth_api.py::GoogleAPIError": [
        "server/src/controllers/oauth_controller.py::OAuthController::oauth_google",
        "server/src/adapters/google_oauth_api.py::GoogleOAuthAPI::fetch_user_info",
        "server/src/services/oauth_service.py::OAuthService::google_oauth"
      ],
      "server/src/adapters/google_oauth_api.py::GoogleAPIError::__init__": [],
      "server/src/adapters/google_oauth_api.py::GoogleOAuthAPI": [],
      "server/src/adapters/google_oauth_api.py::GoogleOAuthAPI::__init__": [
        "server/src/main.py",
        "server/src/server.py::Server::__init__"
      ],
      "server/src/adapters/google_oauth_api.py::GoogleOAuthAPI::generate_password": [
        "server/src/adapters/google_oauth_api.py::GoogleOAuthAPI::fetch_user_info",
        "server/src/controllers/oauth_controller.py::OAuthController::oauth_google",
        "server/src/services/oauth_service.py::OAuthService::google_oauth"
      ],
      "server/src/adapters/google_oauth_api.py::GoogleOAuthAPI::fetch_user_info": [
        "server/src/controllers/oauth_controller.py::OAuthController::oauth_google",
        "server/src/services/oauth_service.py::OAuthService::google_oauth"
      ],
      "server/src/constants/__init__.py::get_github_pr_files_url": [
        "server/src/adapters/github_api.py::GitHubAPI::fetch_pr_files_diff",
        "server/src/controllers/pr_controller.py::PRController::compute",
        "server/src/services/pr_service.py::PRService::get_pr_file_change_nodes"
      ],
      "server/src/constants/__init__.py::get_github_pr_url": [
        "server/src/adapters/github_api.py::GitHubAPI::fetch_pr",
        "server/src/controllers/pr_controller.py::PRController::compute",
        "server/src/services/pr_service.py::PRService::fetch_repo_content"
      ],
      "server/src/constants/__init__.py::get_github_repo_content_for_branch": [
        "server/src/controllers/pr_controller.py::PRController::compute",
        "server/src/services/pr_service.py::PRService::fetch_repo_content"
      ],
      "server/src/controllers/auth_controller.py::LoginRequest": [],
      "server/src/controllers/auth_controller.py::RegisterRequest": [],
      "server/src/controllers/auth_controller.py::AuthController": [],
      "server/src/controllers/auth_controller.py::AuthController::__init__": [
        "server/src/main.py",
        "server/src/server.py::Server::__init__"
      ],
      "server/src/controllers/auth_controller.py::AuthController::register_routes": [
        "server/src/server.py::Server::register_routes",
        "server/src/server.py::Server::__init__",
        "server/src/main.py"
      ],
      "server/src/controllers/oauth_controller.py::OAuthController": [],
      "server/src/controllers/oauth_controller.py::OAuthController::__init__": [
        "server/src/main.py",
        "server/src/server.py::Server::__init__"
      ],
      "server/src/controllers/oauth_controller.py::OAuthController::register_routes": [
        "server/src/server.py::Server::register_routes",
        "server/src/server.py::Server::__init__",
        "server/src/main.py"
      ],
      "server/src/controllers/pr_controller.py::BlastRadiusRequest": [],
      "server/src/controllers/pr_controller.py::PRController": [],
      "server/src/controllers/pr_controller.py::PRController::__init__": [
        "server/src/main.py",
        "server/src/server.py::Server::__init__"
      ],
      "server/src/controllers/pr_controller.py::PRController::register_routes": [
        "server/src/server.py::Server::register_routes",
        "server/src/server.py::Server::__init__",
        "server/src/main.py"
      ],
      "server/src/helpers/db.py::get_db": [],
      "server/src/main.py::main": [
        "server/src/main.py"
      ],
      "server/src/models/user.py::User": [
        "server/src/repositories/user_repo.py::UserRepo::create_user"
      ],
      "server/src/parsers/python_parser.py::PythonDiffParser": [],
      "server/src/parsers/python_parser.py::PythonDiffParser::__init__": [
        "server/src/main.py",
        "server/src/server.py::Server::__init__",
        "server/src/services/pr_service.py::PRService::__init__"
      ],
      "server/src/parsers/python_parser.py::PythonDiffParser::extract_added_code": [
        "server/src/services/pr_service.py::PRService::get_pr_file_change_nodes",
        "server/src/controllers/pr_controller.py::PRController::compute",
        "server/src/parsers/python_parser.py::PythonDiffParser::parse_diff"
      ],
      "server/src/parsers/python_parser.py::PythonDiffParser::parse_diff": [
        "server/src/controllers/pr_controller.py::PRController::compute",
        "server/src/services/pr_service.py::PRService::get_pr_file_change_nodes"
      ],
      "server/src/parsers/python_parser.py::PythonDiffParser::get_text": [
        "server/src/parsers/python_parser.py::PythonDiffParser::extract_imports",
        "server/src/parsers/python_parser.py::PythonDiffParser::traverse",
        "server/src/services/pr_service.py::PRService::fetch_repo_content",
        "server/src/controllers/pr_controller.py::PRController::compute"
      ],
      "server/src/parsers/python_parser.py::PythonDiffParser::extract_definitions": [
        "server/src/controllers/pr_controller.py::PRController::compute",
        "server/src/services/pr_service.py::PRService::fetch_repo_content"
      ],
      "server/src/parsers/python_parser.py::PythonDiffParser::extract_imports": [
        "server/src/controllers/pr_controller.py::PRController::compute",
        "server/src/services/pr_service.py::PRService::fetch_repo_content"
      ],
      "server/src/parsers/python_parser.py::PythonDiffParser::extract_dependency_info": [
        "server/src/controllers/pr_controller.py::PRController::compute",
        "server/src/services/pr_service.py::PRService::fetch_repo_content"
      ],
      "server/src/repositories/user_repo.py::UserRepo": [],
      "server/src/repositories/user_repo.py::UserRepo::__init__": [
        "server/src/controllers/auth_controller.py::AuthController::login",
        "server/src/services/auth_service.py::AuthService::login",
        "server/src/services/oauth_service.py::OAuthService::google_oauth",
        "server/src/services/auth_service.py::AuthService::get_current_user",
        "server/src/services/auth_service.py::AuthService::register",
        "server/src/controllers/auth_controller.py::AuthController::auth_middleware",
        "server/src/controllers/auth_controller.py::AuthController::register",
        "server/src/controllers/oauth_controller.py::OAuthController::oauth_google"
      ],
      "server/src/repositories/user_repo.py::UserRepo::find_by_email": [
        "server/src/repositories/user_repo.py::UserRepo::exists_by_email"
      ],
      "server/src/repositories/user_repo.py::UserRepo::find_by_id": [],
      "server/src/repositories/user_repo.py::UserRepo::create_user": [],
      "server/src/repositories/user_repo.py::UserRepo::exists_by_email": [],
      "server/src/server.py::Server": [],
      "server/src/server.py::Server::__init__": [
        "server/src/main.py"
      ],
      "server/src/server.py::Server::register_routes": [
        "server/src/server.py::Server::__init__",
        "server/src/main.py"
      ],
      "server/src/services/auth_service.py::AuthError": [
        "server/src/controllers/auth_controller.py::AuthController::login",
        "server/src/services/auth_service.py::AuthService::login",
        "server/src/services/auth_service.py::AuthService::register",
        "server/src/controllers/auth_controller.py::AuthController::register"
      ],
      "server/src/services/auth_service.py::AuthError::__init__": [],
      "server/src/services/auth_service.py::AuthService": [],
      "server/src/services/auth_service.py::AuthService::__init__": [
        "server/src/server.py::Server::__init__",
        "server/src/main.py"
      ],
      "server/src/services/auth_service.py::AuthService::hash_password": [
        "server/src/services/auth_service.py::AuthService::register",
        "server/src/controllers/auth_controller.py::AuthController::register"
      ],
      "server/src/services/auth_service.py::AuthService::verify_password": [
        "server/src/services/auth_service.py::AuthService::login",
        "server/src/controllers/auth_controller.py::AuthController::login"
      ],
      "server/src/services/auth_service.py::AuthService::login": [
        "server/src/controllers/auth_controller.py::AuthController::login"
      ],
      "server/src/services/auth_service.py::AuthService::register": [
        "server/src/controllers/auth_controller.py::AuthController::register"
      ],
      "server/src/services/auth_service.py::AuthService::get_current_user": [
        "server/src/controllers/auth_controller.py::AuthController::auth_middleware"
      ],
      "server/src/services/jwt_service.py::JWTService": [],
      "server/src/services/jwt_service.py::JWTService::__init__": [
        "server/src/main.py",
        "server/src/server.py::Server::__init__"
      ],
      "server/src/services/jwt_service.py::JWTService::sign": [
        "server/src/controllers/auth_controller.py::AuthController::login",
        "server/src/services/auth_service.py::AuthService::login",
        "server/src/services/oauth_service.py::OAuthService::google_oauth",
        "server/src/services/auth_service.py::AuthService::register",
        "server/src/controllers/auth_controller.py::AuthController::register",
        "server/src/controllers/oauth_controller.py::OAuthController::oauth_google"
      ],
      "server/src/services/jwt_service.py::JWTService::verify": [
        "server/src/controllers/auth_controller.py::AuthController::auth_middleware",
        "server/src/services/auth_service.py::AuthService::get_current_user"
      ],
      "server/src/services/oauth_service.py::OAuthError": [],
      "server/src/services/oauth_service.py::OAuthError::__init__": [],
      "server/src/services/oauth_service.py::OAuthService": [],
      "server/src/services/oauth_service.py::OAuthService::__init__": [
        "server/src/main.py",
        "server/src/server.py::Server::__init__"
      ],
      "server/src/services/oauth_service.py::OAuthService::google_oauth": [
        "server/src/controllers/oauth_controller.py::OAuthController::oauth_google"
      ],
      "server/src/services/pr_service.py::PRError": [
        "server/src/services/pr_service.py::PRService::fetch_repo_content",
        "server/src/controllers/pr_controller.py::PRController::compute"
      ],
      "server/src/services/pr_service.py::PRError::__init__": [],
      "server/src/services/pr_service.py::PRService": [],
      "server/src/services/pr_service.py::PRService::__init__": [
        "server/src/main.py",
        "server/src/server.py::Server::__init__"
      ],
      "server/src/services/pr_service.py::PRService::get_pr_file_change_nodes": [
        "server/src/controllers/pr_controller.py::PRController::compute"
      ],
      "server/src/services/pr_service.py::PRService::get_all_affected": [
        "server/src/controllers/pr_controller.py::PRController::compute",
        "server/src/services/pr_service.py::PRService::compute_blast_radius"
      ],
      "server/src/services/pr_service.py::PRService::get_depth": [
        "server/src/controllers/pr_controller.py::PRController::compute",
        "server/src/services/pr_service.py::PRService::compute_blast_radius"
      ],
      "server/src/services/pr_service.py::PRService::get_layer": [
        "server/src/controllers/pr_controller.py::PRController::compute",
        "server/src/services/pr_service.py::PRService::compute_blast_radius"
      ],
      "server/src/services/pr_service.py::PRService::score": [
        "server/src/controllers/pr_controller.py::PRController::compute",
        "server/src/services/pr_service.py::PRService::compute_blast_radius"
      ],
      "server/src/services/pr_service.py::PRService::compute_blast_radius": [
        "server/src/controllers/pr_controller.py::PRController::compute"
      ],
      "server/src/services/pr_service.py::PRService::fetch_repo_content": [
        "server/src/controllers/pr_controller.py::PRController::compute"
      ]
    },
    "depths": {
      "server/src/adapters/github_api.py::GitHubAPIError": 3,
      "server/src/adapters/github_api.py::GitHubAPIError::__init__": 0,
      "server/src/adapters/github_api.py::GitHubAPI": 0,
      "server/src/adapters/github_api.py::GitHubAPI::__init__": 2,
      "server/src/adapters/github_api.py::GitHubAPI::_get_headers": 3,
      "server/src/adapters/github_api.py::GitHubAPI::fetch_pr_files_diff": 2,
      "server/src/adapters/github_api.py::GitHubAPI::fetch_pr": 2,
      "server/src/adapters/github_api.py::GitHubAPI::fetch_repo_content": 2,
      "server/src/adapters/github_api.py::GitHubAPI::fetch_file_content": 2,
      "server/src/adapters/google_oauth_api.py::GoogleAPIError": 3,
      "server/src/adapters/google_oauth_api.py::GoogleAPIError::__init__": 0,
      "server/src/adapters/google_oauth_api.py::GoogleOAuthAPI": 0,
      "server/src/adapters/google_oauth_api.py::GoogleOAuthAPI::__init__": 2,
      "server/src/adapters/google_oauth_api.py::GoogleOAuthAPI::generate_password": 3,
      "server/src/adapters/google_oauth_api.py::GoogleOAuthAPI::fetch_user_info": 2,
      "server/src/constants/__init__.py::get_github_pr_files_url": 3,
      "server/src/constants/__init__.py::get_github_pr_url": 3,
      "server/src/constants/__init__.py::get_github_repo_content_for_branch": 2,
      "server/src/controllers/auth_controller.py::LoginRequest": 0,
      "server/src/controllers/auth_controller.py::RegisterRequest": 0,
      "server/src/controllers/auth_controller.py::AuthController": 0,
      "server/src/controllers/auth_controller.py::AuthController::__init__": 2,
      "server/src/controllers/auth_controller.py::AuthController::register_routes": 3,
      "server/src/controllers/oauth_controller.py::OAuthController": 0,
      "server/src/controllers/oauth_controller.py::OAuthController::__init__": 2,
      "server/src/controllers/oauth_controller.py::OAuthController::register_routes": 3,
      "server/src/controllers/pr_controller.py::BlastRadiusRequest": 0,
      "server/src/controllers/pr_controller.py::PRController": 0,
      "server/src/controllers/pr_controller.py::PRController::__init__": 2,
      "server/src/controllers/pr_controller.py::PRController::register_routes": 3,
      "server/src/helpers/db.py::get_db": 0,
      "server/src/main.py::main": 1,
      "server/src/models/user.py::User": 1,
      "server/src/parsers/python_parser.py::PythonDiffParser": 0,
      "server/src/parsers/python_parser.py::PythonDiffParser::__init__": 3,
      "server/src/parsers/python_parser.py::PythonDiffParser::extract_added_code": 3,
      "server/src/parsers/python_parser.py::PythonDiffParser::parse_diff": 2,
      "server/src/parsers/python_parser.py::PythonDiffParser::get_text": 3,
      "server/src/parsers/python_parser.py::PythonDiffParser::extract_definitions": 2,
      "server/src/parsers/python_parser.py::PythonDiffParser::extract_imports": 2,
      "server/src/parsers/python_parser.py::PythonDiffParser::extract_dependency_info": 2,
      "server/src/repositories/user_repo.py::UserRepo": 0,
      "server/src/repositories/user_repo.py::UserRepo::__init__": 2,
      "server/src/repositories/user_repo.py::UserRepo::find_by_email": 1,
      "server/src/repositories/user_repo.py::UserRepo::find_by_id": 0,
      "server/src/repositories/user_repo.py::UserRepo::create_user": 0,
      "server/src/repositories/user_repo.py::UserRepo::exists_by_email": 0,
      "server/src/server.py::Server": 0,
      "server/src/server.py::Server::__init__": 1,
      "server/src/server.py::Server::register_routes": 2,
      "server/src/services/auth_service.py::AuthError": 2,
      "server/src/services/auth_service.py::AuthError::__init__": 0,
      "server/src/services/auth_service.py::AuthService": 0,
      "server/src/services/auth_service.py::AuthService::__init__": 2,
      "server/src/services/auth_service.py::AuthService::hash_password": 2,
      "server/src/services/auth_service.py::AuthService::verify_password": 2,
      "server/src/services/auth_service.py::AuthService::login": 1,
      "server/src/services/auth_service.py::AuthService::register": 1,
      "server/src/services/auth_service.py::AuthService::get_current_user": 1,
      "server/src/services/jwt_service.py::JWTService": 0,
      "server/src/services/jwt_service.py::JWTService::__init__": 2,
      "server/src/services/jwt_service.py::JWTService::sign": 2,
      "server/src/services/jwt_service.py::JWTService::verify": 2,
      "server/src/services/oauth_service.py::OAuthError": 0,
      "server/src/services/oauth_service.py::OAuthError::__init__": 0,
      "server/src/services/oauth_service.py::OAuthService": 0,
      "server/src/services/oauth_service.py::OAuthService::__init__": 2,
      "server/src/services/oauth_service.py::OAuthService::google_oauth": 1,
      "server/src/services/pr_service.py::PRError": 2,
      "server/src/services/pr_service.py::PRError::__init__": 0,
      "server/src/services/pr_service.py::PRService": 0,
      "server/src/services/pr_service.py::PRService::__init__": 2,
      "server/src/services/pr_service.py::PRService::get_pr_file_change_nodes": 1,
      "server/src/services/pr_service.py::PRService::get_all_affected": 2,
      "server/src/services/pr_service.py::PRService::get_depth": 2,
      "server/src/services/pr_service.py::PRService::get_layer": 2,
      "server/src/services/pr_service.py::PRService::score": 2,
      "server/src/services/pr_service.py::PRService::compute_blast_radius": 1,
      "server/src/services/pr_service.py::PRService::fetch_repo_content": 1
    },
    "layers_crossed": {
      "server/src/adapters/github_api.py::GitHubAPIError": [
        "controller",
        "adapter",
        "service"
      ],
      "server/src/adapters/github_api.py::GitHubAPIError::__init__": [],
      "server/src/adapters/github_api.py::GitHubAPI": [],
      "server/src/adapters/github_api.py::GitHubAPI::__init__": [
        "other"
      ],
      "server/src/adapters/github_api.py::GitHubAPI::_get_headers": [
        "controller",
        "adapter",
        "service"
      ],
      "server/src/adapters/github_api.py::GitHubAPI::fetch_pr_files_diff": [
        "controller",
        "service"
      ],
      "server/src/adapters/github_api.py::GitHubAPI::fetch_pr": [
        "controller",
        "service"
      ],
      "server/src/adapters/github_api.py::GitHubAPI::fetch_repo_content": [
        "controller",
        "service"
      ],
      "server/src/adapters/github_api.py::GitHubAPI::fetch_file_content": [
        "controller",
        "service"
      ],
      "server/src/adapters/google_oauth_api.py::GoogleAPIError": [
        "controller",
        "adapter",
        "service"
      ],
      "server/src/adapters/google_oauth_api.py::GoogleAPIError::__init__": [],
      "server/src/adapters/google_oauth_api.py::GoogleOAuthAPI": [],
      "server/src/adapters/google_oauth_api.py::GoogleOAuthAPI::__init__": [
        "other"
      ],
      "server/src/adapters/google_oauth_api.py::GoogleOAuthAPI::generate_password": [
        "controller",
        "adapter",
        "service"
      ],
      "server/src/adapters/google_oauth_api.py::GoogleOAuthAPI::fetch_user_info": [
        "controller",
        "service"
      ],
      "server/src/constants/__init__.py::get_github_pr_files_url": [
        "controller",
        "adapter",
        "service"
      ],
      "server/src/constants/__init__.py::get_github_pr_url": [
        "controller",
        "adapter",
        "service"
      ],
      "server/src/constants/__init__.py::get_github_repo_content_for_branch": [
        "controller",
        "service"
      ],
      "server/src/controllers/auth_controller.py::LoginRequest": [],
      "server/src/controllers/auth_controller.py::RegisterRequest": [],
      "server/src/controllers/auth_controller.py::AuthController": [],
      "server/src/controllers/auth_controller.py::AuthController::__init__": [
        "other"
      ],
      "server/src/controllers/auth_controller.py::AuthController::register_routes": [
        "other"
      ],
      "server/src/controllers/oauth_controller.py::OAuthController": [],
      "server/src/controllers/oauth_controller.py::OAuthController::__init__": [
        "other"
      ],
      "server/src/controllers/oauth_controller.py::OAuthController::register_routes": [
        "other"
      ],
      "server/src/controllers/pr_controller.py::BlastRadiusRequest": [],
      "server/src/controllers/pr_controller.py::PRController": [],
      "server/src/controllers/pr_controller.py::PRController::__init__": [
        "other"
      ],
      "server/src/controllers/pr_controller.py::PRController::register_routes": [
        "other"
      ],
      "server/src/helpers/db.py::get_db": [],
      "server/src/main.py::main": [
        "other"
      ],
      "server/src/models/user.py::User": [
        "repository"
      ],
      "server/src/parsers/python_parser.py::PythonDiffParser": [],
      "server/src/parsers/python_parser.py::PythonDiffParser::__init__": [
        "other",
        "service"
      ],
      "server/src/parsers/python_parser.py::PythonDiffParser::extract_added_code": [
        "controller",
        "other",
        "service"
      ],
      "server/src/parsers/python_parser.py::PythonDiffParser::parse_diff": [
        "controller",
        "service"
      ],
      "server/src/parsers/python_parser.py::PythonDiffParser::get_text": [
        "other",
        "controller",
        "service"
      ],
      "server/src/parsers/python_parser.py::PythonDiffParser::extract_definitions": [
        "controller",
        "service"
      ],
      "server/src/parsers/python_parser.py::PythonDiffParser::extract_imports": [
        "controller",
        "service"
      ],
      "server/src/parsers/python_parser.py::PythonDiffParser::extract_dependency_info": [
        "controller",
        "service"
      ],
      "server/src/repositories/user_repo.py::UserRepo": [],
      "server/src/repositories/user_repo.py::UserRepo::__init__": [
        "controller",
        "service"
      ],
      "server/src/repositories/user_repo.py::UserRepo::find_by_email": [
        "repository"
      ],
      "server/src/repositories/user_repo.py::UserRepo::find_by_id": [],
      "server/src/repositories/user_repo.py::UserRepo::create_user": [],
      "server/src/repositories/user_repo.py::UserRepo::exists_by_email": [],
      "server/src/server.py::Server": [],
      "server/src/server.py::Server::__init__": [
        "other"
      ],
      "server/src/server.py::Server::register_routes": [
        "other"
      ],
      "server/src/services/auth_service.py::AuthError": [
        "controller",
        "service"
      ],
      "server/src/services/auth_service.py::AuthError::__init__": [],
      "server/src/services/auth_service.py::AuthService": [],
      "server/src/services/auth_service.py::AuthService::__init__": [
        "other"
      ],
      "server/src/services/auth_service.py::AuthService::hash_password": [
        "controller",
        "service"
      ],
      "server/src/services/auth_service.py::AuthService::verify_password": [
        "controller",
        "service"
      ],
      "server/src/services/auth_service.py::AuthService::login": [
        "controller"
      ],
      "server/src/services/auth_service.py::AuthService::register": [
        "controller"
      ],
      "server/src/services/auth_service.py::AuthService::get_current_user": [
        "controller"
      ],
      "server/src/services/jwt_service.py::JWTService": [],
      "server/src/services/jwt_service.py::JWTService::__init__": [
        "other"
      ],
      "server/src/services/jwt_service.py::JWTService::sign": [
        "controller",
        "service"
      ],
      "server/src/services/jwt_service.py::JWTService::verify": [
        "controller",
        "service"
      ],
      "server/src/services/oauth_service.py::OAuthError": [],
      "server/src/services/oauth_service.py::OAuthError::__init__": [],
      "server/src/services/oauth_service.py::OAuthService": [],
      "server/src/services/oauth_service.py::OAuthService::__init__": [
        "other"
      ],
      "server/src/services/oauth_service.py::OAuthService::google_oauth": [
        "controller"
      ],
      "server/src/services/pr_service.py::PRError": [
        "controller",
        "service"
      ],
      "server/src/services/pr_service.py::PRError::__init__": [],
      "server/src/services/pr_service.py::PRService": [],
      "server/src/services/pr_service.py::PRService::__init__": [
        "other"
      ],
      "server/src/services/pr_service.py::PRService::get_pr_file_change_nodes": [
        "controller"
      ],
      "server/src/services/pr_service.py::PRService::get_all_affected": [
        "controller",
        "service"
      ],
      "server/src/services/pr_service.py::PRService::get_depth": [
        "controller",
        "service"
      ],
      "server/src/services/pr_service.py::PRService::get_layer": [
        "controller",
        "service"
      ],
      "server/src/services/pr_service.py::PRService::score": [
        "controller",
        "service"
      ],
      "server/src/services/pr_service.py::PRService::compute_blast_radius": [
        "controller"
      ],
      "server/src/services/pr_service.py::PRService::fetch_repo_content": [
        "controller"
      ]
    },
    "risk_scores": {
      "server/src/adapters/github_api.py::GitHubAPIError": "CRITICAL",
      "server/src/adapters/github_api.py::GitHubAPIError::__init__": "LOW",
      "server/src/adapters/github_api.py::GitHubAPI": "LOW",
      "server/src/adapters/github_api.py::GitHubAPI::__init__": "HIGH",
      "server/src/adapters/github_api.py::GitHubAPI::_get_headers": "CRITICAL",
      "server/src/adapters/github_api.py::GitHubAPI::fetch_pr_files_diff": "HIGH",
      "server/src/adapters/github_api.py::GitHubAPI::fetch_pr": "HIGH",
      "server/src/adapters/github_api.py::GitHubAPI::fetch_repo_content": "HIGH",
      "server/src/adapters/github_api.py::GitHubAPI::fetch_file_content": "HIGH",
      "server/src/adapters/google_oauth_api.py::GoogleAPIError": "CRITICAL",
      "server/src/adapters/google_oauth_api.py::GoogleAPIError::__init__": "LOW",
      "server/src/adapters/google_oauth_api.py::GoogleOAuthAPI": "LOW",
      "server/src/adapters/google_oauth_api.py::GoogleOAuthAPI::__init__": "HIGH",
      "server/src/adapters/google_oauth_api.py::GoogleOAuthAPI::generate_password": "CRITICAL",
      "server/src/adapters/google_oauth_api.py::GoogleOAuthAPI::fetch_user_info": "HIGH",
      "server/src/constants/__init__.py::get_github_pr_files_url": "CRITICAL",
      "server/src/constants/__init__.py::get_github_pr_url": "CRITICAL",
      "server/src/constants/__init__.py::get_github_repo_content_for_branch": "HIGH",
      "server/src/controllers/auth_controller.py::LoginRequest": "LOW",
      "server/src/controllers/auth_controller.py::RegisterRequest": "LOW",
      "server/src/controllers/auth_controller.py::AuthController": "LOW",
      "server/src/controllers/auth_controller.py::AuthController::__init__": "HIGH",
      "server/src/controllers/auth_controller.py::AuthController::register_routes": "CRITICAL",
      "server/src/controllers/oauth_controller.py::OAuthController": "LOW",
      "server/src/controllers/oauth_controller.py::OAuthController::__init__": "HIGH",
      "server/src/controllers/oauth_controller.py::OAuthController::register_routes": "CRITICAL",
      "server/src/controllers/pr_controller.py::BlastRadiusRequest": "LOW",
      "server/src/controllers/pr_controller.py::PRController": "LOW",
      "server/src/controllers/pr_controller.py::PRController::__init__": "HIGH",
      "server/src/controllers/pr_controller.py::PRController::register_routes": "CRITICAL",
      "server/src/helpers/db.py::get_db": "LOW",
      "server/src/main.py::main": "MEDIUM",
      "server/src/models/user.py::User": "MEDIUM",
      "server/src/parsers/python_parser.py::PythonDiffParser": "LOW",
      "server/src/parsers/python_parser.py::PythonDiffParser::__init__": "CRITICAL",
      "server/src/parsers/python_parser.py::PythonDiffParser::extract_added_code": "CRITICAL",
      "server/src/parsers/python_parser.py::PythonDiffParser::parse_diff": "HIGH",
      "server/src/parsers/python_parser.py::PythonDiffParser::get_text": "CRITICAL",
      "server/src/parsers/python_parser.py::PythonDiffParser::extract_definitions": "HIGH",
      "server/src/parsers/python_parser.py::PythonDiffParser::extract_imports": "HIGH",
      "server/src/parsers/python_parser.py::PythonDiffParser::extract_dependency_info": "HIGH",
      "server/src/repositories/user_repo.py::UserRepo": "LOW",
      "server/src/repositories/user_repo.py::UserRepo::__init__": "CRITICAL",
      "server/src/repositories/user_repo.py::UserRepo::find_by_email": "MEDIUM",
      "server/src/repositories/user_repo.py::UserRepo::find_by_id": "LOW",
      "server/src/repositories/user_repo.py::UserRepo::create_user": "LOW",
      "server/src/repositories/user_repo.py::UserRepo::exists_by_email": "LOW",
      "server/src/server.py::Server": "LOW",
      "server/src/server.py::Server::__init__": "MEDIUM",
      "server/src/server.py::Server::register_routes": "HIGH",
      "server/src/services/auth_service.py::AuthError": "HIGH",
      "server/src/services/auth_service.py::AuthError::__init__": "LOW",
      "server/src/services/auth_service.py::AuthService": "LOW",
      "server/src/services/auth_service.py::AuthService::__init__": "HIGH",
      "server/src/services/auth_service.py::AuthService::hash_password": "HIGH",
      "server/src/services/auth_service.py::AuthService::verify_password": "HIGH",
      "server/src/services/auth_service.py::AuthService::login": "MEDIUM",
      "server/src/services/auth_service.py::AuthService::register": "MEDIUM",
      "server/src/services/auth_service.py::AuthService::get_current_user": "MEDIUM",
      "server/src/services/jwt_service.py::JWTService": "LOW",
      "server/src/services/jwt_service.py::JWTService::__init__": "HIGH",
      "server/src/services/jwt_service.py::JWTService::sign": "CRITICAL",
      "server/src/services/jwt_service.py::JWTService::verify": "HIGH",
      "server/src/services/oauth_service.py::OAuthError": "LOW",
      "server/src/services/oauth_service.py::OAuthError::__init__": "LOW",
      "server/src/services/oauth_service.py::OAuthService": "LOW",
      "server/src/services/oauth_service.py::OAuthService::__init__": "HIGH",
      "server/src/services/oauth_service.py::OAuthService::google_oauth": "MEDIUM",
      "server/src/services/pr_service.py::PRError": "HIGH",
      "server/src/services/pr_service.py::PRError::__init__": "LOW",
      "server/src/services/pr_service.py::PRService": "LOW",
      "server/src/services/pr_service.py::PRService::__init__": "HIGH",
      "server/src/services/pr_service.py::PRService::get_pr_file_change_nodes": "MEDIUM",
      "server/src/services/pr_service.py::PRService::get_all_affected": "HIGH",
      "server/src/services/pr_service.py::PRService::get_depth": "HIGH",
      "server/src/services/pr_service.py::PRService::get_layer": "HIGH",
      "server/src/services/pr_service.py::PRService::score": "HIGH",
      "server/src/services/pr_service.py::PRService::compute_blast_radius": "MEDIUM",
      "server/src/services/pr_service.py::PRService::fetch_repo_content": "MEDIUM"
    },
    "overall_risk": "CRITICAL"
  },
  "llm_payload": {
    "changed_symbols": [
      "server/src/adapters/google_oauth_api.py::GoogleAPIError",
      "server/src/adapters/google_oauth_api.py::GoogleOAuthAPI::generate_password",
      "server/src/constants/__init__.py::get_github_pr_files_url",
      "server/src/constants/__init__.py::get_github_pr_url",
      "server/src/controllers/auth_controller.py::AuthController::register_routes",
      "server/src/controllers/oauth_controller.py::OAuthController::register_routes",
      "server/src/controllers/pr_controller.py::PRController::register_routes",
      "server/src/parsers/python_parser.py::PythonDiffParser::__init__",
      "server/src/parsers/python_parser.py::PythonDiffParser::extract_added_code",
      "server/src/parsers/python_parser.py::PythonDiffParser::get_text"
    ],
    "transitive": {
      "server/src/adapters/google_oauth_api.py::GoogleAPIError": [
        "server/src/controllers/oauth_controller.py::OAuthController::oauth_google",
        "server/src/adapters/google_oauth_api.py::GoogleOAuthAPI::fetch_user_info",
        "server/src/services/oauth_service.py::OAuthService::google_oauth"
      ],
      "server/src/adapters/google_oauth_api.py::GoogleOAuthAPI::generate_password": [
        "server/src/adapters/google_oauth_api.py::GoogleOAuthAPI::fetch_user_info",
        "server/src/controllers/oauth_controller.py::OAuthController::oauth_google",
        "server/src/services/oauth_service.py::OAuthService::google_oauth"
      ],
      "server/src/constants/__init__.py::get_github_pr_files_url": [
        "server/src/adapters/github_api.py::GitHubAPI::fetch_pr_files_diff",
        "server/src/controllers/pr_controller.py::PRController::compute",
        "server/src/services/pr_service.py::PRService::get_pr_file_change_nodes"
      ],
      "server/src/constants/__init__.py::get_github_pr_url": [
        "server/src/adapters/github_api.py::GitHubAPI::fetch_pr",
        "server/src/controllers/pr_controller.py::PRController::compute",
        "server/src/services/pr_service.py::PRService::fetch_repo_content"
      ],
      "server/src/controllers/auth_controller.py::AuthController::register_routes": [
        "server/src/server.py::Server::register_routes",
        "server/src/server.py::Server::__init__",
        "server/src/main.py"
      ],
      "server/src/controllers/oauth_controller.py::OAuthController::register_routes": [
        "server/src/server.py::Server::register_routes",
        "server/src/server.py::Server::__init__",
        "server/src/main.py"
      ],
      "server/src/controllers/pr_controller.py::PRController::register_routes": [
        "server/src/server.py::Server::register_routes",
        "server/src/server.py::Server::__init__",
        "server/src/main.py"
      ],
      "server/src/parsers/python_parser.py::PythonDiffParser::__init__": [
        "server/src/main.py",
        "server/src/server.py::Server::__init__",
        "server/src/services/pr_service.py::PRService::__init__"
      ],
      "server/src/parsers/python_parser.py::PythonDiffParser::extract_added_code": [
        "server/src/services/pr_service.py::PRService::get_pr_file_change_nodes",
        "server/src/controllers/pr_controller.py::PRController::compute",
        "server/src/parsers/python_parser.py::PythonDiffParser::parse_diff"
      ],
      "server/src/parsers/python_parser.py::PythonDiffParser::get_text": [
        "server/src/parsers/python_parser.py::PythonDiffParser::extract_imports",
        "server/src/parsers/python_parser.py::PythonDiffParser::traverse",
        "server/src/services/pr_service.py::PRService::fetch_repo_content",
        "server/src/controllers/pr_controller.py::PRController::compute"
      ]
    },
    "depths": {
      "server/src/adapters/google_oauth_api.py::GoogleAPIError": 3,
      "server/src/adapters/google_oauth_api.py::GoogleOAuthAPI::generate_password": 3,
      "server/src/constants/__init__.py::get_github_pr_files_url": 3,
      "server/src/constants/__init__.py::get_github_pr_url": 3,
      "server/src/controllers/auth_controller.py::AuthController::register_routes": 3,
      "server/src/controllers/oauth_controller.py::OAuthController::register_routes": 3,
      "server/src/controllers/pr_controller.py::PRController::register_routes": 3,
      "server/src/parsers/python_parser.py::PythonDiffParser::__init__": 3,
      "server/src/parsers/python_parser.py::PythonDiffParser::extract_added_code": 3,
      "server/src/parsers/python_parser.py::PythonDiffParser::get_text": 3
    },
    "risk_scores": {
      "server/src/adapters/google_oauth_api.py::GoogleAPIError": "CRITICAL",
      "server/src/adapters/google_oauth_api.py::GoogleOAuthAPI::generate_password": "CRITICAL",
      "server/src/constants/__init__.py::get_github_pr_files_url": "CRITICAL",
      "server/src/constants/__init__.py::get_github_pr_url": "CRITICAL",
      "server/src/controllers/auth_controller.py::AuthController::register_routes": "CRITICAL",
      "server/src/controllers/oauth_controller.py::OAuthController::register_routes": "CRITICAL",
      "server/src/controllers/pr_controller.py::PRController::register_routes": "CRITICAL",
      "server/src/parsers/python_parser.py::PythonDiffParser::__init__": "CRITICAL",
      "server/src/parsers/python_parser.py::PythonDiffParser::extract_added_code": "CRITICAL",
      "server/src/parsers/python_parser.py::PythonDiffParser::get_text": "CRITICAL"
    },
    "overall_risk": "CRITICAL"
  }
}