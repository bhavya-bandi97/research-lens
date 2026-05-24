# Research Lens 🔬

Discover free academic research papers with AI-powered relevance scoring.

## What it does
- Searches arXiv for research papers on any topic
- Scores each paper's relevance to your search using 
  semantic similarity (Sentence Transformers)
- Displays title, authors, published date, summary, 
  and match percentage
- Colour-coded relevance: highly relevant, 
  moderately relevant, less relevant

## Tech Stack
- Python | Streamlit | arXiv API
- Sentence Transformers (all-MiniLM-L12-v2)
- Semantic similarity via cosine similarity

## How it works
1. User enters a research topic
2. Fetches up to 30 papers from arXiv API
3. Converts search topic and each paper 
   (title + abstract) into vector embeddings
4. Calculates cosine similarity between 
   query and paper vectors
5. Displays results ranked by match percentage

## Why I built this
Students and researchers often struggle to find 
free, relevant academic papers. This tool makes 
arXiv's catalogue more accessible and intelligent.

## Future scope
- Pagination for 30 results
- Year range filter
- Two-stage retrieval — abstract scoring for 
  shortlisting, full paper analysis for top results
- FastAPI backend with caching
- Save and bookmark papers

## Run locally
pip install -r requirements.txt
streamlit run ui/dashboard.py