import logging
import sys
from logging import config
from pathlib import Path
from rich.logging import RichHandler

BASE_DIR = Path(__file__).parent.parent.parent.absolute()
LOGS_DIR = Path(BASE_DIR, "logs")
LOGS_DIR.mkdir(parents=True, exist_ok=True)

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
        # Timed Rotating File Handlers
        "info": {
            "class": "logging.handlers.TimedRotatingFileHandler",
            "filename": Path(LOGS_DIR, "info.log"),
            "formatter": "detailed",
            "level": logging.INFO,
            "when": "W0",  # Rotate weekly on Monday
            "interval": 1,  # Rotate every week
            "backupCount": 4,
        },
        "error": {
            "class": "logging.handlers.TimedRotatingFileHandler",
            "filename": Path(LOGS_DIR, "error.log"),
            "formatter": "detailed",
            "level": logging.ERROR,
            "when": "W0",  # Rotate weekly on Monday
            "interval": 1,  # Rotate every week
            "backupCount": 4,
        },
        # Rotating File Handlers
        # "info": {
        #     "class": "logging.handlers.RotatingFileHandler",
        #     "filename": Path(LOGS_DIR, "info.log"),
        #     "maxBytes": 10485760,  # 1 MB
        #     "backupCount": 10, # Keep 10 logs
        #     "formatter": "detailed",
        #     "level": logging.INFO,
        # },
        # "error": {
        #     "class": "logging.handlers.RotatingFileHandler",
        #     "filename": Path(LOGS_DIR, "error.log"),
        #     "maxBytes": 10485760,  # 1 MB
        #     "backupCount": 10,
        #     "formatter": "detailed",
        #     "level": logging.ERROR,
        # },
    },
    "loggers": {
        "Core": {
            "handlers": ["console", "info", "error"],
            "level": logging.DEBUG,
            "propagate": False,
        },
    },
}

config.dictConfig(logging_config)
logger = logging.getLogger("Core")
logger.setLevel(logging.DEBUG)

if len(logger.handlers):
    logger.handlers[0] = RichHandler(markup=True)
else:
    logger.handlers.append(RichHandler(markup=True))
