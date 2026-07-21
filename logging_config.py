import logging
from pathlib import Path

from config import LOGS_DIR

LOGS_DIR.mkdir(exist_ok=True)

LOG_FILE = LOGS_DIR / "securescope.log"


def setup_logging() -> logging.Logger:
    """
    Configure and return the SecureScope logger.
    """

    logger = logging.getLogger("SecureScope")

    if logger.handlers:
        return logger

    logger.setLevel(logging.INFO)

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    )

    file_handler = logging.FileHandler(LOG_FILE)
    file_handler.setFormatter(formatter)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger