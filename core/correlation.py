import json
from pathlib import Path
from typing import Any

from config import CORRELATED_EVENTS_PATH
from core.risk_engine import create_risk_event
from core.schema import normalize_reasons, scanner_file_name
from logger import logger


def load_json(path: str | Path) -> list[dict[str, Any]]:
    report_path = Path(path)
    if not report_path.exists():
        raise FileNotFoundError(f"Required report is missing: {report_path}")

    with report_path.open(encoding="utf-8") as report_file:
        data = json.load(report_file)

    if not isinstance(data, list):
        raise ValueError(f"Expected a list of records in report: {report_path}")
    return data


def correlate_reports(
    scanner_report_path: str | Path,
    anomaly_report_path: str | Path,
) -> list[dict[str, Any]]:
    """Enrich each anomaly event with matching scanner findings by file name."""
    logger.info("Starting risk correlation...")
    scanner_reports = load_json(scanner_report_path)
    anomaly_reports = load_json(anomaly_report_path)
    scans_by_file = {
        scanner_file_name(scan): scan
        for scan in scanner_reports
        if scanner_file_name(scan)
    }

    final_events: list[dict[str, Any]] = []
    for anomaly in anomaly_reports:
        file_name = str(anomaly.get("file_name") or "")
        scanner_record = scans_by_file.get(file_name, {"risk_score": 0, "findings": []})
        event = create_risk_event(
            str(anomaly.get("employee_id") or "UNKNOWN"),
            file_name,
            scanner_record,
            anomaly,
        )
        event["reasons"] = normalize_reasons(event["reasons"])
        final_events.append(event)

    logger.info("Correlation completed | Events=%d", len(final_events))
    return final_events


def save_final_report(
    events: list[dict[str, Any]],
    output_path: str | Path = CORRELATED_EVENTS_PATH,
) -> Path:
    report_path = Path(output_path)
    report_path.parent.mkdir(parents=True, exist_ok=True)
    with report_path.open("w", encoding="utf-8") as report_file:
        json.dump(events, report_file, indent=2)
    logger.info("Correlated events saved: %s", report_path)
    return report_path
