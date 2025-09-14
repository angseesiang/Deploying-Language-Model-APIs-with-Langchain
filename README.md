# 🚀 Deploying Language Model APIs with LangChain

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue)](#)
[![FastAPI](https://img.shields.io/badge/FastAPI-Web%20Framework-green)](#)
[![LangChain](https://img.shields.io/badge/LangChain-Framework-orange)](#)

This repository contains my training exercise on **deploying language
model APIs** using **LangChain**, **FastAPI**, and **LangServe**.\
It demonstrates how to expose **OpenAI-powered endpoints** via FastAPI,
test them using a client, and stream responses.

🔗 GitHub Repo:
[Deploying-Language-Model-APIs-with-Langchain](https://github.com/angseesiang/Deploying-Language-Model-APIs-with-Langchain)

------------------------------------------------------------------------

## 📖 Contents

-   `app.py` -- FastAPI + LangServe application:
    -   Exposes **OpenAI GPT routes** (`/openai`)
    -   Adds a sample **essay generation chain** (`/essay`)
    -   Provides health check and version endpoints
    -   Supports CORS, static files, and OpenAPI docs
-   `client.py` -- Test client:
    -   Calls `/openai/invoke` and `/essay/invoke`
    -   Supports streaming responses from `/openai/stream` and
        `/essay/stream`
-   `requirements.txt` -- Dependencies (FastAPI, LangChain, LangServe,
    OpenAI, etc.)
-   `url.txt` -- Reference to GitHub repository

------------------------------------------------------------------------

## 🚀 How to Use

### 1. Clone this repository

``` bash
git clone https://github.com/angseesiang/deploying-language-model-apis-with-langchain.git
cd deploying-language-model-apis-with-langchain
```

### 2. Create and activate a virtual environment

``` bash
python -m venv venv
source venv/bin/activate   # On Linux / macOS
venv\Scripts\activate    # On Windows
```

### 3. Install dependencies

``` bash
pip install -r requirements.txt
```

### 4. Configure API keys

Create a `.env` file in the project root and add:

    OPENAI_API_KEY=your_openai_api_key
    LANGCHAIN_API_KEY=your_langchain_api_key

### 5. Run the FastAPI server

``` bash
uvicorn app:app --host 127.0.0.1 --port 3001 --reload
```

This will start the server at `http://127.0.0.1:3001`.\
You can access: - API docs: <http://127.0.0.1:3001/docs> - Health check:
<http://127.0.0.1:3001/healthz>

### 6. Test the API using the client

``` bash
python client.py
```

This will: - Call `/openai/invoke` with a user question - Call
`/essay/invoke` with a topic - Stream responses from both endpoints

------------------------------------------------------------------------

## 🛠️ Requirements

See [`requirements.txt`](requirements.txt): - `fastapi` - `starlette` -
`pydantic` - `typing_extensions` - `langchain` - `langchain-core` -
`langserve` - `langchain-openai` - `langchain-ollama` (optional) -
`python-dotenv` - `requests` - `uvicorn`

------------------------------------------------------------------------

## 📌 Notes

-   This project was created during my **AI/ML training** to understand
    how to **deploy and test language model APIs**.
-   It supports both **non-streaming** and **streaming** API responses.
-   You can extend it by adding additional LangChain chains or models
    (e.g., Ollama).

------------------------------------------------------------------------

## 📜 License

This repository is shared for **educational purposes**. Please credit if
you use it in your own work.
