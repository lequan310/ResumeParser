from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.routes.files import router as files_router
from api.routes.chat import router as chat_router
from core.config import os, get_logger
from db.pool import get_connection_pool

logger = get_logger(__name__)


# Create the FastAPI app
if os.getenv("DEPLOY", "false") == "false":
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
app.include_router(files_router)
app.include_router(chat_router)


@app.get("/health")
async def health_check():
    async with get_connection_pool().connection() as conn:
        async with conn.cursor() as cur:
            await cur.execute("SELECT 1")  # Minimal query
            result = await cur.fetchone()
            if result == (1,):
                return {"message": "OK"}
            else:
                return {"message": "Not OK"}


# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)
