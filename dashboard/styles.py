import streamlit as st


def load_css():
    st.markdown(
        """
        <style>
        .stApp { background: radial-gradient(circle at top right, #102842 0, #07111f 36rem); color: #e5edf7; }
        [data-testid="stSidebar"] { background: linear-gradient(180deg, #0e2035, #081423); border-right: 1px solid #23344c; }
        [data-testid="stSidebarNav"] { display: none; }
        .sidebar-brand { padding: .8rem .25rem 1.45rem; }
        .brand-name { color: #f4f8ff !important; font-size: 1.35rem; font-weight: 780; margin-top: .65rem; }
        .brand-subtitle { color: #91adc9 !important; font-size: .74rem; margin-top: .2rem; }
        .nav-section-label { color: #7793af !important; font-size: .68rem; font-weight: 750; letter-spacing: .09rem; margin: 1.1rem 0 .45rem; }
        .active-nav, .disabled-nav { border-radius: 9px; padding: .65rem .7rem; font-weight: 650; margin: .15rem 0; }
        .active-nav { background: rgba(50,151,166,.2); border: 1px solid rgba(94,201,212,.38); color: #dbfbff !important; }
        .active-nav span, .disabled-nav span { margin-right: .5rem; }
        .disabled-nav { color: #617c98 !important; }
        .disabled-nav small { float: right; font-size: .64rem; font-weight: 600; }
        [data-testid="stSidebar"] [data-testid="stPageLink"] a { border-radius: 9px; color: #b9cce0 !important; font-weight: 620; padding: .6rem .65rem; }
        [data-testid="stSidebar"] [data-testid="stPageLink"] a:hover { background: rgba(80,185,197,.12); color: #f4f8ff !important; }
        .sidebar-spacer { height: 2rem; }
        .sidebar-report-label { color: #7793af !important; font-size: .65rem; font-weight: 750; letter-spacing: .08rem; margin-top: 1rem; }
        .sidebar-footer { color: #6f8aa6 !important; border-top: 1px solid #233e5a; font-size: .72rem; line-height: 1.6; margin-top: 1rem; padding-top: .85rem; }
        .page-hero { background: linear-gradient(120deg, rgba(16,45,82,.96), rgba(11,107,117,.88)); border: 1px solid #32768a; border-radius: 18px; padding: 2rem; margin-bottom: 1.75rem; box-shadow: 0 20px 45px rgba(0,0,0,.2); }
        .eyebrow { color: #9fd7dd !important; font-size: .75rem; font-weight: 700; letter-spacing: .08rem; }
        .hero-title { color: #ffffff !important; font-size: 2.25rem; font-weight: 750; margin-top: .35rem; }
        .hero-subtitle { color: #dbeafe !important; font-size: 1rem; margin-top: .5rem; }
        .report-timestamp { color: #b9d4e8 !important; font-size: .8rem; margin-top: 1.25rem; }
        div[data-testid="stMetric"] { background: #0e1d31; border: 1px solid #29435f; border-radius: 14px; padding: 1rem; }
        div[data-testid="stMetricLabel"] { color: #9fb3c8 !important; }
        div[data-testid="stMetricValue"] { color: #ffffff !important; }
        div[data-testid="stVerticalBlockBorderWrapper"] { background: rgba(14,29,49,.88); border-color: #29435f; border-radius: 14px; }
        [data-testid="stDataFrame"] { border: 1px solid #29435f; border-radius: 12px; overflow: hidden; }
        .stDownloadButton button { background: #167b89; color: white; border: 0; border-radius: 8px; font-weight: 650; }
        .metric-card { min-height: 134px; background: linear-gradient(145deg, rgba(18,39,63,.95), rgba(10,25,43,.96)); border: 1px solid #29435f; border-radius: 15px; box-shadow: 0 14px 28px rgba(0,0,0,.16); padding: 1.15rem; }
        .metric-card-label { color: #a7bad0 !important; font-size: .78rem; font-weight: 700; letter-spacing: .04rem; text-transform: uppercase; }
        .metric-card-value { font-size: 2rem; font-weight: 760; line-height: 1.2; margin-top: .9rem; }
        .metric-card-detail { color: #8fa9c6 !important; font-size: .8rem; margin-top: .65rem; }
        .status-badge { display: inline-block; border: 1px solid; border-radius: 999px; padding: .35rem .7rem; font-size: .75rem; font-weight: 750; letter-spacing: .04rem; text-transform: uppercase; }
        .empty-state { border: 1px dashed #38516d; border-radius: 14px; color: #a7bad0 !important; padding: 1.5rem; text-align: center; background: rgba(14,29,49,.55); }
        .empty-state-title { color: #e5edf7 !important; font-weight: 700; margin-bottom: .35rem; }
        .stButton > button, .stDownloadButton > button { min-height: 2.5rem; }
        </style>
        """,
        unsafe_allow_html=True,
    )
