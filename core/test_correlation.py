from core.correlation import correlate_reports


def test_correlation_supports_scanner_file_compatibility_alias(tmp_path):
    scanner_path = tmp_path / "scanner.json"
    anomaly_path = tmp_path / "anomaly.json"
    scanner_path.write_text(
        '[{"file": "salary.xlsx", "risk_score": 80, "findings": [{"risk": "CRITICAL"}]}]',
        encoding="utf-8",
    )
    anomaly_path.write_text(
        '[{"employee_id": "EMP001", "file_name": "salary.xlsx", "risk_score": 90, "risk_status": "ANOMALY", "action": "DOWNLOAD", "location": "VPN", "device": "Personal", "file_sensitivity": "CRITICAL", "reasons": "After-hours login, ML anomaly detected"}]',
        encoding="utf-8",
    )

    event = correlate_reports(scanner_path, anomaly_path)[0]

    assert event["scanner_risk_score"] == 80
    assert event["anomaly_risk_score"] == 90
    assert event["action"] == "DOWNLOAD"
    assert event["reasons"] == ["After-hours login", "ML anomaly detected"]
