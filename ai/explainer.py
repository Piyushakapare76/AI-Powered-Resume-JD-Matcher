from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def explain_match(resume, jd, score):
    prompt = f"""
You are a technical recruiter.

Resume:
{resume}

Job Description:
{jd}

Match Score: {score}

Provide:
1. A 2-line justification
2. Missing skills (bullet points)
3. 3 resume improvement suggestions
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.3
    )

    return response.choices[0].message.content
