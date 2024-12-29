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
docker compose up --build -d
```

## BE (Local)
Check [README.md](./resume-parser-core/README.md)

## FE (Local)
Check [README.md](./webapp/README.md)