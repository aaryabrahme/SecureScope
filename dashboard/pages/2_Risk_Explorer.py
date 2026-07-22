import streamlit as st

from components import empty_state, risk_table, status_badge
from theme import page_header, premium_divider, section_header, setup_page, sidebar
from utils import available_columns, load_dashboard_data


def format_reasons(reasons) -> list[str]:
    if isinstance(reasons, list):
        return [str(reason) for reason in reasons]
    if isinstance(reasons, str) and reasons.strip():
        return [reasons]
    return ["No rationale was included in the unified report."]


setup_page()

try:
    data = load_dashboard_data()
except FileNotFoundError as error:
    sidebar()
    empty_state("No unified intelligence report", str(error))
    st.stop()

sidebar(data.generated_at, active_page="Risk Explorer")
page_header(
    "Priority Investigations",
    "Filter and investigate the highest-risk insider events supplied by the current unified report.",
    data.generated_at,
)

events = data.risky_users.copy()
if events.empty:
    empty_state("No priority events", "The current unified report does not contain risky-user records.")
    st.stop()

section_header("Investigation queue", "Use filters to narrow the report's prioritized insider-risk events.")
filter_columns = st.columns(3)
with filter_columns[0]:
    severities = sorted(events["severity"].dropna().unique()) if "severity" in events else []
    selected_severities = st.multiselect("Severity", severities, default=severities)
with filter_columns[1]:
    actions = sorted(events["action"].dropna().unique()) if "action" in events else []
    selected_actions = st.multiselect("Action", actions, default=actions)
with filter_columns[2]:
    locations = sorted(events["location"].dropna().unique()) if "location" in events else []
    selected_locations = st.multiselect("Location", locations, default=locations)

if "severity" in events:
    events = events[events["severity"].isin(selected_severities)]
if "action" in events:
    events = events[events["action"].isin(selected_actions)]
if "location" in events:
    events = events[events["location"].isin(selected_locations)]

if events.empty:
    empty_state("No matching events", "Change or clear the filters to restore the investigation queue.")
    st.stop()

risk_table(events, available_columns(events, ["employee_id", "file_name", "action", "location", "severity", "risk_score"]))

premium_divider()
section_header("Investigation workspace", "Event facts and risk rationale from the unified report.")
event_labels = events.apply(
    lambda row: f"{row.get('employee_id', 'Unknown')} | {row.get('file_name', 'Unknown file')} | {row.get('risk_score', 0)}/100",
    axis=1,
)
selected_index = st.selectbox("Select event", event_labels.index, format_func=event_labels.get)
event = events.loc[selected_index]

overview, context = st.columns([2, 3])
with overview:
    status_badge(str(event.get("severity", "Unknown")), str(event.get("severity", "")).lower())
    st.metric("Risk score", f"{event.get('risk_score', 0)}/100")
    st.progress(min(max(float(event.get("risk_score", 0)) / 100, 0), 1))
with context:
    detail_columns = st.columns(2)
    with detail_columns[0]:
        st.caption("Activity context")
        st.write(f"Employee: {event.get('employee_id', 'Unknown')}")
        st.write(f"Action: {event.get('action', 'Unknown')}")
        st.write(f"File: {event.get('file_name', 'Unknown')}")
    with detail_columns[1]:
        st.caption("Access context")
        st.write(f"Location: {event.get('location', 'Unknown')}")
        st.write(f"Device: {event.get('device', 'Unknown')}")
        st.write(f"Sensitivity: {event.get('file_sensitivity', 'Unknown')}")

premium_divider()
section_header("Risk rationale", "Signals included by the insider-risk analysis.")
for reason in format_reasons(event.get("reasons")):
    st.write(f"• {reason}")

st.info("Recommended workflow: validate the activity against access policy, review supporting audit logs, and record the disposition in your case-management process.")
