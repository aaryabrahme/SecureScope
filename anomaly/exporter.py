import os
from datetime import datetime
from anomaly.logger import logger

REPORTS_DIR = "reports"

os.makedirs(REPORTS_DIR, exist_ok=True)
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S"),

def export_csv(df, timestamp):
    filename = os.path.join(
        REPORTS_DIR,
        f"insider_risk_{timestamp}.csv"
    )

    df.to_csv(
        filename,
        index=False
    )

    return filename
    logger.info(f"CSV report saved: {filename}")

def export_json(df, timestamp):
    filename = os.path.join(
        REPORTS_DIR,
        f"insider_risk_{timestamp}.json"
    )

    df.to_json(
        filename,
        orient="records",
        indent=4
    )

    return filename
    logger.info(f"JSON report saved: {filename}")