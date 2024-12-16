# Setup Instructions
## Docker

**Pre-requisites:** Have Docker Installed and Running

**Steps:**
1. Clone the repo
```shell
git clone https://github.com/lequan310/ResumeParser.git
```

2. Create .env files for inside BE (resume-parser-core) and FE (webapp) folders. Copy the format from [.env.example](./resume-parser-core/.env.example) for BE and [.env.example](./webapp/.env.example) for FE.<br></br>

3. Build Images and Run the Containers via Docker Compose
```shell
docker compose up --build
```

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

4. Create .env file in the folder following the [.env.example](./resume-parser-core/.env.example)
```dotenv
# API
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

## FE (Local)
**Pre-requisites:** Have NPM installed

**Steps:**
1. cd into FE folder
```shell
cd webapp
```

2. Install dependencies
```node
npm install
```

3. Create .env file in the folder following the [.env.example](./webapp/.env.example)
```dotenv
```

4. Run the React application
```node
npm run dev
```