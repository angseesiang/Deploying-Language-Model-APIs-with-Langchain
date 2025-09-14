from fastapi import FastAPI
from fastapi.responses import RedirectResponse, Response
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from langserve import add_routes
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
# from langchain_ollama import OllamaLLM  # optional

import os
import uvicorn
import importlib

# ---- TEMP FIX: force-rebuild LangServe Pydantic models for OpenAPI ----
try:
    from pydantic import BaseModel
    from langserve import validation as _ls_validation
    for _name, _obj in vars(_ls_validation).items():
        if isinstance(_obj, type) and issubclass(_obj, BaseModel):
            try:
                _obj.model_rebuild(force=True)
            except Exception:
                pass
except Exception:
    pass
# ----------------------------------------------------------------------

# Load env
load_dotenv()
if not os.getenv("OPENAI_API_KEY"):
    raise RuntimeError("OPENAI_API_KEY not set. Put it in .env (OPENAI_API_KEY=sk-...) or export it.")

# App
app = FastAPI(
    title="LangChain Server",
    version="1.0.0",
    description="FastAPI + LangServe example exposing OpenAI (and optional Ollama) routes",
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # tighten in prod
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Static (optional)
if os.path.isdir("static"):
    app.mount("/static", StaticFiles(directory="static"), name="static")

# Friendly root + favicon
@app.get("/", include_in_schema=False)
def root():
    return RedirectResponse(url="/docs")

@app.get("/favicon.ico", include_in_schema=False)
def favicon():
    return Response(status_code=204)

# Health + version
@app.get("/healthz", include_in_schema=False)
def healthz():
    return {"status": "ok"}

@app.get("/version", include_in_schema=False)
def version():
    def v(pkg):
        try:
            return importlib.import_module(pkg).__version__
        except Exception:
            return "n/a"
    return {
        "fastapi": v("fastapi"),
        "starlette": v("starlette"),
        "pydantic": v("pydantic"),
        "langchain": v("langchain"),
        "langchain_core": v("langchain_core"),
        "langserve": v("langserve"),
        "langchain_openai": v("langchain_openai"),
        "uvicorn": v("uvicorn"),
    }

# ===== Routes via LangServe =====
openai_model = ChatOpenAI(model="gpt-4o-mini")

add_routes(
    app,
    openai_model,
    path="/openai",  # -> /openai/invoke, /openai/stream, /openai/batch, /openai/playground/
)

essay_prompt = ChatPromptTemplate.from_template(
    "Write me an essay about {topic} with about 100 words."
)
essay_chain = essay_prompt | openai_model
add_routes(
    app,
    essay_chain,
    path="/essay",   # -> /essay/invoke, /essay/stream, /essay/batch, /essay/playground/
)

if __name__ == "__main__":
    try:
        uvicorn.run(app, host="127.0.0.1", port=3001)
    except KeyboardInterrupt:
        pass  # suppress traceback on Ctrl+C

