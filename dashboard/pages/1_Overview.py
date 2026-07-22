import streamlit as st

from charts import anomaly_distribution_chart, risk_distribution_chart, risk_trend_chart, security_score_gauge, severity_chart
from components import empty_state, metric_card, risk_table, status_badge
from theme import page_header, premium_divider, section_header, setup_page, sidebar
from utils import available_columns, count_severity, executive_recommendations, load_dashboard_data, score_status


setup_page()

try:
    data = load_dashboard_data()
except FileNotFoundError as error:
    sidebar()
    empty_state("No unified intelligence report", str(error))
    st.stop()

sidebar(data.generated_at, active_page="Security Posture")
page_header(
    "Security Command Center",
    "Enterprise posture analytics and prioritized security intelligence from the latest unified assessment.",
    data.generated_at,
)

status, tone = score_status(data.security_score)

section_header("Security posture", "The unified report's authoritative organizational security score.")
left, right = st.columns([3, 2])
with left:
    st.plotly_chart(security_score_gauge(data.security_score), use_container_width=True)
with right:
    status_badge(status, tone)
    st.markdown("#### Organizational risk index")
    st.write(f"{100 - data.security_score}/100 risk exposure")
    st.caption("Risk exposure is displayed as the inverse of the report's security score; it is not a separate backend calculation.")

premium_divider()
section_header("Data security intelligence", "Exposure signals from the scanner portion of the unified report.")
metrics = st.columns(4)
with metrics[0]:
    metric_card("Files scanned", data.summary["files_scanned"], "Data sources assessed", "neutral", "SCAN")
with metrics[1]:
    metric_card("Sensitive findings", data.summary["sensitive_findings"], "PII and secrets detected", "warning", "FIND")
with metrics[2]:
    metric_card("High-risk files", data.summary["high_risk_files"], "Require exposure review", "danger", "FILE")
with metrics[3]:
    metric_card("Critical exposures", len(data.critical_files), "Files with critical findings", "danger", "CRIT")

premium_divider()
section_header("Insider threat intelligence", "Prioritized event intelligence supplied by the unified report.")
metrics = st.columns(4)
with metrics[0]:
    metric_card("Events analyzed", data.summary["events_analyzed"], "Activity records assessed", "neutral", "EVENT")
with metrics[1]:
    metric_card("Anomalies detected", data.summary["anomalies_detected"], "Across all analyzed activity", "danger", "ANOM")
with metrics[2]:
    metric_card("Top risky users", len(data.risky_users), "Included in the investigation queue", "warning", "USER")
with metrics[3]:
    metric_card("Critical users", count_severity(data.risky_users, "CRITICAL"), "In the priority event list", "danger", "HIGH")

premium_divider()
section_header("Threat analytics", "Charts describe the priority-event list included in this unified-report snapshot.")
row_one = st.columns(2)
with row_one[0]:
    st.plotly_chart(severity_chart(data.risky_users), use_container_width=True)
with row_one[1]:
    st.plotly_chart(risk_distribution_chart(data.risky_users), use_container_width=True)

row_two = st.columns(2)
with row_two[0]:
    st.plotly_chart(anomaly_distribution_chart(data.risky_users), use_container_width=True)
with row_two[1]:
    if data.risk_trend.empty:
        empty_state("Risk trend unavailable", "The current unified report is a snapshot. Add a risk_trend field to future reports to enable longitudinal posture analytics.")
    else:
        st.plotly_chart(risk_trend_chart(data.risk_trend), use_container_width=True)

premium_divider()
section_header("Executive recommendations", "Action-oriented guidance based on the report's current posture and findings.")
for recommendation in executive_recommendations(data):
    st.write(f"• {recommendation}")

premium_divider()
section_header("Priority users", "Highest-risk events available for immediate investigation.")
if data.risky_users.empty:
    empty_state("No priority users", "No risky-user records were included in the current unified report.")
else:
    risk_table(data.risky_users, available_columns(data.risky_users, ["employee_id", "file_name", "action", "severity", "risk_score", "reasons"]))
