import pandas as pd

def generate_summary(df):

    total_events = len(df)

    normal_events = (df["risk_status"] == "NORMAL").sum()

    anomaly_events = (df["risk_status"] == "ANOMALY").sum()

    average_risk = round(df["risk_score"].mean(), 2)

    highest_risk = df["risk_score"].max()

    severity_counts = df["severity"].value_counts()

    return {

    "total_events": total_events,

    "normal_events": normal_events,

    "anomaly_events": anomaly_events,

    "average_risk": average_risk,

    "highest_risk": highest_risk,

    "severity_counts": severity_counts.to_dict()

    }