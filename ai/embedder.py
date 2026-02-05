from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def match_resume_jd(resume, jd):
    documents = [resume, jd]

    vectorizer = TfidfVectorizer(stop_words="english")
    vectors = vectorizer.fit_transform(documents)

    similarity = cosine_similarity(vectors[0], vectors[1])[0][0]
    score = round(similarity * 100, 2)

    # Simple explanation logic
    if score > 75:
        description = "Strong skill alignment with the job description"
    elif score > 50:
        description = "Moderate match but missing some required skills"
    else:
        description = "Low match; significant skill gaps detected"

    # Suggestions
    resume_words = set(resume.lower().split())
    jd_words = set(jd.lower().split())
    missing = list(jd_words - resume_words)

    suggestions = missing[:5]

    return score, description, suggestions
