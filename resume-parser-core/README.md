# Setup Instructions
## BE (Local)
**Pre-requisites:** Have any Python Package Manager installed

**Steps**:
1. cd into BE folder
```shell
cd resume-parser-core
```

2. Create a Python Virtual Environment (Ideally 3.12+). Example using conda:
```python
conda create -p .venv python=3.12.7 -y
conda activate .venv/
```

3. Install uv package manager and install the dependencies
```python
pip install uv
uv sync
```

4. Create .env file in the folder following the [.env.example](.env.example)
```dotenv
# API
API_HOST=
API_PORT=

# LLM
GOOGLE_API_KEY=

# Tracing via LangSmith (Optional)
LANGCHAIN_TRACING_V2=
LANGCHAIN_ENDPOINT=
LANGCHAIN_API_KEY=
LANGCHAIN_PROJECT=
```

5. Run the FastAPI application
```python
uvicorn api.app:app --host 0.0.0.0 --port 8000 --reload
```
