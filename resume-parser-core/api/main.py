import uvicorn
import os
from dotenv import load_dotenv

load_dotenv()


def main():
    uvicorn.run(
        "api.app:app",
        host=os.getenv("API_HOST", "0.0.0.0"),
        port=int(os.getenv("API_PORT", 8000)),
    )


if __name__ == "__main__":
    main()
