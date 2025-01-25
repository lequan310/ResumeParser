from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.routes.files import router as files_router
from core.config import get_logger

logger = get_logger(__name__)

# Create the FastAPI app
app = FastAPI(title="Resume Parser API", version="0.1.0")

# Include the routers
app.include_router(files_router)


@app.get("/health")
def health_check():
    return {"message": "OK"}


@app.get("/test_log")
def test_log():
    logger.info("This is an info log")
    return {"message": "Check the logs"}


# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
