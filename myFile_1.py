import streamlit as st

st.title('Streamlit')
st.header("How to Create Your Own App!")

#click_button = st.button("Click here")

st.info('Go to GitHub.com')
st.link_button('GitHub', 'https://github.com/')

st.write('- Login / Create an Account')
st.write('- Create a Public Repository > Add files > Upload File')
st.write('- Upload your local .py file > Commit Changes')

st.info('Go to streamlit.app')
st.link_button("Streamlit App", 'https://share.streamlit.io/')
st.write('- Login / Create an Account')
st.write('- Create App > Connect to GitHub')
st.write('- Select --> Deploy a public App from GitHub')
st.write('- Fill up --> Deploy an App')
st.write('-- Copy the GitHub Repository URL from Address bar > Paste in the Streamplit Deploy Form')
st.write('-- Main File Path --> Select your main .py file name')
st.write('-- App URL --> Write an URL for your Website')
st.write('- Deploy')
st.write('')
st.write('')
st.write('')

st.success('Your Website has been deployed successfully!')
st.write('')
st.write('')
st.write('')

st.write('For more infomation, please visit https://docs.streamlit.io/')
st.snow()