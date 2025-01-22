# Setup Instructions
## FE (Local)
**Pre-requisites:** Have Node Installed and bun package manager installed. To install bun:
```node
npm install -g bun
```

**Steps:**
1. cd into FE folder
```shell
cd webapp
```

2. Install dependencies
```node
bun install
```

3. Create .env file in the folder following the [.env.example](.env.example)
```dotenv
PARSER_API=
```

4. Run the React application
```node
bun run dev
```