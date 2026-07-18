import logging
import os

LOGS_DIR = "logs"
os.makedirs(LOGS_DIR, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[
        logging.FileHandler(os.path.join(LOGS_DIR, "securescope.log")),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger("SecureScope")