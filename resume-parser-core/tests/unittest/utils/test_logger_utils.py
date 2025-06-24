import logging

import pytest
from rich.logging import RichHandler

from utils.logger_utils import get_logger, select_info_only


@pytest.fixture
def log_record_info():
    return logging.LogRecord(
        name="test",
        level=logging.INFO,
        pathname="test_path",
        lineno=1,
        msg="Test info message",
        args=(),
        exc_info=None,
        func="test_func",
    )


@pytest.fixture
def log_record_debug():
    return logging.LogRecord(
        name="test",
        level=logging.DEBUG,
        pathname="test_path",
        lineno=1,
        msg="Test debug message",
        args=(),
        exc_info=None,
        func="test_func",
    )


def test_select_info_only_with_info_record(log_record_info):
    assert select_info_only(log_record_info) is True


def test_select_info_only_with_debug_record(log_record_debug):
    assert select_info_only(log_record_debug) is False


def test_get_logger_returns_logger_instance():
    logger = get_logger("test_logger_instance")
    assert isinstance(logger, logging.Logger)
    assert logger.name == "test_logger_instance"


def test_get_logger_adds_rich_handler():
    logger_name = "test_logger_handler"
    # Ensure the logger doesn't exist or has no handlers from a previous test run
    if logger_name in logging.Logger.manager.loggerDict:
        del logging.Logger.manager.loggerDict[logger_name]

    logger = get_logger(logger_name)
    assert len(logger.handlers) == 1
    assert isinstance(logger.handlers[0], RichHandler)
    assert logger.handlers[0].markup is True


def test_get_logger_replaces_existing_handler():
    logger_name = "test_logger_replace_handler"
    # Ensure the logger doesn't exist or has no handlers from a previous test run
    if logger_name in logging.Logger.manager.loggerDict:
        del logging.Logger.manager.loggerDict[logger_name]

    logger = logging.getLogger(logger_name)
    # Add a dummy handler
    dummy_handler = logging.StreamHandler()
    logger.addHandler(dummy_handler)

    # Now get the logger using the utility function
    updated_logger = get_logger(logger_name)
    assert len(updated_logger.handlers) == 1
    assert isinstance(updated_logger.handlers[0], RichHandler)
    assert updated_logger.handlers[0].markup is True
    assert updated_logger.handlers[0] is not dummy_handler


def test_get_logger_with_none_name():
    logger = get_logger()  # Call with no name
    assert isinstance(logger, logging.Logger)
    assert logger.name == "root"  # Default logger name when None is provided
    assert len(logger.handlers) >= 1  # Root logger might have other handlers
    assert any(isinstance(h, RichHandler) and h.markup for h in logger.handlers)

    # Clean up handlers added to the root logger if necessary for other tests
    # This is a bit tricky as other tests or libraries might also use the root logger.
    # For simplicity, we'll just check if a RichHandler was added.
    # If strict isolation is needed, more complex teardown might be required.
    # For now, let's remove the RichHandler we might have added to root
    # to avoid side effects if this test runs multiple times or affects other tests.
    # This assumes the RichHandler is the last one added by our function.
    if logger.handlers and isinstance(logger.handlers[-1], RichHandler):
        # A more robust way would be to store the original handlers and restore them.
        # Or, if the function always replaces/adds at index 0 for non-root loggers,
        # and adds for root, the logic might differ.
        # Given the current implementation, get_logger might add a new RichHandler
        # or replace an existing one if it's the first.
        # For the root logger, it's likely to add.
        pass  # Avoid modifying root logger handlers too aggressively in a simple test.
