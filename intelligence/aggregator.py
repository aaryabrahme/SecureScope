"""Create the dashboard's stable unified security-report contract."""

import json
from datetime import datetime
from pathlib import Path
from typing import Any

from config import (
    ANOMALY_LATEST_REPORT,
    CORRELATED_EVENTS_PATH,
    SCANNER_LATEST_REPORT,
    UNIFIED_SECURITY_REPORT_PATH,
)
from core.schema import scanner_file_name
from logger import logger


def load_report(path: str | Path) -> list[dict[str, Any]]:
    report_path = Path(path)
    if not report_path.exists():
        raise FileNotFoundError(f"Required report is missing: {report_path}")
    with report_path.open(encoding="utf-8") as report_file:
        data = json.load(report_file)
    if not isinstance(data, list):
        raise ValueError(f"Expected a list of records in report: {report_path}")
    return data


def calculate_security_score(scanner_data: list[dict[str, Any]], events: list[dict[str, Any]]) -> int:
    """Calculate a 0-100 posture score; higher values represent stronger posture."""
    high_risk_files = sum(item.get("risk_level") in {"HIGH", "CRITICAL"} for item in scanner_data)
    anomalies = sum(event.get("risk_status") == "ANOMALY" for event in events)
    return max(0, 100 - high_risk_files * 5 - min(anomalies // 5, 30))


def create_security_report(
    scanner_path: str | Path = SCANNER_LATEST_REPORT,
    anomaly_path: str | Path = ANOMALY_LATEST_REPORT,
    events_path: str | Path = CORRELATED_EVENTS_PATH,
    output_path: str | Path = UNIFIED_SECURITY_REPORT_PATH,
) -> Path:
    """Generate the dashboard report from scanner, anomaly, and correlated-event data."""
    scanner_data = load_report(scanner_path)
    anomaly_data = load_report(anomaly_path)
    events = load_report(events_path)

    high_risk_files = [
        item for item in scanner_data if item.get("risk_level") in {"HIGH", "CRITICAL"}
    ]
    critical_files = [
        item for item in scanner_data
        if any(finding.get("risk") == "CRITICAL" for finding in item.get("findings", []))
    ]
    top_events = sorted(events, key=lambda event: event.get("risk_score", 0), reverse=True)[:10]
    anomalies_detected = sum(event.get("risk_status") == "ANOMALY" for event in events)

    for file_record in high_risk_files:
        file_record.setdefault("file_name", scanner_file_name(file_record))
        file_record.setdefault("file", file_record["file_name"])

    report = {
        "schema_version": "1.0",
        "project": "SecureScope",
        "generated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "data_notice": "Scanner findings and anomaly results are local demo analysis outputs; anomaly status is not confirmation of malicious activity.",
        "summary": {
            "files_scanned": len(scanner_data),
            "sensitive_findings": sum(len(item.get("findings", [])) for item in scanner_data),
            "high_risk_files": len(high_risk_files),
            "events_analyzed": len(anomaly_data),
            "anomalies_detected": anomalies_detected,
        },
        "data_security": {
            "high_risk_files": high_risk_files,
            "critical_files": critical_files,
        },
        "insider_risk": {
            "top_risky_users": top_events,
        },
        "security_score": calculate_security_score(scanner_data, events),
    }

    destination = Path(output_path)
    destination.parent.mkdir(parents=True, exist_ok=True)
    with destination.open("w", encoding="utf-8") as report_file:
        json.dump(report, report_file, indent=2)
    logger.info("Unified security report generated: %s", destination)
    return destination
