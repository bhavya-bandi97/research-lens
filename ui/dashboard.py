import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import streamlit as st
from services.get_files import fetch_files, base_url
from services.similarity_search import compute_similarity
import feedparser

def dashboard():
    st.title("Research Lens")
    st.write("Welcome to the Research Lens! Here you can find various research papers based on your interests. Use the search bar below to get started.")
    # Add more dashboard components here as needed
    search_topic = st.text_input("Search research topics", 
                                 placeholder="eg: LLM applications in healthcare", 
                                 on_change=lambda: st.session_state.update({"search_triggered": True}))
    if "search_triggered" not in st.session_state:
        st.session_state.search_triggered = False

    search_clicked = st.button("Search") or st.session_state.search_triggered
    st.session_state.search_triggered = False
    if search_clicked and search_topic:
        xml_tree = fetch_files(base_url, search_topic)
        # Process the fetched files here
        st.write("Files fetched successfully! Displaying results...")
        feed = feedparser.parse(xml_tree)
        st.write(f"Found {len(feed.entries)} entries for the topic '{search_topic}'.")
        for entry in feed.entries:
            with st.container(border=True):
                st.write(f"**Title:** {entry.title}")
                st.write(f"**Authors:** {', '.join(author.name for author in entry.authors)}")
                st.write(f"**Published:** {entry.published[:10]}")  # Display only the date part
                with st.expander("Summary"):
                    st.write(f"**Summary:** {entry.summary}")
                st.write(f"**Link:** [Read more]({entry.link})")
                similarity_score = compute_similarity(search_topic, entry.title, entry.summary)
                if similarity_score >= 70:  # Display only if similarity score is above 70%
                    st.success(f"Similarity Score: {similarity_score:.2f}% - Highly relevant!")
                elif similarity_score >= 40:
                    st.info(f"Similarity Score: {similarity_score:.2f}% - Moderately relevant.")
                else:
                    st.warning(f"Similarity Score: {similarity_score:.2f}% - Less relevant.")

dashboard()