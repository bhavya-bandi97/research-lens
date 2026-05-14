import streamlit as st

def dashboard():
    st.title("Dashboard")
    st.write("Welcome to the dashboard! Here you can find various insights and metrics.")
    # Add more dashboard components here as needed
    st.text_input("Search research topics", palaceholder="eg: LLM applications in healthcare")
    st.button("Search")