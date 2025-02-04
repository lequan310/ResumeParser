from functools import lru_cache
from psycopg_pool import AsyncConnectionPool
from core.config import os, get_logger

logger = get_logger(__name__)


@lru_cache(maxsize=1)
def get_connection_pool():
    try:
        pool = AsyncConnectionPool(
            conninfo=f"postgresql://{os.environ['POSTGRES_USER']}:{os.environ['POSTGRES_PASSWORD']}@{os.environ['POSTGRES_HOST']}:{os.environ['POSTGRES_PORT']}/{os.environ['POSTGRES_DB']}",
            max_size=20,
            kwargs={
                "autocommit": True,
                "prepare_threshold": 0,
            },
            open=False,
        )
        logger.info("PostgreSQL connection pool created successfully.")
        return pool
    except Exception as e:
        logger.exception(f"Error creating connection pool: {e}")
        raise
