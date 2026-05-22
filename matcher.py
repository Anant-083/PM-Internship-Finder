import csv
import os

def load_internships():
    internships = []
    filepath = os.path.join(os.path.dirname(__file__), 'data', 'internships.csv')
    with open(filepath, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            internships.append(row)
    return internships


def calculate_score(student, internship):
    score = 0

    # --- Skills Match (40 points) ---
    student_skills = [s.strip().lower() for s in student['skills'].split(',')]
    required_skills = [s.strip().lower() for s in internship['skills_required'].split(',')]
    
    matched_skills = set(student_skills) & set(required_skills)
    if len(required_skills) > 0:
        skill_score = (len(matched_skills) / len(required_skills)) * 40
        score += skill_score

    # --- State Match (20 points) ---
    if student['state'].strip().lower() == internship['state'].strip().lower():
        score += 20
    else:
        score += 5  # partial points for any location

    # --- Sector Preference Match (20 points) ---
    if student['sector_preference'].strip().lower() == internship['sector'].strip().lower():
        score += 20

    # --- Education Match (10 points) ---
    if student['education'].strip().lower() == internship['education_required'].strip().lower():
        score += 10

    # --- Affirmative Action Bonus (10 points) ---
    if student.get('rural', 'no').strip().lower() == 'yes':
        score += 5
    if student.get('differently_abled', 'no').strip().lower() == 'yes':
        score += 5

    return round(score, 2)


def get_top_matches(student, top_n=5):
    internships = load_internships()
    scored = []

    for internship in internships:
        score = calculate_score(student, internship)
        scored.append({
            'internship': internship,
            'score': score,
            'matched_skills': list(
                set([s.strip().lower() for s in student['skills'].split(',')]) &
                set([s.strip().lower() for s in internship['skills_required'].split(',')])
            )
        })

    # Sort by score descending
    scored.sort(key=lambda x: x['score'], reverse=True)

    return scored[:top_n]
