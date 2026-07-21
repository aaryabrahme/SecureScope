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

# ==========================================================
# SECURITY POSTURE
# ==========================================================

premium_divider()

section_header(
    "🛡 Security Posture",
    "Overall assessment based on the Organizational Risk Index."
)

with st.container(border=True):

    if org_risk < 30:

        st.success(
            """
### 🟢 Healthy Security Posture

Your organization currently exhibits a **low overall risk profile**.

**Recommendations**

• Continue routine monitoring

• Perform periodic security reviews

• Maintain current security controls
"""
        )

    elif org_risk < 70:

        st.warning(
            """
### 🟡 Elevated Security Posture

Multiple indicators require attention.

**Recommendations**

• Review high-risk employees

• Investigate suspicious behaviour

• Increase monitoring frequency
"""
        )

    else:

        st.error(
            """
### 🔴 Critical Security Posture

Immediate investigation is recommended.

**Recommendations**

• Investigate all critical-risk users

• Review authentication logs

• Validate privileged activity

• Consider temporary account restrictions
"""
        )


# ==========================================================
# ORI EXPLANATION
# ==========================================================

st.caption(
    """
### Organizational Risk Index (ORI)

The ORI is calculated using a weighted risk model.

• **60%** Average Risk Score

• **30%** Percentage of Anomalous Events

• **10%** Percentage of Critical Severity Events

The resulting score provides a high-level indicator of the organization's
overall cybersecurity posture.
"""
)


premium_divider()


# ==========================================================
# RECENT RISK EVENTS
# ==========================================================

section_header(
    "🚨 Recent Risk Events",
    "Highest-risk events detected during the latest scan."
)

display_df = (

    filtered_df

    .sort_values(
        "risk_score",
        ascending=False
    )[

        [
            "employee_id",
            "action",
            "severity",
            "risk_score",
            "location",
            "device",
        ]

    ]

)

with st.container(border=True):

    st.dataframe(

        style_risk_table(
            display_df
        ),

        use_container_width=True,

        hide_index=True,

    )


premium_divider()


# ==========================================================
# DASHBOARD SUMMARY
# ==========================================================

section_header(
    "📌 Executive Summary"
)

col1, col2, col3 = st.columns(3)

with col1:

    st.info(
        f"""
### Total Events

**{len(filtered_df):,}**

Security events analysed.
"""
    )

with col2:

    st.info(
        f"""
### Average Risk

**{filtered_df['risk_score'].mean():.1f}**

Current organizational average.
"""
    )

with col3:

    st.info(
        f"""
### Highest Risk

**{filtered_df['risk_score'].max()}**

Most severe event detected.
"""
    )


premium_divider()


# ==========================================================
# FOOTER
# ==========================================================

st.markdown(
    """
<div style="text-align:center;padding:20px;color:#6B7280;">

<b>SecureScope</b><br>

AI-Powered Security Intelligence Platform

<br><br>

Version 1.3 • © 2026 Aarya

</div>
""",
    unsafe_allow_html=True,
)