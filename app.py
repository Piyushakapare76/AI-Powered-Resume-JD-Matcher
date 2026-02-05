from flask import Flask, render_template, request
from ai.matcher import match_resume_jd
from ai.name_extractor import extract_name

app = Flask(__name__,template_folder='templates')

rankings = []
candidate_count = 1

@app.route("/", methods=["GET", "POST"])
def index():
    global candidate_count

    score = None
    description = ""
    suggestions = []
    resume_text = ""
    jd_text = ""

    if request.method == "POST":
        resume_text = request.form["resume"]
        jd_text = request.form["jd"]

        score, description, suggestions = match_resume_jd(resume_text, jd_text)

        # 🔹 Extract name automatically
        name = extract_name(resume_text)
        if not name:
            name = f"Candidate {candidate_count}"
            candidate_count += 1

        rankings.append((name, score))
        rankings.sort(key=lambda x: x[1], reverse=True)

    return render_template(
        "index.html",
        score=score,
        description=description,
        suggestions=suggestions,
        rankings=rankings,
        resume=resume_text,
        jd=jd_text
    )

if __name__ == "__main__":
    app.run(debug=True)
