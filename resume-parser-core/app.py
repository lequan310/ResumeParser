import os
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from core.config import settings
from api.v1.routes import routers as v1_routers
from core.db import get_connection_pool
from utils.logger_utils import get_logger

logger = get_logger(__name__)

# Create the FastAPI app
if settings.ENV != "prod":
    app = FastAPI(title="Resume Parser API", version="0.1.0")
else:
    app = FastAPI(
        title="Resume Parser API",
        version="0.1.0",
        docs_url=None,
        redoc_url=None,
        openapi_url=None,
    )

# Include the routers
app.include_router(v1_routers)


@app.get("/")
async def root():
    return {"message": "Hello World!"}


@app.get("/health")
async def health_check():
    # Health check database connection
    async with get_connection_pool().connection() as conn:
        async with conn.cursor() as cur:
            await cur.execute("SELECT 1")  # Minimal query
            result = await cur.fetchone()
            if result == (1,):
                return {"status": "OK"}
            else:
                return {"status": "Not OK"}


app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "api.app:app",
        host=os.getenv("API_HOST", "0.0.0.0"),
        port=int(os.getenv("API_PORT", 8000)),
    )
