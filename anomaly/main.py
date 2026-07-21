from datetime import datetime

from anomaly.console import (
    print_export_summary,
    print_summary,
    print_top_events,
)
from anomaly.exporter import export_csv, export_json
from logger import logger
from anomaly.pipeline import run_pipeline
from anomaly.ranking import get_top_risk_events
from anomaly.summary import generate_summary


def main() -> None:
    """
    Entry point for SecureScope Phase 2.

    Runs the anomaly detection pipeline,
    displays a summary,
    exports reports,
    and logs execution.
    """

    logger.info("Starting SecureScope Phase 2")

    df = run_pipeline()

    summary = generate_summary(df)

    print_summary(summary)

    top_events = get_top_risk_events(df)

    print_top_events(top_events)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    csv_file = export_csv(df, timestamp)
    json_file = export_json(df, timestamp)

    print_export_summary(
        csv_file,
        json_file,
    )

    logger.info("SecureScope Phase 2 completed successfully.")


if __name__ == "__main__":
    main()
