# Project Description
Resume Parser is a web application that showcases AI's capabilities in hiring and career consultancy. The 2 main features are Resume Parsing and AI Career Consultant Chatbot:
- Resume Parsing: User upload a resume file in .pdf format, and the AI will extract the information from the resume and output in a structured format.
- AI Career Consultant Chatbot: A ReAct agent that can chat and memorize conversation. Each time a resume is uploaded, a new conversation will be started.
- Resume Analyzer: User upload job description to compare resume against it.

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
