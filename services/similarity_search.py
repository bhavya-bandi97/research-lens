from sentence_transformers import SentenceTransformer, util



model = SentenceTransformer('all-MiniLM-L12-v2')

def compute_similarity(query, title, abstract):
    query_embedding = model.encode(query)
    title_embedding = model.encode(title)
    abstract_embedding = model.encode(abstract)
    
    title_score = util.cos_sim(query_embedding, title_embedding).item()
    abstract_score = util.cos_sim(query_embedding, abstract_embedding).item()

    weighted_score = (0.7 * title_score) + (0.3 * abstract_score)
    match_percentage = weighted_score * 100
    return match_percentage
