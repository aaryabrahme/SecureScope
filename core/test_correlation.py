from core.correlation import (
    correlate_reports,
    save_final_report
)


scanner_report = [
    {
        "file_name": "salary.xlsx",
        "risk_score": 80,
        "findings": [
            "Critical file detected"
        ]
    }
]


anomaly_report = [
    {
        "employee_id": "EMP001",
        "file_name": "salary.xlsx",
        "risk_score": 100,
        "reasons": [
            "VPN access",
            "After-hours login"
        ]
    }
]


import json


with open(
    "reports/test_scanner.json",
    "w"
) as f:
    json.dump(
        scanner_report,
        f,
        indent=4
    )


with open(
    "reports/test_anomaly.json",
    "w"
) as f:
    json.dump(
        anomaly_report,
        f,
        indent=4
    )



events = correlate_reports(
    "reports/test_scanner.json",
    "reports/test_anomaly.json"
)


path = save_final_report(
    events
)


print(events)

print(
    "Saved:",
    path
)