import json

from dashboard import utils


def test_dashboard_data_parses_minimal_unified_report(tmp_path, monkeypatch):
    report_path = tmp_path / "security_report.json"
    report_path.write_text(
        json.dumps(
            {
                "generated_at": "2026-07-29 10:00:00",
                "summary": {"files_scanned": 1, "sensitive_findings": 2, "high_risk_files": 1, "events_analyzed": 3, "anomalies_detected": 1},
                "data_security": {"high_risk_files": [{"file": "sample.txt"}], "critical_files": []},
                "insider_risk": {"top_risky_users": [{"employee_id": "EMP001", "risk_score": 80}]},
                "security_score": 75,
            }
        ),
        encoding="utf-8",
    )
    monkeypatch.setattr(utils, "REPORT_PATH", report_path)
    utils._read_report.clear()

    data = utils.load_dashboard_data()

    assert data.security_score == 75
    assert data.risky_users.iloc[0]["employee_id"] == "EMP001"
