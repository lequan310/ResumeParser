import os
import uvicorn
from dotenv import load_dotenv

load_dotenv()


def main():
    uvicorn.run(
        "api.app:app", host="0.0.0.0", port=int(os.getenv("PORT", 8000), reload=True)
    )


if __name__ == "__main__":
    main()
