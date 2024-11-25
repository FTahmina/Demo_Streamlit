import os
import streamlit as st

st.logo('Images/logo_1.png')


pages = {
    "Streamlit": [
    	st.Page("pages/Home.py", title="🔳 Introduction"),
        st.Page("pages/Installation.py", title="🔳 Installation"),
        st.Page("pages/CreateApp.py", title="🔳 Create and Update App"),
    ],

    "Resources": [
        st.Page("pages/Learn.py", title="Learn about us"),
    ],
}

pg = st.navigation(pages)
pg.run()