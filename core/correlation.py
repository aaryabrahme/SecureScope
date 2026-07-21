import json
from pathlib import Path

from logger import logger

from core.risk_engine import create_risk_event


def load_json(path):
    """
    Load JSON report.
    """

    with open(path, "r") as file:
        return json.load(file)



def correlate_reports(
    scanner_report_path,
    anomaly_report_path,
):
    """
    Combine scanner and anomaly reports.
    """

    logger.info(
        "Starting risk correlation..."
    )


    scanner_reports = load_json(
        scanner_report_path
    )


    anomaly_reports = load_json(
        anomaly_report_path
    )


    final_events = []


    for anomaly in anomaly_reports:

        employee_id = anomaly.get(
            "employee_id"
        )

        file_name = anomaly.get(
            "file_name"
        )


        matching_scanner = None


        for scan in scanner_reports:

            if scan.get("file_name") == file_name:
                matching_scanner = scan
                break


        if matching_scanner is None:

            matching_scanner = {
                "risk_score": 0,
                "findings": []
            }


        event = create_risk_event(
            employee_id,
            file_name,
            matching_scanner,
            anomaly,
        )


        final_events.append(
            event
        )


    logger.info(
        "Correlation completed | Events=%d",
        len(final_events),
    )


    return final_events



def save_final_report(
    events,
    output_path="reports/securescope_final_report.json"
):

    Path(output_path).parent.mkdir(
        exist_ok=True
    )


    with open(output_path, "w") as file:

        json.dump(
            events,
            file,
            indent=4
        )


    logger.info(
        "Final report saved: %s",
        output_path
    )


    return output_path