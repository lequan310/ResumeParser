import logging
from rich.logging import RichHandler


def select_info_only(record: logging.LogRecord) -> bool:
    return record.levelno == logging.INFO


def get_logger(name: str | None = None) -> logging.Logger:
    logger = logging.getLogger(name)
    if len(logger.handlers):
        logger.handlers[0] = RichHandler(markup=True)
    else:
        logger.addHandler(RichHandler(markup=True))
    return logger
