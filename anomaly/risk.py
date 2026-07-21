from typing import Any

from constants import (
    AFTER_HOURS_SCORE,
    CRITICAL,
    CRITICAL_FILE_SCORE,
    CRITICAL_THRESHOLD,
    HIGH,
    HIGH_THRESHOLD,
    HIGH_VOLUME_ACCESS_SCORE,
    LOW,
    ML_ANOMALY_SCORE,
    MEDIUM,
    MEDIUM_THRESHOLD,
    PERSONAL_DEVICE_SCORE,
    VPN_SCORE,
)


def calculate_risk(
    event: dict[str, Any],
) -> dict[str, Any]:
    """
    Calculate business risk score for an access event.

    Combines:
        - User behavior signals
        - Data sensitivity
        - ML anomaly prediction

    Returns:
        Risk score, severity, and explanation reasons.
    """

    score = 0
    reasons = []

    if event.get("login_hour", 24) < 6:
        score += AFTER_HOURS_SCORE
        reasons.append("After-hours login")

    if event.get("device") == "Personal":
        score += PERSONAL_DEVICE_SCORE
        reasons.append("Personal device")

    if event.get("location") == "VPN":
        score += VPN_SCORE
        reasons.append("VPN access")

    if event.get("files_accessed", 0) > 100:
        score += HIGH_VOLUME_ACCESS_SCORE
        reasons.append("High volume file access")

    if event.get("file_sensitivity") == "CRITICAL":
        score += CRITICAL_FILE_SCORE
        reasons.append("Critical file accessed")

    if event.get("risk_status") == "ANOMALY":
        score += ML_ANOMALY_SCORE
        reasons.append("ML anomaly detected")

    score = min(score, 100)


    if score >= CRITICAL_THRESHOLD:
        severity = CRITICAL

    elif score >= HIGH_THRESHOLD:
        severity = HIGH

    elif score >= MEDIUM_THRESHOLD:
        severity = MEDIUM

    else:
        severity = LOW


    return {
        "risk_score": score,
        "severity": severity,
        "reasons": reasons,
        "risk_factors": len(reasons),
    }
