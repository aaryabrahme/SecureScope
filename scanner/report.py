from pathlib import Path
from typing import Any

from logging_config import setup_logging

from scanner.detector import detect_sensitive_data
from scanner.readers import read_file
from scanner.risk import calculate_risk
from scanner.secret_detector import detect_high_entropy_strings

logger = setup_logging()


def scan_file(file_path: Path) -> dict[str, Any]:
    """
    Scan a single file for sensitive information and secrets.

    The scan performs:
        1. File reading
        2. Regex-based detection
        3. High-entropy secret detection
        4. Risk calculation

    Returns:
        Dictionary containing scan results.
    """

    logger.info("Scanning file: %s", file_path.name)

    file_text = read_file(file_path)

    if not file_text:
        return {
            "file": file_path.name,
            "path": str(file_path),
            "findings": [],
            "risk_score": 0,
            "risk_level": "LOW",
        }

    findings = detect_sensitive_data(file_text)

    filtered_text = file_text

    for finding in findings:
        value = finding.get("value")

        if value:
            filtered_text = filtered_text.replace(value, "")

    secret_findings = detect_high_entropy_strings(filtered_text)

    findings.extend(secret_findings)

    score, level = calculate_risk(findings)

    logger.info(
        "Completed scan for %s | Findings: %d | Score: %d",
        file_path.name,
        len(findings),
        score,
    )

    return {
        "file": file_path.name,
        "path": str(file_path),
        "findings": findings,
        "risk_score": score,
        "risk_level": level,
    }