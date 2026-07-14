from pathlib import Path

from docx import text

from scanner.readers import read_file
from scanner.detector import detect_sensitive_data
from scanner.risk import calculate_risk
from scanner.secret_detector import detect_high_entropy_strings

def scan_file(file_path: Path):

    text = read_file(file_path)

    findings = detect_sensitive_data(text)

    filtered_text = text

    for finding in findings:
        filtered_text = filtered_text.replace(
            finding["value"],
            ""
        )


    secret_findings = detect_high_entropy_strings(filtered_text)

    findings.extend(secret_findings)

    score, level = calculate_risk(findings)

    return {
        "file": file_path.name,
        "path": str(file_path),
        "findings": findings,
        "risk_score": score,
        "risk_level": level
    }