
import streamlit as st

st.set_page_config(
    page_title="AI Project",
    page_icon="🤖"
)

st.title("AI Based Smart Monitoring System")

st.write("Welcome to my AI project!")

st.subheader("Project Dashboard")

name = st.text_input("Enter your name")

if st.button("Submit"):
    st.success(f"Welcome, {name}!")

st.info("Streamlit application is running successfully.")
