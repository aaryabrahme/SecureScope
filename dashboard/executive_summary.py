import random
import pandas as pd


INTRO_LOW = [
    "Security posture remains stable.",
    "Overall organizational risk is currently low.",
    "Current monitoring indicates a healthy security posture."
]

INTRO_MEDIUM = [
    "Several indicators require further investigation.",
    "Moderate insider-risk activity has been detected.",
    "Current findings suggest elevated organizational risk."
]

INTRO_HIGH = [
    "Immediate investigation is recommended.",
    "Critical security indicators have been identified.",
    "The organization is currently experiencing a high-risk security posture."
]


def generate_summary(df: pd.DataFrame):

    total_events = len(df)

    anomalies = (df["is_anomaly"] == 1).sum()

    avg_risk = df["risk_score"].mean()

    critical = (df["severity"] == "CRITICAL").sum()

    high = (df["severity"] == "HIGH").sum()

    top_action = df["action"].mode().iloc[0]

    top_location = df["location"].mode().iloc[0]

    top_device = df["device"].mode().iloc[0]

    top_employee = (
        df.sort_values(
            "risk_score",
            ascending=False
        )
        .iloc[0]["employee_id"]
    )

    # ------------------------------------
    # Determine posture
    # ------------------------------------

    if critical >= 5 or avg_risk >= 70:

        posture = "🔴 Critical"

        intro = random.choice(INTRO_HIGH)

        recommendation = (
            "Immediately investigate the highest-risk employees, "
            "validate recent privileged activity, and review all "
            "Critical severity events."
        )

    elif high >= 5 or anomalies >= 20:

        posture = "🟡 Elevated"

        intro = random.choice(INTRO_MEDIUM)

        recommendation = (
            "Prioritize investigation of High severity events and "
            "continue monitoring users exhibiting anomalous behaviour."
        )

    else:

        posture = "🟢 Healthy"

        intro = random.choice(INTRO_LOW)

        recommendation = (
            "Continue routine monitoring and periodically review "
            "high-risk accounts."
        )

    summary = f"""
### {posture}

**{intro}**

SecureScope analysed **{total_events:,} security events** and detected **{anomalies} anomalous activities**.

The **average organisational risk score** is **{avg_risk:.1f}/100**.

### Key Findings

- 👤 Highest-risk employee: **{top_employee}**
- 📂 Most common action: **{top_action}**
- 🌍 Primary location: **{top_location}**
- 💻 Most common device: **{top_device}**
- 🔴 Critical events: **{critical}**
- 🟠 High severity events: **{high}**

### Analyst Recommendation

{recommendation}
"""

    return summary