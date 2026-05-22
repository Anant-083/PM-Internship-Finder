import os
from groq import Groq

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

def explain_match(student, internship, matched_skills, score):
    
    try:
        prompt = f"""
You are an internship counselor for India's PM Internship Scheme.

A student has been matched with an internship. Explain this match in 2-3 simple sentences.
Be encouraging, specific, and mention the actual skills and location that matched.

Student Details:
- Name: {student['name']}
- Skills: {student['skills']}
- State: {student['state']}
- Preferred Sector: {student['sector_preference']}

Matched Internship:
- Company: {internship['company']}
- Role: {internship['role']}
- Location: {internship['location']}, {internship['state']}
- Required Skills: {internship['skills_required']}
- Stipend: Rs {internship['stipend']}/month

Skills that matched: {', '.join(matched_skills) if matched_skills else 'General profile fit'}
Match Score: {score}/100

Write a short friendly explanation. Plain sentences only. No bullet points.
"""

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=150,
            temperature=0.7
        )

        return response.choices[0].message.content.strip()

    except Exception as e:
        return f"This internship matches your profile with a score of {score}/100."
