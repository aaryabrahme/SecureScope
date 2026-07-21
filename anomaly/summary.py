import pandas as pd


def generate_summary(
    df: pd.DataFrame,
) -> dict:
    """
    Generate anomaly detection summary statistics.

    Args:
        df:
            DataFrame containing anomaly results.

    Returns:
        Dictionary containing dashboard metrics.
    """

    total_events = len(df)

    normal_events = (
        df["risk_status"] == "NORMAL"
    ).sum()

    anomaly_events = (
        df["risk_status"] == "ANOMALY"
    ).sum()

    average_risk = (
        round(
            df["risk_score"].mean(),
            2
        )
        if not df.empty
        else 0
    )

    highest_risk = (
        df["risk_score"].max()
        if not df.empty
        else 0
    )

    severity_counts = (
        df["severity"]
        .value_counts()
        .to_dict()
    )

    high_risk_events = (
        df["severity"] == "HIGH"
    ).sum()

    critical_events = (
        df["severity"] == "CRITICAL"
    ).sum()


    return {

        "total_events": int(total_events),

        "normal_events": int(normal_events),

        "anomaly_events": int(anomaly_events),

        "average_risk": average_risk,

        "highest_risk": int(highest_risk),

        "high_risk_events": int(high_risk_events),

        "critical_events": int(critical_events),

        "severity_counts": severity_counts,

    }
