from flask import Flask, render_template, request
from matcher import get_top_matches
from groq_helper import explain_match
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/match', methods=['POST'])
def match():
    # Get student data from form
    student = {
        'name': request.form.get('name'),
        'age': request.form.get('age'),
        'gender': request.form.get('gender'),
        'state': request.form.get('state'),
        'education': request.form.get('education'),
        'skills': request.form.get('skills'),
        'sector_preference': request.form.get('sector_preference'),
        'rural': request.form.get('rural', 'no'),
        'differently_abled': request.form.get('differently_abled', 'no'),
        'stipend_expectation': request.form.get('stipend_expectation')
    }

    # Get top 5 matches
    top_matches = get_top_matches(student, top_n=5)

    # Add AI explanation to each match
    for match_item in top_matches:
        explanation = explain_match(
            student=student,
            internship=match_item['internship'],
            matched_skills=match_item['matched_skills'],
            score=match_item['score']
        )
        match_item['explanation'] = explanation

    return render_template('results.html', student=student, matches=top_matches)


@app.route('/admin')
def admin():
    return render_template('admin.html')


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
