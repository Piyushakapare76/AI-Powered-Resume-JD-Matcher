# AI-Powered-Resume-JD-Matcher


An AI-driven application that evaluates a candidate’s resume against a job description and generates a **fit score with a concise explanation**.  
The system is designed to help recruiters and hiring teams quickly assess candidate suitability using semantic understanding instead of keyword matching.

---

## Objective

To build a tool that:
- Accepts a resume (plain text or PDF) and a job description
- Uses AI to evaluate compatibility
- Outputs a **match score (0–100)** with a clear justification
- Recommends improvements to increase alignment
- Stores and ranks multiple candidate evaluations

---

## Features

### MVP Features
- Resume input (text)
- Job description input
- AI-based semantic matching
- Match score generation (0–100)
- Short, human-readable explanation
- Simple Web UI 

###  Bonus Features
- Resume improvement suggestions
- Persistent storage of results
- Ranking of multiple resumes based on score
- Automatic name extraction from resume text

## System Architecture

User Input (Resume + JD)
        ↓
Text Preprocessing
        ↓
 Embedding Model
        ↓
Similarity Scoring (Cosine Similarity)
        ↓
Score Normalization (0–100)
        ↓
Explanation + Suggestions
        ↓
Ranking Storage 
        ↓
Web UI Display

## Components:
1) User Interface (Flask + HTML/CSS)

Simple web interface

Left panel: Resume and Job Description input

Right panel: Match score, explanation, and suggestions

Rankings displayed without clearing previous inputs

No database used (in-memory storage)

2) Text Processing Module

Cleans and normalizes resume and job description text

Extracts keywords and skill terms

Automatically detects candidate name from resume text

3) Embedding Engine

Converts resume and job description into numerical vectors

Uses pre-trained sentence embeddings for semantic similarity

Runs 100% offline after model download

4) Matching & Scoring Logic

Uses cosine similarity between resume and JD vectors

Score normalized into percentage format (0–100%)

Ensures higher scores for strong semantic matches

5) Explanation & Recommendation Engine

Identifies missing or weak skills

Generates short justification like:

“Strong backend development skills but limited cloud experience”

Recommends keywords or skills to add to improve match

6) Ranking Module

Stores multiple resume scores in memory

Displays rankings in descending order

Automatically updates when a new resume is analyzed


## AI Tools Used & Technical Decisions
Sentence Transformers (Embedding Model)

## Model Used:
TF-IDF

## Why this model?

Lightweight and fast

Produces high-quality semantic embeddings

Works very well for resume–JD similarity

Fully usable offline after initial download

No API key, billing, or rate limits required

## Why embeddings instead of keyword matching?

Captures semantic meaning, not just exact words

## Example:

“Backend Developer” ≈ “Server-side Engineer”

Much more accurate and realistic scoring

## Prompt Engineering / RAG (Explanation)
Prompt Engineering

Instead of a generative LLM, the system uses semantic similarity

Explanation and suggestions are derived from:

Skill overlap

Missing important JD keywords

This ensures:

Deterministic output
 reliability

No hallucinations

## RAG (Retrieval-Augmented Generation)

Light RAG-style logic is used:

Resume text = document

Job description = query

Missing keywords = retrieval result

Suggestions are generated based on retrieved missing skills
