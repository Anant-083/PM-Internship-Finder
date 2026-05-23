# PM Internship Finder

![SIH25033](https://img.shields.io/badge/SIH-25033-blue?style=for-the-badge)
![Ministry of Corporate Affairs](https://img.shields.io/badge/Ministry-Corporate%20Affairs-navy?style=for-the-badge)
![Flask](https://img.shields.io/badge/Flask-Python-black?style=for-the-badge&logo=flask)
![Groq AI](https://img.shields.io/badge/Groq-AI%20Powered-orange?style=for-the-badge)
![Render](https://img.shields.io/badge/Deployed-Render-brightgreen?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Live-success?style=for-the-badge)

> AI-powered internship matching system built for Smart India Hackathon 2025 — Problem Statement SIH25033 by Ministry of Corporate Affairs.

**[Live Demo](https://pm-internship-finder.onrender.com)** · **[Report Bug](https://github.com/Anant-083/PM-Internship-Finder/issues)** · **[Request Feature](https://github.com/Anant-083/PM-Internship-Finder/issues)**

---

## The Problem

India's PM Internship Scheme promises 1 crore internships over 5 years across the country's top 500 companies. But the challenge is not the number of opportunities — it is the matching. Thousands of students apply, and without a smart system, wrong students get wrong internships. Students from rural areas and underrepresented communities get further left behind.

The Ministry of Corporate Affairs needed a solution: an intelligent system that matches every student to the right opportunity — fairly, quickly, and transparently.

---

## What We Built

A full-stack AI-powered web application where a student fills their profile once — skills, location, education, sector preference — and gets back their top 5 internship matches, ranked by a weighted scoring algorithm, each explained in plain language by an AI.

Not a form that collects data. An engine that makes decisions.

---

## How the Matching Works

Every internship in the database gets scored against the student's profile:

```
Skills match          →  up to 40 points
State match           →  up to 20 points
Sector preference     →  up to 20 points
Education match       →  up to 10 points
Affirmative action    →  up to 10 points
────────────────────────────────────────
Maximum score         →  100 points
```

Affirmative action gives a bonus to students from rural/aspirational districts and differently abled candidates — directly addressing the PS requirement for equitable representation.

The top 5 highest scoring internships are returned. Each one comes with an AI-generated explanation — written by Groq's llama-3.3-70b model — telling the student exactly why this internship was recommended for them.

---

## Features

- AI-powered matchmaking engine using weighted scoring algorithm
- Groq AI generates personalised explanation for each match
- Affirmative action bonus for rural and differently abled students
- Admin dashboard with password protection
- Clean professional light UI — fully responsive
- 50 internship slots across 14 sectors and 16 states (expanding)

---

## Tech Stack

![Python](https://img.shields.io/badge/Python-3.11-blue?style=flat-square&logo=python)
![Flask](https://img.shields.io/badge/Flask-3.0-black?style=flat-square&logo=flask)
![Groq](https://img.shields.io/badge/Groq-llama--3.3--70b-orange?style=flat-square)
![HTML](https://img.shields.io/badge/HTML-5-red?style=flat-square&logo=html5)
![CSS](https://img.shields.io/badge/CSS-3-blue?style=flat-square&logo=css3)
![JavaScript](https://img.shields.io/badge/JavaScript-ES6-yellow?style=flat-square&logo=javascript)

| Layer | Technology |
|---|---|
| Backend | Flask (Python) |
| Frontend | HTML, CSS, JavaScript |
| Matching Engine | Pure Python weighted scoring |
| AI Explanation | Groq API — llama-3.3-70b-versatile |
| Database | CSV — 50 internship slots |
| Deployment | Render |

---

## Project Structure

```
PM-Internship-Finder/
│
├── app.py                  ← Flask routes
├── matcher.py              ← Matching algorithm
├── groq_helper.py          ← Groq AI integration
│
├── data/
│   └── internships.csv     ← Internship database
│
├── templates/
│   ├── index.html          ← Student profile form
│   ├── results.html        ← Matched internships
│   ├── admin.html          ← Admin dashboard
│   └── admin_login.html    ← Admin login
│
├── static/
│   ├── style.css
│   └── script.js
│
├── requirements.txt
├── Procfile
└── README.md
```

---

## Run Locally

```bash
# Clone the repo
git clone https://github.com/Anant-083/PM-Internship-Finder
cd PM-Internship-Finder

# Install dependencies
pip install -r requirements.txt

# Create .env file
echo GROQ_API_KEY=your_groq_api_key_here > .env

# Run
python app.py
```

Open `http://localhost:5000`

---

## PS Requirements vs What's Built

| Requirement from SIH25033 | Status |
|---|---|
| Skills-based AI matching | Done |
| Location preference matching | Done |
| Sector interest matching | Done |
| Education qualification matching | Done |
| Affirmative action — rural districts | Done |
| Affirmative action — differently abled | Done |
| AI-based matchmaking engine | Done |
| Functional frontend prototype | Done |
| Admin dashboard | Done |
| Password-protected admin access | Done |

---

## Roadmap

- [ ] Expand internship database — integrating real PM Internship Scheme data via government APIs
- [ ] Company self-registration portal — companies submit their own internship slots
- [ ] Past participation tracking — first-timers get priority
- [ ] Social category filters — SC/ST/OBC representation
- [ ] District-level affirmative action — aspirational districts get higher weightage
- [ ] Admin can add/remove internship slots from dashboard directly
- [ ] Export matched results as PDF

---

## Live Demo

**[pm-internship-finder.onrender.com](https://pm-internship-finder.onrender.com)**

---

## About

Built by **Anant** — B.Tech CSE (AI & ML), Brainware University
Solo project built for SIH25033 prototype submission.

This project is not affiliated with the Government of India. Independent prototype built for educational and hackathon purposes.

[![GitHub](https://img.shields.io/badge/GitHub-Anant--083-black?style=flat-square&logo=github)](https://github.com/Anant-083)
