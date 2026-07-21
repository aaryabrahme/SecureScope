from core.risk_engine import create_risk_event


scanner = {
    "risk_score": 80,
    "findings": [
        "Critical file detected"
    ]
}


anomaly = {
    "risk_score": 100,
    "reasons": [
        "After-hours access",
        "VPN access"
    ]
}


result = create_risk_event(
    "EMP001",
    "salary.xlsx",
    scanner,
    anomaly,
)


print(result)