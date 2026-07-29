from core.risk_engine import calculate_unified_risk, create_risk_event


def test_unified_risk_weights_behavior_more_than_scanner_risk():
    assert calculate_unified_risk(80, 100)["final_risk_score"] == 92


def test_risk_event_preserves_activity_context():
    event = create_risk_event(
        "EMP001",
        "salary.xlsx",
        {"risk_score": 80, "findings": []},
        {"risk_score": 100, "action": "DOWNLOAD", "location": "VPN", "device": "Personal", "file_sensitivity": "CRITICAL", "risk_status": "ANOMALY", "reasons": ["VPN access"]},
    )
    assert event["risk_score"] == 92
    assert event["risk_status"] == "ANOMALY"
    assert event["device"] == "Personal"
