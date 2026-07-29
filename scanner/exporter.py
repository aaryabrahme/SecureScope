from datetime import datetime
import json
from typing import Any

from config import SCANNER_REPORTS_DIR
from logger import logger

LATEST_DIR = SCANNER_REPORTS_DIR / "latest"
ARCHIVE_DIR = SCANNER_REPORTS_DIR / "archive"



def create_report_dirs():

    LATEST_DIR.mkdir(
        parents=True,
        exist_ok=True
    )

    ARCHIVE_DIR.mkdir(
        parents=True,
        exist_ok=True
    )



def export_json(reports: list[dict[str, Any]]):

    create_report_dirs()


    timestamp = datetime.now().strftime(
        "%Y%m%d_%H%M%S"
    )


    archive_file = ARCHIVE_DIR / (
        f"scan_report_{timestamp}.json"
    )


    latest_file = LATEST_DIR / (
        "scan_report.json"
    )


    # archive version

    with open(
        archive_file,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            reports,
            file,
            indent=4
        )


    # dashboard version

    with open(
        latest_file,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            reports,
            file,
            indent=4
        )


    logger.info(
        "Scanner report saved: %s",
        latest_file
    )


    return latest_file
