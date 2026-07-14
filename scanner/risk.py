RISK_WEIGHTS = {
    "Low": 10,
    "Medium": 20,
    "High": 40,
    "Critical": 60
}


def calculate_risk(findings):
    """
    Calculate the overall risk score for a file.
    """

    score = 0

    for finding in findings:
        score += RISK_WEIGHTS.get(finding["risk"], 0)

    # Keep score between 0 and 100
    score = min(score, 100)

    if score >= 80:
        level = "CRITICAL"
    elif score >= 50:
        level = "HIGH"
    elif score >= 20:
        level = "MEDIUM"
    else:
        level = "LOW"

    return score, level