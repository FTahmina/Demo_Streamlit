import os
import streamlit as st
from PIL import Image

col1, col2, col3 = st.columns(3)
with col2:
	st.image('Images/logo_1.png')


# Center-aligned text using HTML
st.write("""<h1 style='text-align: center; color: Brown'>
	A faster way to build and share data apps
	</h1>""", unsafe_allow_html=True)

st.caption("""<h3 style='text-align: center'>
	Streamlit turns data scripts into shareable web apps in minutes. All in pure Python. No front‑end experience required.
	</h3>""", unsafe_allow_html=True)


st.divider()

st.write(""" <a href="https://streamlit.io/#install" 
    	style="padding: 10px 16px; 
        background: red; 
        color: white; 
        text-decoration: none; 
        border-radius: 8px; 
        font-size: 16px;" > 
        👉  Try Streamlit Now
    </a> """, unsafe_allow_html=True)


st.link_button('☁️ Deploy on Community Cloud', 'https://streamlit.io/cloud')
st.link_button('📄 Streamlit Documentation', 'https://docs.streamlit.io/')

