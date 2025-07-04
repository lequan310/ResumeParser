from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.v1.routes import routers as v1_routers
from core.config import settings
from core.container import Container
from core.db import get_connection_pool
from utils.logger_utils import get_logger

logger = get_logger(__name__)
container = Container()


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Application lifespan manager for startup and shutdown events.
    """
    # Startup
    logger.info("Starting up the application...")

    # Initialize database connection pool
    pool = get_connection_pool()
    await pool.open()

    # Setup chat service
    chat_service = container.chat_service()
    await chat_service.setup()

    logger.info("Application startup complete.")

    yield

    # Shutdown
    logger.info("Shutting down the application...")

    # Unwire dependencies
    container.unwire()

    # Close database connection pool
    await pool.close()

    logger.info("Application shutdown complete.")


def create_fastapi_app() -> FastAPI:
    """
    Create and configure the FastAPI application.

    Returns:
        FastAPI: Configured FastAPI application instance.
    """

    # Create the FastAPI app with lifespan
    app = FastAPI(title="Resume Parser API", version="0.1.0", lifespan=lifespan)

    # Set the application container
    app.container = container

    # Include the routers
    app.include_router(v1_routers)

    # Add CORS middleware
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.ALLOWED_ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return app


app = create_fastapi_app()


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


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "app:app",
        host=settings.API_HOST,
        port=settings.API_PORT,
    )
