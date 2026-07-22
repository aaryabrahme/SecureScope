import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


BACKGROUND = "rgba(0,0,0,0)"
TEXT = "#e5edf7"
GRID = "#29435f"
SEVERITY_COLORS = {
    "LOW": "#33b679",
    "MEDIUM": "#f6c85f",
    "HIGH": "#f28e2b",
    "CRITICAL": "#e15759",
}


def apply_chart_theme(figure: go.Figure) -> go.Figure:
    figure.update_layout(
        paper_bgcolor=BACKGROUND,
        plot_bgcolor=BACKGROUND,
        font={"color": TEXT, "family": "Inter, Segoe UI, sans-serif"},
        margin={"l": 12, "r": 12, "t": 48, "b": 12},
        height=330,
        legend={"orientation": "h", "y": 1.12, "x": 1, "xanchor": "right"},
    )
    figure.update_xaxes(showgrid=False, linecolor=GRID)
    figure.update_yaxes(gridcolor=GRID)
    return figure


def security_score_gauge(score: int) -> go.Figure:
    figure = go.Figure(
        go.Indicator(
            mode="gauge+number",
            value=score,
            number={"suffix": "/100", "font": {"size": 42}},
            title={"text": "Security score"},
            gauge={
                "axis": {"range": [0, 100]},
                "bar": {"color": "#50b9c5"},
                "steps": [
                    {"range": [0, 40], "color": "#572c38"},
                    {"range": [40, 70], "color": "#5c4b27"},
                    {"range": [70, 100], "color": "#174a46"},
                ],
            },
        )
    )
    return apply_chart_theme(figure)


def severity_chart(events: pd.DataFrame) -> go.Figure:
    if events.empty or "severity" not in events:
        return go.Figure()

    counts = events["severity"].value_counts().rename_axis("severity").reset_index(name="events")
    figure = px.bar(
        counts,
        x="severity",
        y="events",
        color="severity",
        text="events",
        color_discrete_map=SEVERITY_COLORS,
        category_orders={"severity": ["CRITICAL", "HIGH", "MEDIUM", "LOW"]},
    )
    figure.update_traces(textposition="outside")
    return apply_chart_theme(figure)


def risk_distribution_chart(events: pd.DataFrame) -> go.Figure:
    if events.empty or "risk_score" not in events:
        return go.Figure()

    figure = px.histogram(
        events,
        x="risk_score",
        nbins=10,
        color_discrete_sequence=["#50b9c5"],
    )
    figure.update_layout(xaxis_title="Risk score", yaxis_title="Priority events")
    return apply_chart_theme(figure)


def anomaly_distribution_chart(events: pd.DataFrame) -> go.Figure:
    if events.empty or "is_anomaly" not in events:
        return go.Figure()

    labels = events["is_anomaly"].map({1: "Anomaly", 0: "Expected"}).fillna("Unknown")
    counts = labels.value_counts().rename_axis("status").reset_index(name="events")
    figure = px.pie(
        counts,
        names="status",
        values="events",
        hole=0.62,
        color="status",
        color_discrete_map={"Anomaly": "#ef6b73", "Expected": "#50c8a7", "Unknown": "#8fa9c6"},
    )
    figure.update_traces(textinfo="percent")
    return apply_chart_theme(figure)


def risk_trend_chart(trend: pd.DataFrame) -> go.Figure:
    if trend.empty or not {"timestamp", "security_score"}.issubset(trend.columns):
        return go.Figure()

    figure = px.line(trend, x="timestamp", y="security_score", markers=True)
    figure.update_traces(line={"color": "#50b9c5", "width": 3})
    figure.update_layout(xaxis_title="Assessment", yaxis_title="Security score")
    return apply_chart_theme(figure)
