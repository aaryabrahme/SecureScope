from pathlib import Path
from datetime import datetime
import shutil

from logger import logger


REPORTS_DIR = Path("reports")

LATEST_DIR = REPORTS_DIR / "latest"

ARCHIVE_DIR = REPORTS_DIR / "archive"



def create_report_dirs():

    LATEST_DIR.mkdir(
        parents=True,
        exist_ok=True
    )

    ARCHIVE_DIR.mkdir(
        parents=True,
        exist_ok=True
    )



def export_csv(df, timestamp):

    create_report_dirs()


    archive_file = ARCHIVE_DIR / (
        f"insider_risk_{timestamp}.csv"
    )


    latest_file = LATEST_DIR / (
        "insider_risk.csv"
    )


    # archive copy

    df.to_csv(
        archive_file,
        index=False
    )


    # dashboard copy

    df.to_csv(
        latest_file,
        index=False
    )


    logger.info(
        "CSV report saved: %s",
        latest_file
    )


    return latest_file




def export_json(df, timestamp):

    create_report_dirs()


    archive_file = ARCHIVE_DIR / (
        f"insider_risk_{timestamp}.json"
    )


    latest_file = LATEST_DIR / (
        "insider_risk.json"
    )


    # archive copy

    df.to_json(
        archive_file,
        orient="records",
        indent=4
    )


    # dashboard copy

    df.to_json(
        latest_file,
        orient="records",
        indent=4
    )


    logger.info(
        "JSON report saved: %s",
        latest_file
    )


    return latest_file
