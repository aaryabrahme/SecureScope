import logging
from logging.handlers import RotatingFileHandler

from config import LOG_FILE


def setup_logger() -> logging.Logger:
    """
    Configure and return the global SecureScope logger.
    """

    logger = logging.getLogger(
        "SecureScope"
    )

    logger.setLevel(
        logging.INFO
    )


    # Prevent duplicate handlers
    if logger.handlers:
        return logger


    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )


    file_handler = RotatingFileHandler(
        LOG_FILE,
        maxBytes=5_000_000,
        backupCount=5,
    )

    file_handler.setFormatter(
        formatter
    )


    console_handler = logging.StreamHandler()

    console_handler.setFormatter(
        formatter
    )


    logger.addHandler(
        file_handler
    )

    logger.addHandler(
        console_handler
    )


    return logger



logger = setup_logger()