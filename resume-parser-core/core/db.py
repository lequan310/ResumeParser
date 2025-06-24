from functools import lru_cache

from psycopg import Error as PsycopgError
from psycopg_pool import AsyncConnectionPool

from core.config import settings
from utils.logger_utils import get_logger

logger = get_logger(__name__)


@lru_cache(maxsize=1)
def get_connection_pool():
    try:
        pool = AsyncConnectionPool(
            conninfo=f"postgresql://{settings.POSTGRES_USER}:{settings.POSTGRES_PASSWORD}@{settings.POSTGRES_HOST}:{settings.POSTGRES_PORT}/{settings.POSTGRES_DB}",
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


async def reset_db():
    async with get_connection_pool().connection() as conn:
        # Disable autocommit to create a single transaction.
        await conn.set_autocommit(False)
        async with conn.cursor() as cur:
            try:
                # Last time I drop without truncating, it caused an error when starting the server again
                await cur.execute(
                    "TRUNCATE TABLE public.checkpoints, public.checkpoint_writes, public.checkpoint_migrations, public.checkpoint_blobs;"
                )
                await cur.execute(
                    "DROP TABLE public.checkpoints, public.checkpoint_writes, public.checkpoint_migrations, public.checkpoint_blobs;"
                )
                await conn.commit()
                logger.info("Database reset successfully.")
            except PsycopgError as e:
                # Rollback the transaction if any error occurred.
                await conn.rollback()
                logger.exception(f"Error resetting database: {e}")
                # Consider re-raising the exception or logging it appropriately.
                raise
