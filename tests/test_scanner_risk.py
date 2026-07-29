from scanner.risk import calculate_risk


def test_scanner_risk_score_and_severity_are_deterministic():
    score, severity = calculate_risk([{"risk": "CRITICAL"}, {"risk": "MEDIUM"}])
    assert score == 75
    assert severity == "HIGH"


def test_scanner_risk_ignores_unknown_finding_labels():
    assert calculate_risk([{"risk": "UNKNOWN"}]) == (0, "LOW")
