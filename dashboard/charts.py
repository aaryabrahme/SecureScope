import plotly.express as px
import plotly.graph_objects as go


# ==========================================================
# Risk Severity Distribution
# ==========================================================

def severity_chart(df):

    severity_counts = (
        df["severity"]
        .value_counts()
        .reset_index()
    )

    severity_counts.columns = [
        "Severity",
        "Count"
    ]

    fig = px.pie(
        severity_counts,
        names="Severity",
        values="Count",
        title="Risk Severity Distribution",
        hole=0.45,
    )

    fig.update_layout(
        height=400,
        margin=dict(
            l=20,
            r=20,
            t=60,
            b=20,
        ),
        legend_title="Severity",
    )

    return fig


# ==========================================================
# Normal vs Anomalous Events
# ==========================================================

def anomaly_chart(df):

    anomaly_counts = (
        df["is_anomaly"]
        .value_counts()
        .reset_index()
    )

    anomaly_counts.columns = [
        "Status",
        "Count"
    ]

    anomaly_counts["Status"] = (
        anomaly_counts["Status"]
        .map({
            0: "Normal",
            1: "Anomaly"
        })
    )

    fig = px.bar(
        anomaly_counts,
        x="Status",
        y="Count",
        title="Normal vs Anomalous Events",
        text="Count",
    )

    fig.update_layout(
        height=400,
        margin=dict(
            l=20,
            r=20,
            t=60,
            b=20,
        ),
        xaxis_title="",
        yaxis_title="Events",
    )

    fig.update_traces(
        textposition="outside"
    )

    return fig


# ==========================================================
# Risk Score Distribution
# ==========================================================

def risk_distribution(df):

    fig = px.histogram(
        df,
        x="risk_score",
        nbins=20,
        title="Risk Score Distribution",
    )

    fig.update_layout(
        height=400,
        margin=dict(
            l=20,
            r=20,
            t=60,
            b=20,
        ),
        xaxis_title="Risk Score",
        yaxis_title="Events",
    )

    return fig


# ==========================================================
# Organizational Risk Gauge
# ==========================================================

def risk_gauge(df):

    avg_risk = df["risk_score"].mean()

    anomaly_pct = (
        (df["is_anomaly"] == 1).mean() * 100
    )

    critical_pct = (
        (df["severity"] == "CRITICAL").mean() * 100
    )

    org_risk = (
        (avg_risk * 0.60)
        + (anomaly_pct * 0.30)
        + (critical_pct * 0.10)
    )

    fig = go.Figure(
        go.Indicator(
            mode="gauge+number",
            value=org_risk,
            number={
                "suffix": " / 100"
            },
            title={
                "text": "Organizational Risk Index"
            },
            gauge={
                "axis": {
                    "range": [0, 100]
                },
                "bar": {
                    "color": "#1f77b4"
                },
                "steps": [
                    {
                        "range": [0, 30],
                        "color": "#2ecc71",
                    },
                    {
                        "range": [30, 70],
                        "color": "#f1c40f",
                    },
                    {
                        "range": [70, 100],
                        "color": "#e74c3c",
                    },
                ],
                "threshold": {
                    "line": {
                        "color": "black",
                        "width": 4,
                    },
                    "value": org_risk,
                },
            },
        )
    )

    fig.update_layout(
        height=350,
        margin=dict(
            l=20,
            r=20,
            t=60,
            b=20,
        ),
    )

    return fig, org_risk


# ==========================================================
# Organizational Risk Trend
# ==========================================================

def risk_trend_chart(history_df):

    history_df = history_df.sort_values("Scan")

    fig = px.line(
        history_df,
        x="Scan",
        y="ORI",
        title="Organizational Risk Trend",
        markers=True,
    )

    fig.update_traces(
        mode="lines+markers",
        line=dict(width=3),
        marker=dict(size=8),
    )

    fig.update_layout(
        height=350,
        margin=dict(
            l=20,
            r=20,
            t=60,
            b=20,
        ),
        xaxis_title="Scan",
        yaxis_title="ORI",
        hovermode="x unified",
    )

    return fig