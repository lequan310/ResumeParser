# Setup Instructions
## Docker

**Pre-requisites:** Have Docker Installed and Running

**Steps:**
1. Clone the repo
```bash
git clone https://github.com/lequan310/ResumeParser.git
```

2. Build Images and Run the Containers via Docker Compose
```bash
docker compose up --build
```

## BE (Local)
**Pre-requisites:** Have any Python Package Manager installed

**Steps**:
1. cd into BE folder
```bash
cd resume-parser-core
```

2. Create a Python Virtual Environment (Ideally 3.12+). Example using conda:
```bash
conda create -p .venv python=3.12.7 -y
conda activate .venv/
```

3. Install uv package manager and install the dependencies
```bash
pip install uv
uv sync
```

4. Run the FastAPI application
```bash
uvicorn api.app:app --host 0.0.0.0 --port 8000 --reload
```

## FE (Local)
**Pre-requisites:** Have NPM installed

**Steps:**
1. cd into FE folder
```bash
cd webapp
```

2. Install dependencies
```bash
npm install
```

3. Run the React application
```bash
npm run dev
```