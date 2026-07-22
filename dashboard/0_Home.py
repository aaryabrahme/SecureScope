from pathlib import Path
import sys

import streamlit as st


ROOT_DIR = Path(__file__).resolve().parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.append(str(ROOT_DIR))

from dashboard.components import empty_state, metric_card, risk_table, status_badge
from dashboard.theme import page_header, premium_divider, section_header, setup_page, sidebar
from dashboard.utils import available_columns, count_severity, load_dashboard_data, score_status


setup_page()

try:
    data = load_dashboard_data()
except FileNotFoundError as error:
    sidebar()
    page_header("Security Intelligence Workspace", "Generate a unified report to begin reviewing security posture.")
    empty_state("No unified intelligence report", str(error))
    st.stop()

sidebar(data.generated_at)
page_header(
    "Executive Security Overview",
    "A consolidated view of organizational posture, data exposure, and prioritized insider-risk signals.",
    data.generated_at,
)

status, tone = score_status(data.security_score)
header, badge_column = st.columns([5, 1])
with header:
    st.caption("Current organizational posture")
with badge_column:
    status_badge(status, tone)

metrics = st.columns(4)
with metrics[0]:
    metric_card("Security score", f"{data.security_score}/100", "Unified posture assessment", tone, "POSTURE")
with metrics[1]:
    metric_card("Sensitive findings", data.summary["sensitive_findings"], "Across scanned data sources", "warning", "DATA")
with metrics[2]:
    metric_card("Anomalies", data.summary["anomalies_detected"], "Detected in analyzed events", "danger", "RISK")
with metrics[3]:
    metric_card("Priority investigations", len(data.risky_users), "Top-risk events in this report", "neutral", "QUEUE")

premium_divider()
left, right = st.columns([3, 2])
with left:
    section_header("Threat highlights", "Signals requiring the fastest security-team response.")
    critical_users = count_severity(data.risky_users, "CRITICAL")
    if critical_users or not data.critical_files.empty:
        st.error(
            f"{critical_users} critical prioritized user events and {len(data.critical_files)} critical file exposures require review."
        )
    else:
        st.success("No critical exposures are present in the current unified report.")
with right:
    section_header("Assessment scope", "What this dashboard is showing.")
    st.caption(f"{data.summary['files_scanned']} files scanned · {data.summary['events_analyzed']} events analyzed")
    st.caption("Data refreshes automatically when the unified report changes.")

premium_divider()
section_header("Quick investigation queue", "Open the Risk Explorer for full event context and rationale.")
if data.risky_users.empty:
    empty_state("No priority events", "The current unified report does not contain risky-user records.")
else:
    risk_table(data.risky_users, available_columns(data.risky_users, ["employee_id", "file_name", "action", "severity", "risk_score"]))
