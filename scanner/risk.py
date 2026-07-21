from typing import Any

from constants import (
    RISK_WEIGHTS,
    CRITICAL_THRESHOLD,
    HIGH_THRESHOLD,
    MEDIUM_THRESHOLD,
    LOW,
    MEDIUM,
    HIGH,
    CRITICAL,
)


def calculate_risk(
    findings: list[dict[str, Any]]
) -> tuple[int, str]:
    """
    Calculate the cumulative risk score for a file.

    Each finding contributes a weighted score based on
    its assigned risk category.

    The final score is capped at 100 and mapped to
    an overall severity level.

    Returns:
        Tuple containing:
        (risk_score, risk_level)
    """

    score = 0

    for finding in findings:
        risk = finding.get("risk")
        score += RISK_WEIGHTS.get(risk, 0)

    score = min(score, 100)

    if score >= CRITICAL_THRESHOLD:
        level = CRITICAL

    elif score >= HIGH_THRESHOLD:
        level = HIGH

    elif score >= MEDIUM_THRESHOLD:
        level = MEDIUM

    else:
        level = LOW

    return score, level