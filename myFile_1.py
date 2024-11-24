import os
import streamlit as st
from PIL import Image

cwd = os.getcwd()

image_file = ('pic_1.PNG')
image_path = os.path.join(cwd, image_file)
img = Image.open(image_path)
st.image(img)

st.title('Streamlit')
st.header('How to Create Your Own App!')
st.write('')

st.info('Go to GitHub.com')
st.link_button('GitHub', 'https://github.com/')

st.write('- Login / Create an Account')
st.write('- Create a New Repository > Add: Repository Name > Settings: Public > Create Repository') 
st.write('- Add files > Upload File')
st.write('- Upload your local .py file > Commit Changes')
st.write('')

st.info('Go to streamlit.app')
st.link_button('Streamlit App', 'https://share.streamlit.io/')
st.write('- Login / Create an Account')
st.write('- Create App > Connect to GitHub')
st.write('- Select --> Deploy a public App from GitHub')
st.write('- Fill up --> Deploy an App')
st.write('-- Copy the GitHub Repository URL from Address bar > Paste in the Streamplit Deploy Form')
st.write('-- Main File Path --> Select your main .py file name')
st.write('-- App URL --> Write an URL for your Website')
st.write('- Deploy')
st.write('')


st.success('Your Website has been deployed successfully!')
st.write('')
st.write('')
st.subheader('Update Your App')
st.write('- Go to your GitHub Repository')
st.write('- Add files > Upload File')
st.write('- Upload your updated local .py file > Commit Changes')
st.write('')
st.write('')
st.write('')

st.divider()
st.write('R E F E R E N C E S')
st.caption('- Streamlit Blog: https://blog.streamlit.io/host-your-streamlit-app-for-free/')
st.caption('- Streamlit Documentation: https://docs.streamlit.io/')

st.feedback('stars')