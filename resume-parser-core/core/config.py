import os
import logging
import sys
from logging import config
from pathlib import Path
from rich.logging import RichHandler
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).parent.parent.absolute()
LOGS_DIR = Path(BASE_DIR, "logs")
LOGS_DIR.mkdir(parents=True, exist_ok=True)


def select_info_only(record: logging.LogRecord) -> bool:
    return record.levelno == logging.INFO


def get_logger(name: str | None = None) -> logging.Logger:
    logger = logging.getLogger(name)
    if len(logger.handlers):
        logger.handlers[0] = RichHandler(markup=True)
    else:
        logger.addHandler(RichHandler(markup=True))
    return logger


# Timed Rotating File Handlers for weekly log rotation. Use RotatingFileHandler for size based rotation.
logging_config = {
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
            "stream": sys.stdout,
            "formatter": "minimal",
            "level": logging.DEBUG,
        },
        # "info": {
        #     "class": "logging.handlers.TimedRotatingFileHandler",
        #     "filename": Path(LOGS_DIR, "info.log"),
        #     "formatter": "detailed",
        #     "level": logging.INFO,
        #     "when": "W0",  # Rotate weekly on Monday
        #     "interval": 1,  # Rotate every week
        #     "backupCount": 4,
        #     "filters": [select_info_only],
        # },
        # "error": {
        #     "class": "logging.handlers.TimedRotatingFileHandler",
        #     "filename": Path(LOGS_DIR, "error.log"),
        #     "formatter": "detailed",
        #     "level": logging.ERROR,
        #     "when": "W0",  # Rotate weekly on Monday
        #     "interval": 1,  # Rotate every week
        #     "backupCount": 4,
        # },
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
        "core.llm": {
            "handlers": ["console", "info", "error"],
            "level": logging.DEBUG,
            "propagate": False,
        },
        "core.parser.utils.parse_utils": {
            "handlers": ["console", "info", "error"],
            "level": logging.DEBUG,
            "propagate": False,
        },
        "core.utils.pdf_utils": {
            "handlers": ["console", "info", "error"],
            "level": logging.DEBUG,
            "propagate": False,
        },
        "core.chat.utils.nodes": {
            "handlers": ["console", "info", "error"],
            "level": logging.DEBUG,
            "propagate": False,
        },
        "core.chat.graph": {
            "handlers": ["console", "info", "error"],
            "level": logging.DEBUG,
            "propagate": False,
        },
        "core.analysis.analysis_utils": {
            "handlers": ["console", "info", "error"],
            "level": logging.DEBUG,
            "propagate": False,
        },
        "db.pool": {
            "handlers": ["console", "info", "error"],
            "level": logging.DEBUG,
            "propagate": False,
        },
    },
    "root": {
        "handlers": ["info", "error"],
        "level": logging.DEBUG,
    },
}

config.dictConfig(logging_config)
