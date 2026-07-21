import streamlit as st


def load_css():

    st.markdown(
        """
<style>

/* =====================================================
   IMPORT FONT
===================================================== */

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');


/* =====================================================
   GLOBAL
===================================================== */

html,
body,
[class*="css"]{
    font-family:'Inter',sans-serif;
}

.stApp{

    background:#F5F7FB;
    color:#111827;

}


/* =====================================================
   MAIN PAGE
===================================================== */

.block-container{

    padding-top:2rem;
    padding-bottom:2rem;
    padding-left:3rem;
    padding-right:3rem;
    max-width:1500px;

}


/* =====================================================
   HEADINGS
===================================================== */

h1{

    font-size:2.4rem;
    font-weight:800;
    color:#111827;
    letter-spacing:-0.5px;

}

h2{

    font-size:1.7rem;
    font-weight:700;
    color:#111827;

}

h3{

    font-size:1.3rem;
    font-weight:600;
    color:#111827;

}


/* =====================================================
   SIDEBAR
===================================================== */

section[data-testid="stSidebar"]{

    background:#FFFFFF;
    border-right:1px solid #E5E7EB;

}

section[data-testid="stSidebar"] .block-container{

    padding-top:2rem;
    padding-left:1.4rem;
    padding-right:1.4rem;

}


/* =====================================================
   DIVIDERS
===================================================== */

hr{

    border:none;
    border-top:1px solid #E5E7EB;
    margin:2rem 0;

}


/* =====================================================
   CONTAINERS
===================================================== */

div[data-testid="stVerticalBlockBorderWrapper"]{

    border-radius:22px;
    border:1px solid #E5E7EB;
    background:#FFFFFF;

    box-shadow:
        0 10px 30px rgba(15,23,42,.05);

    padding:.3rem;

    transition:.25s;

}

div[data-testid="stVerticalBlockBorderWrapper"]:hover{

    transform:translateY(-2px);

    box-shadow:
        0 18px 40px rgba(15,23,42,.08);

}


/* =====================================================
   METRIC CARDS
===================================================== */

div[data-testid="metric-container"]{

    background:white;

    border-radius:18px;

    border:1px solid #E5E7EB;

    padding:22px;

    box-shadow:
        0 8px 20px rgba(0,0,0,.05);

}

div[data-testid="metric-container"] label{

    color:#6B7280;

    font-size:15px;

}

div[data-testid="metric-container"] [data-testid="stMetricValue"]{

    font-size:36px;

    font-weight:800;

    color:#2563EB;

}


/* =====================================================
   DATAFRAME
===================================================== */

div[data-testid="stDataFrame"]{

    border-radius:18px;

    overflow:hidden;

    border:1px solid #E5E7EB;

}


/* =====================================================
   BUTTONS
===================================================== */

.stButton>button{

    background:#2563EB;

    color:white;

    border:none;

    border-radius:12px;

    padding:.65rem 1.4rem;

    font-weight:600;

    transition:.25s;

}

.stButton>button:hover{

    background:#1D4ED8;

    transform:translateY(-1px);

}


/* =====================================================
   DOWNLOAD BUTTON
===================================================== */

.stDownloadButton>button{

    width:100%;

    background:#2563EB;

    color:white;

    border:none;

    border-radius:12px;

    font-weight:600;

}


/* =====================================================
   SELECTBOX
===================================================== */

div[data-baseweb="select"]{

    border-radius:12px;

}


/* =====================================================
   MULTISELECT
===================================================== */

div[data-baseweb="tag"]{

    background:#DBEAFE;

    color:#1E40AF;

}


/* =====================================================
   PLOTLY
===================================================== */

.js-plotly-plot{

    border-radius:18px;

}


/* =====================================================
   ALERTS
===================================================== */

div[data-baseweb="notification"]{

    border-radius:16px;

}


/* =====================================================
   EXPANDERS
===================================================== */

details{

    border-radius:18px;

    border:1px solid #E5E7EB;

}


/* =====================================================
   SCROLLBAR
===================================================== */

::-webkit-scrollbar{

    width:10px;

}

::-webkit-scrollbar-thumb{

    background:#CBD5E1;

    border-radius:50px;

}

::-webkit-scrollbar-thumb:hover{

    background:#94A3B8;

}


/* =====================================================
   CAPTIONS
===================================================== */

.caption{

    color:#6B7280;

}


/* =====================================================
   LINKS
===================================================== */

a{

    color:#2563EB;

    text-decoration:none;

}

a:hover{

    text-decoration:underline;

}


/* =====================================================
   ANIMATION
===================================================== */

@keyframes fadeUp{

    from{

        opacity:0;

        transform:translateY(12px);

    }

    to{

        opacity:1;

        transform:translateY(0px);

    }

}

.block-container{

    animation:fadeUp .45s ease;

}

</style>
        """,
        unsafe_allow_html=True,
    )