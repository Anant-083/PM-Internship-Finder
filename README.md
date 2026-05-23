# PM Internship Finder

> AI-powered internship matching system built for Smart India Hackathon 2025 — Problem Statement SIH25033 by Ministry of Corporate Affairs.

---

## The Problem

India's PM Internship Scheme promises 1 crore internships over 5 years across the country's top 500 companies. But the challenge isn't the number of opportunities — it's the matching. Thousands of students apply, and without a smart system, wrong students get wrong internships. Students from rural areas and underrepresented communities get further left behind.

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

## Screenshots

> Home — Student profile form

> Results — Top 5 matches with AI insight

> Admin — Internship slots and sector distribution

---

## Tech Stack

```
Frontend       HTML, CSS, JavaScript
Backend        Python, Flask
AI Layer       Groq API (llama-3.3-70b-versatile)
Matching       Pure Python weighted scoring
Data           CSV — 50 internship slots, 14 sectors, 16 states
Deployment     Render
```

---

## Run It Locally

```bash
git clone https://github.com/Anant-083/PM-Internship-Finder
cd PM-Internship-Finder
pip install -r requirements.txt
```

Create a `.env` file:
```
GROQ_API_KEY=your_key_here
```

Run:
```bash
python app.py
```

Open `http://localhost:5000`

---

## PS Requirements vs What's Built

| Requirement from SIH25033 | Implemented |
|---|---|
| Skills-based AI matching | Yes |
| Location preference | Yes |
| Sector interest | Yes |
| Education qualification | Yes |
| Affirmative action — rural districts | Yes |
| Affirmative action — differently abled | Yes |
| Internship capacity tracking | Partial — via CSV database |
| Functional frontend prototype | Yes |
| AI-based matchmaking engine | Yes |

---

## Live Demo

https://pm-internship-finder.onrender.com

---

## About

Built by Anant, a second-year B.Tech CSE (AI & ML) student at Brainware University, as a solo SIH prototype project.

This project is not affiliated with the Government of India. It is an independent prototype built for educational and hackathon purposes.

GitHub: [Anant-083](https://github.com/Anant-083)
