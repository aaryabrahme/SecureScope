import json

import streamlit as st

from components import empty_state, metric_card, risk_table, status_badge
from theme import page_header, premium_divider, section_header, setup_page, sidebar
from utils import available_columns, load_dashboard_data, score_status


setup_page()

try:
    data = load_dashboard_data()
except FileNotFoundError as error:
    sidebar()
    empty_state("No unified intelligence report", str(error))
    st.stop()

sidebar(data.generated_at)
page_header(
    "Unified Security Report",
    "Review scanner and insider-risk findings, then export the current enterprise assessment.",
    data.generated_at,
)

status, tone = score_status(data.security_score)
summary, badge = st.columns([5, 1])
with summary:
    st.caption("Unified assessment status")
with badge:
    status_badge(status, tone)

metrics = st.columns(4)
with metrics[0]:
    metric_card("Security score", f"{data.security_score}/100", "Unified posture assessment", tone, "POSTURE")
with metrics[1]:
    metric_card("Events analyzed", data.summary["events_analyzed"], "Activity data assessed", "neutral", "EVENT")
with metrics[2]:
    metric_card("High-risk files", data.summary["high_risk_files"], "Scanner findings requiring review", "warning", "FILES")
with metrics[3]:
    metric_card("Critical exposures", len(data.critical_files), "Files containing critical findings", "danger", "CRIT")

premium_divider()
section_header("Data security findings", "High-risk and critical files identified by the scanner.")
if data.high_risk_files.empty:
    empty_state("No high-risk files", "No file exposures are present in this unified report.")
else:
    risk_table(data.high_risk_files, available_columns(data.high_risk_files, ["file", "path", "risk_level", "risk_score", "findings"]))

premium_divider()
section_header("Priority insider-risk events", "Highest-risk events included in the current report.")
if data.risky_users.empty:
    empty_state("No priority events", "No insider-risk events are present in this unified report.")
else:
    risk_table(data.risky_users, available_columns(data.risky_users, ["employee_id", "file_name", "action", "severity", "risk_score", "reasons"]))

premium_divider()
section_header("Export assessment", "Downloads contain the current report without changing scanner or ML results.")
left, right = st.columns(2)
with left:
    st.download_button(
        "Download unified JSON",
        json.dumps(data.report, indent=2),
        file_name="securescope_security_report.json",
        mime="application/json",
        use_container_width=True,
    )
with right:
    st.download_button(
        "Download priority events CSV",
        data.risky_users.to_csv(index=False),
        file_name="securescope_priority_events.csv",
        mime="text/csv",
        use_container_width=True,
    )
