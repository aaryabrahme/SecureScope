import re

from scanner.regex_patterns import PATTERNS


def detect_sensitive_data(text: str):

    findings = []

    for data_type, details in PATTERNS.items():

        matches = re.findall(details["regex"], text)

        for match in matches:

            findings.append({

                "type": data_type,

                "value": match,

                "risk": details["risk"]

            })

    return findings