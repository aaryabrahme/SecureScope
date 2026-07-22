import streamlit as st


def load_css():

    st.markdown(
        """
<style>

/* =========================
GLOBAL
========================= */

.stApp {

    background:
    linear-gradient(
        135deg,
        #020617,
        #0f172a
    );

    color:#f8fafc;

}


h1,h2,h3,h4,h5,h6 {

    color:#f8fafc !important;

}


p,span,div {

    color:#cbd5e1;

}


/* =========================
SIDEBAR
========================= */


section[data-testid="stSidebar"] {


    background:
    linear-gradient(
        180deg,
        #020617,
        #111827
    );


    border-right:
    1px solid #1e293b;


}



section[data-testid="stSidebar"] * {


    color:#f8fafc !important;


}



/* =========================
METRIC CARDS
========================= */


div[data-testid="stMetric"] {


    background:
    rgba(15,23,42,0.75);


    padding:20px;


    border-radius:18px;


    border:
    1px solid #334155;


    box-shadow:
    0 10px 30px rgba(0,0,0,0.35);


}



div[data-testid="stMetricLabel"] {


    color:#94a3b8 !important;


}



div[data-testid="stMetricValue"] {


    color:#ffffff !important;


    font-weight:800;


}



/* =========================
CONTAINERS
========================= */


div[data-testid="stVerticalBlockBorderWrapper"] {


    background:
    rgba(15,23,42,0.70);


    border-radius:20px;


    border:
    1px solid #334155;


    padding:10px;


}



/* =========================
DATAFRAME
========================= */


div[data-testid="stDataFrame"] {


    border-radius:16px;


    overflow:hidden;


}



/* =========================
DOWNLOAD BUTTONS
========================= */


.stDownloadButton button {


    background:#2563eb;


    color:white;


    border-radius:12px;


    border:none;


    font-weight:700;


}



.stDownloadButton button:hover {


    background:#1d4ed8;


}



/* =========================
ALERTS
========================= */


div[data-testid="stAlert"] {


    border-radius:16px;


}



/* =========================
SELECT BOX
========================= */


div[data-baseweb="select"] > div {


    background:#111827;


    border:
    1px solid #334155;


}



div[data-baseweb="select"] span {


    color:#f8fafc !important;


}


/* =========================
TABLE TEXT
========================= */


[data-testid="stDataFrame"] * {


    color:#f8fafc !important;


}


</style>
""",
        unsafe_allow_html=True,
    )