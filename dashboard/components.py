import streamlit as st
import pandas as pd


# ==========================================================
# PREMIUM UI COMPONENTS
# ==========================================================

def section_header(title, subtitle=""):

    st.markdown(
        f"""
        <div style="margin-bottom:1rem;">
            <div style="font-size:2rem;font-weight:700;color:#111827;">
                {title}
            </div>
            <div style="color:#6B7280;font-size:1rem;margin-top:0.25rem;">
                {subtitle}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


def metric_card(icon, value, label, color="#2563EB"):

    st.markdown(
        f"""
        <div style="
            background:#FFFFFF;
            border:1px solid #E5E7EB;
            border-radius:20px;
            padding:1.5rem;
            box-shadow:0 8px 24px rgba(15,23,42,0.06);
            min-height:170px;
            display:flex;
            flex-direction:column;
            justify-content:space-between;
        ">

            <div style="font-size:2rem;">{icon}</div>

            <div style="
                font-size:2.6rem;
                font-weight:700;
                color:{color};
                line-height:1;
                margin:0.75rem 0;
            ">
                {value}
            </div>

            <div style="
                color:#6B7280;
                font-size:0.95rem;
                font-weight:600;
            ">
                {label}
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )


def info_card(title, content):

    st.markdown(
        f"""
        <div style="
            background:#FFFFFF;
            border:1px solid #E5E7EB;
            border-radius:20px;
            padding:1.75rem;
            box-shadow:0 8px 24px rgba(15,23,42,0.06);
        ">

            <div style="
                font-size:1.15rem;
                font-weight:700;
                margin-bottom:1rem;
                color:#111827;
            ">
                {title}
            </div>

            <div style="
                color:#374151;
                line-height:1.7;
                font-size:1rem;
            ">
                {content}
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )


# ==========================================================
# DASHBOARD METRICS
# ==========================================================

def display_metrics(df):

    total_events = len(df)

    anomalies = int((df["is_anomaly"] == 1).sum())

    avg_risk = round(df["risk_score"].mean(), 1)

    highest_risk = int(df["risk_score"].max())

    section_header(
        "📈 Key Risk Metrics",
        "Live organizational risk indicators from the latest security assessment."
    )

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        metric_card("📄", f"{total_events:,}", "Total Events")

    with col2:
        metric_card("🚨", anomalies, "Anomalies", "#DC2626")

    with col3:
        metric_card("📈", avg_risk, "Average Risk", "#2563EB")

    with col4:
        metric_card("🔥", highest_risk, "Highest Risk", "#EA580C")


# ==========================================================
# FILTERS
# ==========================================================

def risk_filters(df):

    st.sidebar.markdown("### 🔍 Filters")

    severity = st.sidebar.multiselect(
        "Severity",
        options=sorted(df["severity"].unique()),
        default=list(sorted(df["severity"].unique()))
    )

    action = st.sidebar.multiselect(
        "Action",
        options=sorted(df["action"].unique()),
        default=list(sorted(df["action"].unique()))
    )

    location = st.sidebar.multiselect(
        "Location",
        options=sorted(df["location"].unique()),
        default=list(sorted(df["location"].unique()))
    )

    filtered_df = df[
        (df["severity"].isin(severity))
        &
        (df["action"].isin(action))
        &
        (df["location"].isin(location))
    ]

    return filtered_df


def global_filters(df):

    st.sidebar.markdown("### 🌐 Global Filters")

    severity = st.sidebar.multiselect(
        "Severity",
        options=sorted(df["severity"].unique()),
        default=list(sorted(df["severity"].unique()))
    )

    location = st.sidebar.multiselect(
        "Location",
        options=sorted(df["location"].unique()),
        default=list(sorted(df["location"].unique()))
    )

    filtered_df = df[
        (df["severity"].isin(severity))
        &
        (df["location"].isin(location))
    ]

    return filtered_df


# ==========================================================
# TABLE STYLING
# ==========================================================

def style_risk_table(df):

    display_df = df.copy()

    def severity_badge(value):

        value = str(value).upper()

        if value == "CRITICAL":
            return "🔴 CRITICAL"

        elif value == "HIGH":
            return "🟠 HIGH"

        elif value == "MEDIUM":
            return "🟡 MEDIUM"

        else:
            return "🟢 LOW"

    if "severity" in display_df.columns:

        display_df["severity"] = (
            display_df["severity"]
            .apply(severity_badge)
        )

    return display_df


# ==========================================================
# INVESTIGATION PANEL
# ==========================================================

def risk_details(df):

    section_header(
        "🧑‍💻 Investigation Workspace",
        "Analyze suspicious user activity and determine the appropriate response."
    )

    selected_employee = st.selectbox(
        "Choose an employee to investigate",
        sorted(df["employee_id"].unique())
    )

    event = df[
        df["employee_id"] == selected_employee
    ].iloc[0]

    score = int(event["risk_score"])

    severity = str(event["severity"]).upper()

    # ------------------------------------------------------
    # Risk Overview Card
    # ------------------------------------------------------

    with st.container(border=True):

        left, right = st.columns([2, 1])

        with left:

            st.markdown(f"## 👤 {event['employee_id']}")

            if severity == "CRITICAL":
                st.error("🔴 CRITICAL")

            elif severity == "HIGH":
                st.warning("🟠 HIGH")

            elif severity == "MEDIUM":
                st.info("🟡 MEDIUM")

            else:
                st.success("🟢 LOW")

        with right:

            st.metric(
                "Risk Score",
                f"{score}/100"
            )

        st.progress(score / 100)

    st.markdown("<br>", unsafe_allow_html=True)

    # ------------------------------------------------------
    # Event Details
    # ------------------------------------------------------

    with st.container(border=True):

        st.subheader("📋 Event Details")

        col1, col2 = st.columns(2)

        with col1:

            st.markdown(f"**Action**  \n{event['action']}")

            st.markdown(f"**Location**  \n{event['location']}")

            st.markdown(f"**Device**  \n{event['device']}")

        with col2:

            st.markdown(f"**File**  \n{event['file_name']}")

            st.markdown(f"**Sensitivity**  \n{event['file_sensitivity']}")

            status = (
                "Anomaly"
                if event["is_anomaly"] == 1
                else "Normal"
            )

            st.markdown(f"**Status**  \n{status}")

    st.markdown("<br>", unsafe_allow_html=True)

    # ------------------------------------------------------
    # Risk Factors
    # ------------------------------------------------------

    with st.container(border=True):

        st.subheader("⚠️ Risk Factors")

        reasons = event.get("reasons", [])

        if isinstance(reasons, str):

            reasons = (
                reasons
                .strip("[]")
                .replace("'", "")
                .split(",")
            )

        if reasons:

            for reason in reasons:

                st.markdown(
                    f"• {str(reason).strip()}"
                )

        else:

            st.success(
                "No additional risk factors available."
            )

    st.markdown("<br>", unsafe_allow_html=True)

    # ------------------------------------------------------
    # AI Analyst Recommendation
    # ------------------------------------------------------

    with st.container(border=True):

        st.subheader("🧠 AI Analyst Recommendation")

        if severity == "CRITICAL":

            st.error(
                """
**Immediate action recommended**

• Review authentication logs for the last 24 hours.

• Validate all privileged activity.

• Consider temporarily restricting access until the investigation is complete.
"""
            )

        elif severity == "HIGH":

            st.warning(
                """
**Investigate suspicious behavior**

• Review recent file access activity.

• Monitor user behavior for escalation.

• Escalate if additional anomalies are detected.
"""
            )

        elif severity == "MEDIUM":

            st.info(
                """
**Continue monitoring**

• Validate unusual activity with the employee.

• Review future behavior for escalation.
"""
            )

        else:

            st.success(
                """
**No immediate action required**

Continue routine monitoring and periodic review.
"""
            )