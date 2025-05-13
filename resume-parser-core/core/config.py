import logging
import logging.config
import sys
from pathlib import Path
from utils.logger_utils import select_info_only
from pydantic_settings import BaseSettings
from pydantic import computed_field, Field
from dotenv import load_dotenv

load_dotenv()


class Settings(BaseSettings):
    BASE_DIR: Path = Path(__file__).parent.parent.absolute()
    LOGS_DIR: Path = Path(BASE_DIR, "logs")

    ALLOWED_ORIGINS: list[str] = ["*"]

    ENV: str = "dev"

    API_HOST: str = "0.0.0.0"
    API_PORT: int = 8000

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
                "backupCount": 10,
                "filters": [select_info_only],
                "maxBytes": 1048576,  # 1 MB
            },
            "error": {
                "class": "logging.handlers.RotatingFileHandler",
                "filename": Path(LOGS_DIR, "error.log"),
                "formatter": "detailed",
                "level": logging.ERROR,
                "backupCount": 10,
                "maxBytes": 1048576,  # 1 MB
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
