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
    search_topic = st.text_input("Search research topics", placeholder="eg: LLM applications in healthcare")
    if st.button("Search"):
        xml_tree = fetch_files(base_url, search_topic)
        # Process the fetched files here
        st.write("Files fetched successfully! Displaying results...")
        feed = feedparser.parse(xml_tree)
        st.write(f"{len(feed.entries)} entries found")
        for entry in feed.entries:
            st.write(f"**Title:** {entry.title}")
            st.write(f"**Authors:** {', '.join(author.name for author in entry.authors)}")
            st.write(f"**Published:** {entry.published}")
            st.write(f"**Summary:** {entry.summary}")
            st.write(f"**Link:** [Read more]({entry.link})")
            similarity_score = compute_similarity(search_topic, entry.title, entry.summary)
            st.write(f"**Similarity Score:** {similarity_score:.2f}%")

dashboard()