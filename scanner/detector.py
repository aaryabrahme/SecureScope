import re

from scanner.regex_patterns import PATTERNS


def detect_sensitive_data(text: str):

    findings = []

    for data_type, details in PATTERNS.items():

        matches = re.findall(details["regex"], text)

        for match in matches:

            # Handle regex capture groups
            if isinstance(match, tuple):
                value = match[-1]
            else:
                value = match

            finding = {

                "type": data_type,

                "value": value,

                "risk": details["risk"]

            }

            if "reason" in details:
                finding["reason"] = details["reason"]


            findings.append(finding)

    return findings