import streamlit as st


IMAGE_ADDRESS = "https://www.kl-marathon.com/media/uploads/logo/rcm_logo.jpg"


st.title("ReefCheck Analyse")
st.image(IMAGE_ADDRESS)

if st.experimental_user.is_logged_in:
    with st.sidebar:
        st.write(st.experimental_user["name"])
        st.image(st.experimental_user["picture"])

if not st.experimental_user.is_logged_in:
    if st.sidebar.button("Log in with Google", type="primary", icon=":material/login:"):
        st.login()
else:
    if st.sidebar.button("Log out", type="secondary", icon=":material/logout:"):
        st.write(st.experimental_user["name"])
        st.logout()
        st.stop()