from typing import Any

from logger import logger

from constants import (
    CRITICAL_THRESHOLD,
    HIGH_THRESHOLD,
    MEDIUM_THRESHOLD,
)


def calculate_final_severity(score: int) -> str:
    """
    Convert final risk score into severity.
    """

    if score >= CRITICAL_THRESHOLD:
        return "CRITICAL"

    elif score >= HIGH_THRESHOLD:
        return "HIGH"

    elif score >= MEDIUM_THRESHOLD:
        return "MEDIUM"

    return "LOW"



def calculate_unified_risk(
    scanner_risk: int,
    anomaly_risk: int,
) -> dict[str, Any]:
    """
    Combine scanner and anomaly risks.

    Scanner:
        Data sensitivity risk

    Anomaly:
        Behaviour risk
    """

    logger.debug(
        "Calculating unified risk | Scanner=%d Anomaly=%d",
        scanner_risk,
        anomaly_risk,
    )


    # Weighted scoring
    #
    # Behaviour is slightly more important
    # because insider attacks depend on actions.

    final_score = int(
        (scanner_risk * 0.4)
        +
        (anomaly_risk * 0.6)
    )


    final_score = min(
        final_score,
        100
    )


    severity = calculate_final_severity(
        final_score
    )


    return {
        "final_risk_score": final_score,
        "severity": severity,
    }



def create_risk_event(
    employee_id: str,
    file_name: str,
    scanner_report: dict[str, Any],
    anomaly_report: dict[str, Any],
) -> dict[str, Any]:
    """
    Create a unified SecureScope event.
    """


    scanner_score = scanner_report.get(
        "risk_score",
        0
    )


    anomaly_score = anomaly_report.get(
        "risk_score",
        0
    )


    unified = calculate_unified_risk(
        scanner_score,
        anomaly_score,
    )


    return {

        "employee_id": employee_id,

        "file_name": file_name,

        "scanner_risk_score": scanner_score,
        "anomaly_risk_score": anomaly_score,

        "final_risk_score": unified[
            "final_risk_score"
        ],

        "severity": unified[
            "severity"
        ],

        "risk_score": unified["final_risk_score"],
        "risk_status": anomaly_report.get("risk_status", "NORMAL"),
        "action": anomaly_report.get("action", "UNKNOWN"),
        "location": anomaly_report.get("location", "UNKNOWN"),
        "device": anomaly_report.get("device", "UNKNOWN"),
        "file_sensitivity": anomaly_report.get("file_sensitivity", "UNKNOWN"),
        "login_hour": anomaly_report.get("login_hour"),
        "files_accessed": anomaly_report.get("files_accessed"),
        "reasons": anomaly_report.get("reasons", []),
        "scanner_findings": scanner_report.get("findings", []),

    }
