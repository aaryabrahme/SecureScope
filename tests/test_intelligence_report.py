import json

from intelligence.aggregator import create_security_report


def test_unified_report_uses_correlated_event_context(tmp_path):
    scanner_path = tmp_path / "scanner.json"
    anomaly_path = tmp_path / "anomaly.json"
    events_path = tmp_path / "events.json"
    output_path = tmp_path / "security_report.json"
    scanner_path.write_text('[{"file": "salary.txt", "risk_score": 60, "risk_level": "HIGH", "findings": [{"risk": "CRITICAL"}]}]', encoding="utf-8")
    anomaly_path.write_text('[{"employee_id": "EMP001"}]', encoding="utf-8")
    events_path.write_text('[{"employee_id": "EMP001", "risk_score": 92, "risk_status": "ANOMALY", "action": "DOWNLOAD", "scanner_risk_score": 60, "anomaly_risk_score": 100}]', encoding="utf-8")

    create_security_report(scanner_path, anomaly_path, events_path, output_path)
    report = json.loads(output_path.read_text(encoding="utf-8"))

    assert report["summary"]["anomalies_detected"] == 1
    assert report["data_security"]["critical_files"][0]["file"] == "salary.txt"
    assert report["insider_risk"]["top_risky_users"][0]["scanner_risk_score"] == 60
    assert report["security_score"] == 95
