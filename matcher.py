import csv
import os

def load_internships():
    internships = []
    try:
        filepath = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data', 'internships.csv')
        with open(filepath, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                internships.append(row)
    except Exception as e:
        print(f"Error loading internships: {e}")
    return internships


def calculate_score(student, internship):
    score = 0

    try:
        # Skills Match (40 points)
        student_skills = [s.strip().lower() for s in student['skills'].split(',')]
        raw = internship['skills_required'].replace(']','').replace('[','')
        required_skills = [s.strip().lower() for s in raw.split(',')]

        matched_skills = set(student_skills) & set(required_skills)
        if len(required_skills) > 0:
            score += (len(matched_skills) / len(required_skills)) * 40

        # State Match (20 points)
        if student['state'].strip().lower() == internship['state'].strip().lower():
            score += 20
        else:
            score += 5

        # Sector Match (20 points)
        if student['sector_preference'].strip().lower() == internship['sector'].strip().lower():
            score += 20

        # Education Match (10 points)
        if student['education'].strip().lower() == internship['education_required'].strip().lower():
            score += 10

        # Affirmative Action (10 points)
        if student.get('rural', 'no').strip().lower() == 'yes':
            score += 5
        if student.get('differently_abled', 'no').strip().lower() == 'yes':
            score += 5

    except Exception as e:
        print(f"Error calculating score: {e}")

    return round(score, 2)


def get_top_matches(student, top_n=5):
    internships = load_internships()
    scored = []

    for internship in internships:
        score = calculate_score(student, internship)
        
        student_skills = [s.strip().lower() for s in student['skills'].split(',')]
        raw = internship['skills_required'].replace(']','').replace('[','')
        required_skills = [s.strip().lower() for s in raw.split(',')]
        matched = list(set(student_skills) & set(required_skills))

        scored.append({
            'internship': internship,
            'score': score,
            'matched_skills': matched
        })

    scored.sort(key=lambda x: x['score'], reverse=True)
    return scored[:top_n]
