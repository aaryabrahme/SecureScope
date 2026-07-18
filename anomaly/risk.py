def calculate_risk(event):

    score = 0
    reasons = []

    if event["login_hour"] < 6:
        score += 20
        reasons.append("After-hours login")

    if event["device"] == "Personal":
        score += 15
        reasons.append("Personal device")

    if event["location"] == "VPN":
        score += 15
        reasons.append("VPN access")

    if event["files_accessed"] > 100:
        score += 25
        reasons.append("High volume file access")

    if event["file_sensitivity"] == "CRITICAL":
        score += 15
        reasons.append("Critical file accessed")

    if event["risk_status"] == "ANOMALY":
        score += 30
        reasons.append("ML anomaly detected")

    score = min(score, 100)

    if score >= 80:
        severity = "CRITICAL"
    elif score >= 60:
        severity = "HIGH"
    elif score >= 40:
        severity = "MEDIUM"
    else:
        severity = "LOW"

    return {
        "risk_score": score,
        "severity": severity,
        "reasons": reasons
    }