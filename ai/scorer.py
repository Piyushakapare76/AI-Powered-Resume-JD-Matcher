from sklearn.metrics.pairwise import cosine_similarity

def calculate_score(resume_vec, jd_vec):
    similarity = cosine_similarity([resume_vec], [jd_vec])[0][0]
    return round(similarity * 100, 2)
