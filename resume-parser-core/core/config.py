import logging
import logging.config
from pathlib import Path

from dotenv import load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict

from utils.logger_utils import select_info_only

load_dotenv()


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    BASE_DIR: Path = Path(__file__).parent.parent.absolute()
    LOGS_DIR: Path = Path(BASE_DIR, "logs")

    ALLOWED_ORIGINS: list[str] = ["*"]

    ENV: str = "dev"

    API_HOST: str = "0.0.0.0"
    API_PORT: int = 8000

    # LLM API Keys
    GOOGLE_API_KEY: str = ""
    GROQ_API_KEY: str = ""

    # Database
    POSTGRES_HOST: str = "localhost"
    POSTGRES_PORT: int = 5432
    POSTGRES_USER: str = ""
    POSTGRES_PASSWORD: str = ""
    POSTGRES_DB: str = ""

    # Tools
    TAVILY_API_KEY: str = ""

    # LangSmith Tracing (Optional)
    LANGCHAIN_TRACING_V2: str = "false"
    LANGCHAIN_ENDPOINT: str = ""
    LANGCHAIN_API_KEY: str = ""
    LANGCHAIN_PROJECT: str = ""

    # Timed Rotating File Handlers for weekly log rotation. Use RotatingFileHandler for size based rotation.
    LOGGING_CONFIG: dict = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "minimal": {"format": "%(message)s"},
            "detailed": {
                "format": "%(levelname)s %(asctime)s [%(name)s:%(filename)s:%(funcName)s:%(lineno)d]\n%(message)s\n"
            },
        },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "stream": "ext://sys.stdout",
                "formatter": "minimal",
                "level": logging.DEBUG,
            },
            "info": {
                "class": "logging.handlers.RotatingFileHandler",
                "filename": Path(LOGS_DIR, "info.log"),
                "formatter": "detailed",
                "level": logging.INFO,
                "backupCount": 1,
                "filters": [select_info_only],
                "maxBytes": 102400,  # 100 KB
            },
            "error": {
                "class": "logging.handlers.RotatingFileHandler",
                "filename": Path(LOGS_DIR, "error.log"),
                "formatter": "detailed",
                "level": logging.ERROR,
                "backupCount": 1,
                "maxBytes": 102400,  # 100 KB
            },
        },
        "loggers": {
            "core": {
                "handlers": ["info", "error"],
                "level": logging.DEBUG,
                "propagate": False,
            },
            "db": {
                "handlers": ["info", "error"],
                "level": logging.DEBUG,
                "propagate": False,
            },
            "api": {
                "handlers": ["info", "error"],
                "level": logging.DEBUG,
                "propagate": False,
            },
        },
        "root": {
            "handlers": ["info", "error"],
            "level": logging.DEBUG,
        },
    }


settings = Settings()
settings.LOGS_DIR.mkdir(parents=True, exist_ok=True)
logging.config.dictConfig(settings.LOGGING_CONFIG)
