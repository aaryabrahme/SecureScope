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
    Calculate risk score based on finding severity.

    Each finding contributes according to its severity.
    """

    score = 0

    for finding in findings:

        risk = finding.get("risk")

        print(
            "DEBUG RISK:",
            risk,
            "WEIGHT:",
            RISK_WEIGHTS.get(risk)
        )

        score += RISK_WEIGHTS.get(
            risk,
            0
        )

    if score >= CRITICAL_THRESHOLD:
        level = CRITICAL

    elif score >= HIGH_THRESHOLD:
        level = HIGH

    elif score >= MEDIUM_THRESHOLD:
        level = MEDIUM

    else:
        level = LOW


    return score, level