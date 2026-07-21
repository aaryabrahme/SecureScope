from typing import Any
import re

from logger import logger
from scanner.regex_patterns import PATTERNS


def detect_sensitive_data(text: str) -> list[dict[str, Any]]:
    """
    Detect sensitive information in text using predefined regex patterns.

    Returns:
        A list of findings containing:
            - type
            - value
            - risk
            - reason (optional)
    """

    if not text.strip():
        return []

    findings: list[dict[str, Any]] = []

    for data_type, details in PATTERNS.items():

        try:
            matches = details["regex"].findall(text)

        except Exception as error:
            logger.error(
                "Regex error for %s: %s",
                data_type,
                error
            )
            continue

        for match in matches:

            value = match[-1] if isinstance(match, tuple) else match

            finding = {
                "type": data_type,
                "value": value,
                "risk": details["risk"],
            }

            reason = details.get("reason")

            if reason:
                finding["reason"] = reason

            findings.append(finding)

    return findings
