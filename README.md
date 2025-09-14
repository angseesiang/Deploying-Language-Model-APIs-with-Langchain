# 🚀 Deploying Language Model APIs with LangChain

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue)](#)
[![FastAPI](https://img.shields.io/badge/FastAPI-Web%20Framework-green)](#)
[![LangChain](https://img.shields.io/badge/LangChain-Framework-orange)](#)

This repository contains my training exercise on **deploying language
model APIs** using **LangChain**, **FastAPI**, and **LangServe**.\
It demonstrates how to expose **OpenAI‑powered endpoints** via FastAPI,
test them with a Python client, stream responses, and try interactive
playgrounds.

------------------------------------------------------------------------

## 📖 Contents

-   `app.py` -- FastAPI + LangServe application:
    -   Exposes **OpenAI GPT routes** (`/openai`)
    -   Adds a sample **essay generation chain** (`/essay`)
    -   Health check and version endpoints
    -   CORS, optional static files, and OpenAPI docs
-   `client.py` -- Simple client to call `/openai` and `/essay`
    (invocation + streaming)
-   `requirements.txt` -- Python dependencies
-   `url.txt` -- Project reference link

------------------------------------------------------------------------

## 🚀 How to Use

### 1) Clone this repository

``` bash
git clone https://github.com/angseesiang/deploying-language-model-apis-with-langchain.git
cd deploying-language-model-apis-with-langchain
```

### 2) Create and activate a virtual environment (recommended)

``` bash
python -m venv venv
source venv/bin/activate   # Linux / macOS
venv\Scripts\activate    # Windows
```

### 3) Install dependencies

``` bash
pip install -r requirements.txt
python -m pip install -i https://pypi.org/simple "sse-starlette==1.6.5"
```

### 4) Configure API keys

Create a `.env` file in the project root and add:

    OPENAI_API_KEY=your_openai_api_key
    LANGCHAIN_API_KEY=your_langchain_api_key

### 5) Start the API server

Run the FastAPI app locally:

``` bash
python app.py
```

This launches the server on **http://127.0.0.1:3001** and exposes: - API
Docs (Swagger): http://127.0.0.1:3001/docs - Health check:
http://127.0.0.1:3001/healthz - **LangServe Playgrounds** (interactive
UIs): - Essay chain: http://127.0.0.1:3001/essay/playground/ - OpenAI
chat: http://127.0.0.1:3001/openai/playground/

### 6) Test the API with the Python client

In a separate terminal (with the virtual environment activated), run:

``` bash
python client.py
```

The client will: - Invoke `/openai/invoke` with a prompt - Invoke
`/essay/invoke` with a topic - Demonstrate streaming from
`/openai/stream` and `/essay/stream`

------------------------------------------------------------------------

## 🛠️ Requirements

See [`requirements.txt`](requirements.txt): - `fastapi`, `starlette`,
`pydantic`, `typing_extensions` - `langchain`, `langchain-core`,
`langserve`, `langchain-openai`, `langchain-ollama` (optional) -
`python-dotenv`, `requests`, `uvicorn` - `sse-starlette==1.6.5`

------------------------------------------------------------------------

## 📌 Notes

-   Built during my **AI/ML training** to learn how to **deploy and test
    language model APIs**.
-   Supports both **non‑streaming** and **streaming** responses.
-   Easily extend by adding more LangChain chains (e.g., RAG, tools, or
    Ollama routes).

------------------------------------------------------------------------

## 📜 License

This repository is shared for **educational purposes**. Please credit if
you use it in your own work.
