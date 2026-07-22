from html import escape

import pandas as pd
import streamlit as st


STATUS_COLORS = {
    "success": "#50c8a7",
    "warning": "#f2bc5f",
    "danger": "#ef6b73",
    "error": "#ef6b73",
    "critical": "#ef6b73",
    "high": "#f2bc5f",
    "medium": "#f2bc5f",
    "low": "#50c8a7",
    "neutral": "#8fa9c6",
}


def metric_card(label: str, value: str | int, detail: str, tone: str = "neutral", icon: str = ""):
    color = STATUS_COLORS.get(tone, STATUS_COLORS["neutral"])
    st.markdown(
        f"""
        <div class="metric-card">
            <div class="metric-card-label">{escape(icon)} {escape(label)}</div>
            <div class="metric-card-value" style="color:{color}">{escape(str(value))}</div>
            <div class="metric-card-detail">{escape(detail)}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def status_badge(label: str, tone: str = "neutral"):
    color = STATUS_COLORS.get(tone, STATUS_COLORS["neutral"])
    st.markdown(
        f'<span class="status-badge" style="border-color:{color}; color:{color}">{escape(label)}</span>',
        unsafe_allow_html=True,
    )


def empty_state(title: str, message: str):
    st.markdown(
        f"""
        <div class="empty-state">
            <div class="empty-state-title">{escape(title)}</div>
            <div>{escape(message)}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def risk_table(dataframe: pd.DataFrame, columns: list[str]):
    visible_columns = [column for column in columns if column in dataframe.columns]
    if not visible_columns:
        return

    column_config = {}
    if "risk_score" in visible_columns:
        column_config["risk_score"] = st.column_config.ProgressColumn(
            "Risk score",
            min_value=0,
            max_value=100,
            format="%d",
        )

    st.dataframe(
        dataframe[visible_columns],
        use_container_width=True,
        hide_index=True,
        column_config=column_config,
    )
