# MCP AI FastAPI + LangChain Learning Journal

This journal documents my 30-day journey to gain production-level expertise in:
- **FastAPI** (async APIs, validation, testing, deployment)
- **LangChain** (retrievers, agents, LangGraph, tools)
- **MCP Agentic Framework** (tool servers, orchestration, observability)

---

## Day 1 — FastAPI Setup & /health Endpoint

### 🎯 Goal
- Learn to set up a FastAPI project with proper structure.
- Implement a `/health` endpoint with realistic production fields.
- Write automated async tests to validate behavior.

### 🛠 Steps Completed
1. Created project structure with `app/`, `routes/`, and `schemas/` folders.
2. Defined `HealthResponse` Pydantic schema with:
   - `version: str`
   - `timestamp: datetime` (UTC-aware)
   - `uptime: float`
3. Created `health_check` route using `APIRouter` and included it in `main.py`.
4. Stored app start time in `app.state.start_time` for uptime calculation.
5. Ran locally using `uvicorn` and verified endpoint behavior.

### ✅ Achievements
- Avoided “frozen timestamp” bug by generating `datetime.now()` inside the route.
- Used `app.state` to store global state without circular imports.
- Successfully wrote async tests using:
  - `httpx.AsyncClient` + `ASGITransport`
  - Status code and schema validation
  - Timestamp correctness (UTC format, changes per request)
  - Uptime correctness (float, positive, increases over time)

### 💡 Key Learnings
- **Pydantic models** define clear, validated response shapes.
- **APIRouter** helps modularize routes for larger apps.
- **app.state** is a safe place for shared runtime state.
- **ASGITransport** allows in-memory testing without spinning up a server.
- Always test **time-dependent fields** for change and correctness.

---


## Day 2 — Routing & Dependency Injection (DI)

### 🎯 Goal
- Learn to structure multiple routers cleanly.
- Use FastAPI dependency injection (`Depends`) to provide data to endpoints.
- Centralize app configuration with a `Settings` object.
- Override dependencies in tests to simulate different scenarios.

### 🛠 Steps Completed
1. Created a new `/config` endpoint in its own `config.py` router.
2. Defined a `ConfigResponse` schema with:
   - `app_name: str`
   - `version: str`
   - `debug: bool`
3. Implemented `get_config()` as a dependency and injected it into the route using `Depends`.
4. Learned how to override dependencies in tests via `app.dependency_overrides`.
5. Created a central `Settings` model (`app/core/settings.py`) using Pydantic.
6. Stored a `Settings` instance in `app.state` at startup.
7. Updated `/config` to pull data from `Settings` via `get_settings` dependency.

### ✅ Achievements
- Modularized routes: `/api/v1/health`, `/api/v1/server-info`, `/api/v1/config`.
- Made configuration testable and override-friendly without changing route code.
- Validated DI chain with tests at both `get_config` and `get_settings` levels.

### 💡 Key Learnings
- **`Depends`** injects dependencies automatically and keeps routes clean.
- Centralizing config in `app.state` prevents hardcoding and supports test overrides.
- Dependency overrides are powerful for simulating different runtime conditions.
- Router tags and summaries improve API docs.
- Prefix versioning (`/api/v1`) makes future upgrades easier.

---

## Day 3 — Pydantic v2 Deep Dive  

### 🎯 Goal  
Understand how to validate, serialize, and document request/response data with Pydantic v2 inside FastAPI.  

### 🛠 Steps Completed  
- Created `UserCreationSchema` using Pydantic’s `Field`, `EmailStr`, and `default_factory`.  
- Explored schema-driven request bodies (`user: UserCreationSchema`) vs plain params.  
- Wrote tests ensuring constraints like `min_length` on username and email format validation.  
- Learned how Swagger/OpenAPI auto-updates based on schema definitions.  
- Practiced quiz-style validation: identifying when query params, path params, or request body is expected.  

### ✅ Achievements  
- Endpoints now automatically validate inputs (username length, email format, timestamps).  
- Swagger UI body editor became editable after binding schema → strong link between **request body** and **Pydantic models**.  
- All tests passed for `/user` endpoint, verifying schema correctness.  

### 💡 Key Learnings  
- **Schema = Contract**: When schema is bound to a POST body, Swagger exposes the JSON editor. Without it, only query/path params appear.  
- **Validation is declarative**: No need for manual checks — Pydantic enforces rules like `min_length=3` or valid email format.  
- **Default factories** (like `datetime.now(timezone.utc)`) make models dynamic at runtime.  
- **Tests confirm schema guarantees** — e.g., a failing username `"ab"` proves validation works.  

---

## Day 4 — Async I/O & Background Tasks  

### 🎯 Goal  
Learn to handle external HTTP calls asynchronously, mock dependencies cleanly in tests, and explore background execution patterns.  

### 🛠 Steps Completed  
- Integrated `httpx.AsyncClient` with FastAPI dependencies.  
- Created `/external-httpbin` endpoint fetching data from `https://httpbin.org/get`.  
- Modeled the response in `HttpBinResponse` (`url`, `origin`, `user_agent`, `fetched_at`).  
- Wrote fake clients (`FakeClient`, `FakeResp`) to override `get_http_client` in tests.  
- Ensured dependency overrides replaced the whole client cleanly without patching internals.  

### ✅ Achievements  
- Tests for `/external-httpbin` pass using **fake dependencies** instead of live HTTP calls.  
- Learned how to override dependencies in `app.dependency_overrides` for isolated testing.  
- Practiced cleanup: `app.dependency_overrides.clear()` to avoid cross-test leaks.  
- Observed async flow: `await client.get()` inside route logic, with safe `.aclose()`.  

### 💡 Key Learnings  
- **Async I/O**: External calls should be `await`ed to avoid blocking the event loop.  
- **Dependency override > patching**: Overriding keeps tests aligned with FastAPI’s design, while patching internals like `httpx.AsyncClient.get` is brittle.  
- **Schema-first response models** give a clear contract for what endpoints must return.  
- **Fake clients are lightweight**: build small classes (`json()`, `status_code`) to mimic responses and test logic without real network calls.  
- **Dependency Injection** ensures route logic can be tested in isolation — scaling better for bigger projects.  


## Day 5 — Testing & Coverage
...

## Day 6 — Mini-Project: Todo API
...

## Day 7 — Deploy & Logging
...

## Day 8 — LangChain Setup & First LLM Call
...

## Day 9 — PromptTemplates & LCEL
...

## Day 10 — Chains
...

## Day 11 — Data Loaders & Splitters
...

## Day 12 — Vector Stores
...

## Day 13 — RetrievalQA
...

## Day 14 — Deploy RAG API
...

## Day 15 — Agents: Tool Creation
...

## Day 16 — Memory
...

## Day 17 — LangGraph Basics
...

## Day 18 — Multi-step Agents
...

## Day 19 — Streaming Responses
...

## Day 20 — Agent with 3 Tools
...

## Day 21 — Eval with LangSmith
...

## Day 22 — MCP Concepts
...

## Day 23 — First MCP Tool Server
...

## Day 24 — LangChain + MCP Tool
...

## Day 25 — Auth
...

## Day 26 — Observability
...

## Day 27 — Deploy to AWS ECS
...

## Day 28 — Load Test & Polish
...

## Day 29 — Final Agent Demo Build
...

## Day 30 — Retrospective & Next Steps
...
