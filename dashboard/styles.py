import streamlit as st


def load_css():
    st.markdown(
        """
        <style>
        .stApp { background: #07111f; color: #e5edf7; }
        [data-testid="stSidebar"] { background: #0b1728; border-right: 1px solid #23344c; }
        .page-hero { background: linear-gradient(120deg, #102d52, #0b6b75); border: 1px solid #32768a; border-radius: 18px; padding: 2rem; margin-bottom: 1.75rem; }
        .eyebrow { color: #9fd7dd !important; font-size: .75rem; font-weight: 700; letter-spacing: .08rem; }
        .hero-title { color: #ffffff !important; font-size: 2.25rem; font-weight: 750; margin-top: .35rem; }
        .hero-subtitle { color: #dbeafe !important; font-size: 1rem; margin-top: .5rem; }
        .report-timestamp { color: #b9d4e8 !important; font-size: .8rem; margin-top: 1.25rem; }
        div[data-testid="stMetric"] { background: #0e1d31; border: 1px solid #29435f; border-radius: 14px; padding: 1rem; }
        div[data-testid="stMetricLabel"] { color: #9fb3c8 !important; }
        div[data-testid="stMetricValue"] { color: #ffffff !important; }
        div[data-testid="stVerticalBlockBorderWrapper"] { background: #0e1d31; border-color: #29435f; border-radius: 14px; }
        [data-testid="stDataFrame"] { border: 1px solid #29435f; border-radius: 12px; overflow: hidden; }
        .stDownloadButton button { background: #167b89; color: white; border: 0; border-radius: 8px; font-weight: 650; }
        </style>
        """,
        unsafe_allow_html=True,
    )
