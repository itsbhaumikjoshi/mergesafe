# MergeSafe

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Backend](https://img.shields.io/badge/backend-FastAPI-green)
![Frontend](https://img.shields.io/badge/frontend-React%20%2B%20TypeScript-blue)
![Status](https://img.shields.io/badge/status-active-lightgrey)

MergeSafe is a side project that analyzes pull requests and estimates their potential impact on a codebase. Instead of only looking at file diffs, it builds a dependency graph of the repository and computes how far a change can propagate.

The goal is simple: provide a clearer view of **what a PR might affect**, and surface a small set of high-impact areas with brief AI-assisted recommendations.

---

## 🧠 Overview

MergeSafe works in a pipeline:

1. Accept a pull request
2. Extract changed functions/classes
3. Build a repository-level dependency graph
4. Traverse the graph to compute impact (blast radius)
5. Rank the most critical affected nodes
6. Generate a concise report using AI

---

## ⚙️ How It Works

### 1. Authentication

* Users sign in using **Email & Password** or **Google OAuth**
* JWT is used for session handling
* PostgreSQL is used only for storing user data

---

### 2. Pull Request Processing

* User provides a PR (must be open and owned by any user)
* The system fetches PR diffs via the GitHub API
* Changes are mapped into normalized nodes:

```
{file_path}::{class}::{method}
{file_path}::{class}
{file_path}::{function}
```

---

### 3. Repository Graph Construction

* The repository is traversed using BFS
* Code is parsed using Tree-sitter
* A dependency graph is built:

**Nodes**

* Functions
* Methods
* Classes

**Edges**

* Function/method calls
* Usage relationships

External libraries (pip-installed modules) are ignored to reduce noise.

---

### 4. Blast Radius Computation

* Starting from PR diff nodes
* DFS traversal is used to find all reachable nodes
* Depth of propagation is tracked

---

### 5. Critical Node Selection

* Nodes are ranked based on:

  * Number of dependents (fan-out)
  * Frequency of usage
* A heap is used to extract the top 10 most impactful nodes

---

### 6. AI Report Generation

* The filtered results are sent to the Groq API
* A structured report is generated:

  * Summary of impact
  * Key affected areas
  * Basic recommendations

---

### 7. Frontend Rendering

* Displays:

  * Impacted nodes
  * Graph-based insights
  * AI-generated report

---

## 🧰 Tech Stack

### Backend

* Python + FastAPI
* Tree-sitter (code parsing)
* PostgreSQL (user storage)
* JWT authentication

### Frontend

* TypeScript
* React

### External APIs

* Google OAuth (login / register)
* GitHub API (PR + repo data)
* Groq (report generation)

---

## 📡 API Documentation

Once the backend is running in development, interactive API docs are available at:

```
http://localhost:8000/docs
```

(Generated automatically by FastAPI via Swagger UI)

---

## 📁 Project Structure

```
mergesafe/
│
├── server/
│   ├── src/
│   │   ├── adapters/         # API Calls
│   │   ├── constants/        # Const vars
│   │   ├── controllers/      # Routes
│   │   ├── helpers/          # Helper funcs
│   │   ├── mock/             # Mock data for test accounts
│   │   ├── models/           # DB models (users)
│   │   ├── parsers/          # Tree-sitter integration
│   │   ├── repositories/     # Model repos
│   │   ├── services/         # Core logic (PR, graph, analysis)
│   │   └── main.py           # FastAPI entry point
│   │   └── server.py
│   │
│   ├── .env.example
│   ├── requirements.txt
│   └── Dockerfile
│
├── client/
│   ├── src/
│   │   ├── adapters/         # API calls
│   │   ├── components/       # UI components
│   │   ├── context/          # Contexts
│   │   ├── helpers/          # Helper funcs
│   │   ├── styles/           # styles
│   │   └── App.tsx
│   │   └── main.tsx
│   │
│   ├── package.json
│   ├── .env.example
│   └── vite.config.ts
│
└── README.md
```

---

## 🚀 Getting Started

### 1. Clone the repository

```
git clone https://github.com/itsbhaumikjoshi/mergesafe.git
cd mergesafe
```

---

### 2. Backend Setup

```
cd server
pip install -r requirements.txt
load the .env as per .env.example
uvicorn app.main:app --reload
```

---

### 3. Frontend Setup

```
cd frontend
npm install
load the .env as per .env.example
npm run dev
```

---

### 4. Environment Variables

Create a `.env` file:

Server
```
PORT=
HOSt=
PROD=
DATABASE_URL=
JWT_SECRET=
FRONTEND_URL=
GEN_AI_API_KEY=
GITHUB_API_TOKEN=
GOOGLE_CLIENT_ID=
GOOGLE_CLIENT_SECRET=
GOOGLE_REDIRECT_URI=
```

Client
```
VITE_API_BASE_URL=
VITE_GOOGLE_CLIENT_ID=
VITE_GOOGLE_REDIRECT_URI=
VITE_TEST_EMAIL=
VITE_TEST_PASSWORD=
```

---

## 📌 Current Limitations

* Supports Python repository files only
* Static analysis may miss dynamic behavior (common in Python)
* Full repository traversal can be slow for large codebases
* No persistent graph caching yet

---

## 🚧 Possible Improvements

* Incremental graph updates instead of full traversal
* Multi-language support via Tree-sitter
* More refined scoring for impact ranking
* Better handling of refactors and renames
* Graph storage for reuse across PRs

---

## 🧾 Summary

MergeSafe is a lightweight attempt at understanding PR impact using static analysis and graph traversal. It focuses on surfacing a small, useful subset of affected areas rather than providing exhaustive analysis.
