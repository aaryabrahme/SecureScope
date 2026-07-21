import plotly.express as px
import plotly.graph_objects as go


# ==========================================================
# GLOBAL CHART THEME
# ==========================================================

PRIMARY = "#2563EB"
SUCCESS = "#22C55E"
WARNING = "#F59E0B"
DANGER = "#EF4444"
BACKGROUND = "rgba(0,0,0,0)"
GRID = "#E5E7EB"
TEXT = "#111827"


def apply_chart_theme(fig):

    fig.update_layout(

        paper_bgcolor=BACKGROUND,
        plot_bgcolor=BACKGROUND,

        font=dict(
            family="Inter, Segoe UI, sans-serif",
            color=TEXT,
            size=14,
        ),

        title=dict(
            x=0,
            font=dict(
                size=22,
                color=TEXT,
            ),
        ),

        margin=dict(
            l=20,
            r=20,
            t=60,
            b=20,
        ),

        legend=dict(
            orientation="h",
            y=1.08,
            x=1,
            xanchor="right",
            bgcolor="rgba(0,0,0,0)",
        ),

        hoverlabel=dict(
            bgcolor="white",
            font_size=14,
        ),

        height=360,
    )

    fig.update_xaxes(

        showgrid=False,
        zeroline=False,
        linecolor=GRID,
    )

    fig.update_yaxes(

        gridcolor=GRID,
        zeroline=False,
    )

    return fig


# ==========================================================
# SEVERITY PIE
# ==========================================================

def severity_chart(df):

    severity_counts = (
        df["severity"]
        .value_counts()
        .reset_index()
    )

    severity_counts.columns = [
        "Severity",
        "Count",
    ]

    fig = px.pie(

        severity_counts,

        names="Severity",

        values="Count",

        hole=0.60,

        color="Severity",

        color_discrete_map={
            "LOW": SUCCESS,
            "MEDIUM": WARNING,
            "HIGH": "#FB923C",
            "CRITICAL": DANGER,
        },
    )

    fig.update_traces(

        textinfo="percent",

        textfont_size=15,

        marker=dict(
            line=dict(
                color="white",
                width=2,
            )
        ),
    )

    return apply_chart_theme(fig)


# ==========================================================
# ANOMALY BAR
# ==========================================================

def anomaly_chart(df):

    anomaly_counts = (
        df["is_anomaly"]
        .value_counts()
        .reset_index()
    )

    anomaly_counts.columns = [
        "Status",
        "Count",
    ]

    anomaly_counts["Status"] = (
        anomaly_counts["Status"]
        .map(
            {
                0: "Normal",
                1: "Anomaly",
            }
        )
    )

    fig = px.bar(

        anomaly_counts,

        x="Status",

        y="Count",

        color="Status",

        text="Count",

        color_discrete_map={
            "Normal": PRIMARY,
            "Anomaly": DANGER,
        },
    )

    fig.update_traces(

        textposition="outside",

        marker_line_width=0,
    )

    return apply_chart_theme(fig)


# ==========================================================
# RISK DISTRIBUTION
# ==========================================================

def risk_distribution(df):

    fig = px.histogram(

        df,

        x="risk_score",

        nbins=20,

        color_discrete_sequence=[PRIMARY],
    )

    fig.update_traces(

        marker_line_width=0,
    )

    return apply_chart_theme(fig)


# ==========================================================
# ORGANIZATIONAL RISK
# ==========================================================

def risk_gauge(df):

    avg_risk = df["risk_score"].mean()

    anomaly_pct = (
        (df["is_anomaly"] == 1).mean()
        * 100
    )

    critical_pct = (
        (df["severity"] == "CRITICAL").mean()
        * 100
    )

    org_risk = (

        avg_risk * 0.60

        + anomaly_pct * 0.30

        + critical_pct * 0.10

    )

    fig = go.Figure(

        go.Indicator(

            mode="gauge+number",

            value=org_risk,

            number={
                "suffix": "/100",
                "font": {"size": 42},
            },

            title={
                "text": "Organizational Risk Index"
            },

            gauge={

                "axis": {
                    "range": [0, 100]
                },

                "bar": {
                    "color": PRIMARY
                },

                "steps": [

                    {
                        "range": [0, 30],
                        "color": "#DCFCE7",
                    },

                    {
                        "range": [30, 70],
                        "color": "#FEF3C7",
                    },

                    {
                        "range": [70, 100],
                        "color": "#FEE2E2",
                    },
                ],

                "threshold": {

                    "line": {
                        "color": "#111827",
                        "width": 4,
                    },

                    "value": org_risk,
                },
            },
        )
    )

    fig.update_layout(

        height=360,

        paper_bgcolor=BACKGROUND,
    )

    return fig, round(org_risk, 1)


# ==========================================================
# RISK TREND
# ==========================================================

def risk_trend_chart(history_df):

    history_df = history_df.sort_values(
        "Scan"
    )

    fig = px.line(

        history_df,

        x="Scan",

        y="ORI",

        markers=True,
    )

    fig.update_traces(

        mode="lines+markers",

        line=dict(
            width=4,
            color=PRIMARY,
        ),

        marker=dict(
            size=9,
        ),
    )

    return apply_chart_theme(fig)