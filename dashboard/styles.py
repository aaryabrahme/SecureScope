import streamlit as st


def load_css():
    st.markdown(
        """
        <style>

        /* ---------- GLOBAL ---------- */

        .stApp {
            background: radial-gradient(circle at top right, #102842 0, #07111f 36rem);
            color: #e5edf7;
        }


        /* ---------- SIDEBAR ---------- */

        [data-testid="stSidebar"] {
            background: linear-gradient(180deg, #0e2035, #081423);
            border-right: 1px solid #23344c;
        }

        [data-testid="stSidebarNav"] {
            display:none;
        }


        .sidebar-brand {
            padding: 0.5rem 0.2rem 1.5rem;
            text-align:left;
        }


        .sidebar-brand img {
            width:90px !important;
            height:90px !important;
            object-fit:contain;
            margin-bottom:10px;
        }


        .brand-name {
            color:#f4f8ff !important;
            font-size:1.45rem;
            font-weight:800;
        }


        .brand-subtitle {
            color:#91adc9 !important;
            font-size:.78rem;
        }


        .nav-section-label {
            color:#7793af !important;
            font-size:.68rem;
            font-weight:750;
            letter-spacing:.09rem;
            margin:1.1rem 0 .45rem;
        }


        .active-nav,
        .disabled-nav {

            border-radius:10px;
            padding:.7rem;
            font-weight:650;
            margin:.15rem 0;

        }


        .active-nav {

            background:rgba(50,151,166,.2);
            border:1px solid rgba(94,201,212,.38);
            color:#dbfbff !important;

        }


        .active-nav span {
            margin-right:.5rem;
        }


        /* ---------- PAGE HERO ---------- */


        .page-hero {

            background:
            linear-gradient(
            120deg,
            rgba(16,45,82,.96),
            rgba(11,107,117,.88)
            );

            border:1px solid #32768a;
            border-radius:18px;

            padding:2rem;
            margin-bottom:1.75rem;

        }


        .hero-title {

            color:white !important;
            font-size:2.25rem;
            font-weight:750;

        }


        .hero-subtitle {

            color:#dbeafe !important;

        }



        /* ---------- METRIC CARDS ---------- */


        .metric-card {

            height:155px;
            min-height:155px;

            display:flex;
            flex-direction:column;

            background:
            linear-gradient(
            145deg,
            rgba(18,39,63,.95),
            rgba(10,25,43,.96)
            );


            border:1px solid #29435f;

            border-radius:15px;

            padding:1.15rem;


            box-shadow:
            0 14px 28px rgba(0,0,0,.16);


            overflow:hidden;

        }



        .metric-card-label {


            color:#a7bad0 !important;

            font-size:.75rem;

            font-weight:750;

            letter-spacing:.05rem;

            text-transform:uppercase;


            height:42px;

            display:flex;

            align-items:flex-start;

        }



        .metric-card-value {


            font-size:2rem;

            font-weight:800;

            line-height:1;

            margin-top:.4rem;


        }



        .metric-card-detail {


            color:#8fa9c6 !important;

            font-size:.8rem;

            margin-top:auto;

            height:22px;


        }



        /* ---------- TABLE ---------- */


        [data-testid="stDataFrame"] {

            border:1px solid #29435f;

            border-radius:12px;

        }



        .status-badge {

            display:inline-block;

            border:1px solid;

            border-radius:999px;

            padding:.35rem .7rem;

            font-size:.75rem;

            font-weight:750;

        }

        .risk-score-box {

            background: linear-gradient(
                145deg,
                rgba(239,68,68,0.15),
                rgba(18,39,63,0.95)
            );

            border:1px solid #ef6b73;

            border-radius:15px;

            padding:1rem;

            text-align:center;

            margin-bottom:1rem;

        }


        .risk-score-value {

            font-size:3rem;

            font-weight:800;

            color:#ef6b73;

        }


        .risk-score-label {

            color:#9fb3c8;

            font-size:.85rem;

        }

        </style>
        """,

        unsafe_allow_html=True,
    )