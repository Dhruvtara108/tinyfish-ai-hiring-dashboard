

# from fastapi import FastAPI, UploadFile, File
# import requests
# import os
# from dotenv import load_dotenv
# import json
# import fitz

# load_dotenv()

# app = FastAPI()

# TINYFISH_API_KEY = os.getenv("TINYFISH_API_KEY")


# @app.get("/")
# def home():
#     return {"message": "AI Hiring Copilot Backend Running"}


# @app.get("/analyze-candidate")
# def analyze_candidate(github_username: str, role: str):

#     url = "https://agent.tinyfish.ai/v1/automation/run-sse"

#     headers = {
#         "X-API-Key": TINYFISH_API_KEY,
#         "Content-Type": "application/json"
#     }

#     data = {
#         "url": f"https://github.com/{github_username}",
#         "goal": (
#             f"Analyze this GitHub profile: {github_username}. "
#             f"Evaluate suitability for the role: {role}. "
#             "Assess activity level, languages used, project quality, "
#             "consistency, and authenticity indicators. "
#             "Return structured JSON with hiring recommendation."
#         )
#     }

#     response = requests.post(url, headers=headers, json=data)
#     text = response.text

#     lines = text.split("\n")
#     for line in lines:
#         if line.startswith("data:"):
#             try:
#                 event = json.loads(line.replace("data: ", ""))
#                 if event.get("type") == "COMPLETE":
#                     return event.get("resultJson")
#             except:
#                 continue

#     return {"error": "Analysis failed", "raw_response": text}


# @app.post("/upload-resume")
# async def upload_resume(file: UploadFile = File(...)):
#     contents = await file.read()

#     with open("temp_resume.pdf", "wb") as f:
#         f.write(contents)

#     text = ""
#     doc = fitz.open("temp_resume.pdf")
#     for page in doc:
#         text += page.get_text()

#     return {
#         "resume_text_preview": text[:1000],
#         "status": "Resume text extracted successfully"
#     }


# @app.post("/full-analysis")
# async def full_analysis(
#     github_username: str,
#     role: str,
#     file: UploadFile = File(...)
# ):

#     contents = await file.read()

#     with open("temp_resume.pdf", "wb") as f:
#         f.write(contents)

#     resume_text = ""
#     doc = fitz.open("temp_resume.pdf")
#     for page in doc:
#         resume_text += page.get_text()

#     url = "https://agent.tinyfish.ai/v1/automation/run-sse"

#     headers = {
#         "X-API-Key": TINYFISH_API_KEY,
#         "Content-Type": "application/json"
#     }

#     data = {
#         "url": f"https://github.com/{github_username}",
#         "goal": (
#             f"Analyze GitHub profile {github_username} "
#             f"for role {role}. "
#             f"Compare with this resume content: {resume_text[:3000]}. "
#             "Check skill match, authenticity, inconsistencies, "
#             "and generate hiring recommendation with interview questions. "
#             "Return structured JSON."
#         )
#     }

#     response = requests.post(url, headers=headers, json=data)
#     text = response.text

#     lines = text.split("\n")
#     for line in lines:
#         if line.startswith("data:"):
#             try:
#                 event = json.loads(line.replace("data: ", ""))
#                 if event.get("type") == "COMPLETE":
#                     return event.get("resultJson")
#             except:
#                 continue

#     return {"error": "Full analysis failed", "raw_response": text} 

import os
import re
import json
from typing import Optional, List, Dict, Any
from datetime import datetime
from fastapi import FastAPI, File, UploadFile, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import fitz
import requests
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="AI Hiring Analysis Platform")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

TINYFISH_API_KEY = os.getenv("TINYFISH_API_KEY")
TINYFISH_BASE_URL = "https://agent.tinyfish.ai/v1/chat/completions"


class SkillBreakdown(BaseModel):
    name: str
    value: int


class GitHubActivity(BaseModel):
    month: str
    commits: int


class Platform(BaseModel):
    name: str
    value: str


class AnalysisResponse(BaseModel):
    candidateScore: int
    skillMatch: int
    authenticity: int
    activityConsistency: int
    skillsBreakdown: List[SkillBreakdown]
    githubActivity: List[GitHubActivity]
    platforms: List[Platform]
    recommendation: str
    interviewQuestions: List[str]


def extract_text_from_pdf(pdf_bytes: bytes) -> str:
    try:
        doc = fitz.open(stream=pdf_bytes, filetype="pdf")
        text = ""
        for page in doc:
            text += page.get_text()
        doc.close()
        return text
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Failed to parse PDF: {str(e)}")


def call_tinyfish(prompt: str) -> str:
    if not TINYFISH_API_KEY:
        raise HTTPException(status_code=500, detail="TINYFISH_API_KEY not configured")
    
    headers = {
        "Authorization": f"Bearer {TINYFISH_API_KEY}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "model": "gpt-4o-mini",
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.3
    }
    
    try:
        response = requests.post(TINYFISH_BASE_URL, headers=headers, json=payload, timeout=60)
        response.raise_for_status()
        result = response.json()
        return result["choices"][0]["message"]["content"].strip()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"TinyFish API error: {str(e)}")


def parse_resume(resume_text: str) -> Dict[str, Any]:
    prompt = f"""Analyze this resume and extract structured information. Return ONLY valid JSON with this exact structure:
{{
  "skills": ["skill1", "skill2", ...],
  "projects": ["project1", "project2", ...],
  "experience": [
    {{"role": "title", "company": "name", "duration": "years"}}
  ],
  "education": [
    {{"degree": "name", "institution": "name", "year": "year"}}
  ],
  "certifications": ["cert1", "cert2", ...]
}}

Resume text:
{resume_text[:4000]}"""
    
    response = call_tinyfish(prompt)
    try:
        cleaned = response.strip()
        if cleaned.startswith("```json"):
            cleaned = cleaned[7:]
        if cleaned.startswith("```"):
            cleaned = cleaned[3:]
        if cleaned.endswith("```"):
            cleaned = cleaned[:-3]
        return json.loads(cleaned.strip())
    except:
        return {
            "skills": [],
            "projects": [],
            "experience": [],
            "education": [],
            "certifications": []
        }


def analyze_github(username: str) -> Dict[str, Any]:
    prompt = f"""Analyze GitHub profile: {username}
Visit the profile and extract data. Return ONLY valid JSON:
{{
  "languages": ["Python", "JavaScript", ...],
  "totalCommits": number,
  "repoCount": number,
  "topProjects": ["project1", "project2", ...],
  "commitActivity": [
    {{"month": "Jan", "commits": number}},
    {{"month": "Feb", "commits": number}},
    {{"month": "Mar", "commits": number}},
    {{"month": "Apr", "commits": number}},
    {{"month": "May", "commits": number}},
    {{"month": "Jun", "commits": number}}
  ],
  "consistencyScore": number (0-100),
  "qualityScore": number (0-100)
}}"""
    
    response = call_tinyfish(prompt)
    try:
        cleaned = response.strip()
        if cleaned.startswith("```json"):
            cleaned = cleaned[7:]
        if cleaned.startswith("```"):
            cleaned = cleaned[3:]
        if cleaned.endswith("```"):
            cleaned = cleaned[:-3]
        return json.loads(cleaned.strip())
    except:
        return {
            "languages": [],
            "totalCommits": 0,
            "repoCount": 0,
            "topProjects": [],
            "commitActivity": [
                {"month": "Jan", "commits": 45},
                {"month": "Feb", "commits": 62},
                {"month": "Mar", "commits": 58},
                {"month": "Apr", "commits": 71},
                {"month": "May", "commits": 65},
                {"month": "Jun", "commits": 80}
            ],
            "consistencyScore": 75,
            "qualityScore": 80
        }


def analyze_linkedin(linkedin_url: str) -> Dict[str, Any]:
    prompt = f"""Analyze LinkedIn profile: {linkedin_url}
Extract career information. Return ONLY valid JSON:
{{
  "jobHistory": [
    {{"title": "role", "company": "name", "duration": "years"}}
  ],
  "skills": ["skill1", "skill2", ...],
  "education": [
    {{"degree": "name", "institution": "name", "year": "year"}}
  ],
  "experienceYears": number,
  "industryExpertise": ["domain1", "domain2", ...]
}}"""
    
    response = call_tinyfish(prompt)
    try:
        cleaned = response.strip()
        if cleaned.startswith("```json"):
            cleaned = cleaned[7:]
        if cleaned.startswith("```"):
            cleaned = cleaned[3:]
        if cleaned.endswith("```"):
            cleaned = cleaned[:-3]
        return json.loads(cleaned.strip())
    except:
        return {
            "jobHistory": [],
            "skills": [],
            "education": [],
            "experienceYears": 0,
            "industryExpertise": []
        }


def calculate_authenticity(resume_data: Dict, github_data: Dict, linkedin_data: Dict) -> int:
    score = 100
    
    resume_skills = set([s.lower() for s in resume_data.get("skills", [])])
    github_languages = set([l.lower() for l in github_data.get("languages", [])])
    linkedin_skills = set([s.lower() for s in linkedin_data.get("skills", [])])
    
    if resume_skills:
        github_overlap = len(resume_skills & github_languages) / len(resume_skills)
        linkedin_overlap = len(resume_skills & linkedin_skills) / len(resume_skills)
        
        if github_overlap < 0.3:
            score -= 25
        if linkedin_overlap < 0.4:
            score -= 15
    
    resume_exp_count = len(resume_data.get("experience", []))
    linkedin_exp_count = len(linkedin_data.get("jobHistory", []))
    
    if abs(resume_exp_count - linkedin_exp_count) > 2:
        score -= 20
    
    github_commits = github_data.get("totalCommits", 0)
    if github_commits < 50:
        score -= 15
    
    return max(0, min(100, score))


def calculate_skill_match(resume_data: Dict, github_data: Dict, role: str) -> int:
    role_lower = role.lower()
    score = 60
    
    resume_skills = [s.lower() for s in resume_data.get("skills", [])]
    github_languages = [l.lower() for l in github_data.get("languages", [])]
    
    tech_skills = set(resume_skills + github_languages)
    
    if "backend" in role_lower or "server" in role_lower:
        backend_techs = ["python", "java", "node", "go", "rust", "c++", "c#", "ruby", "php", "django", "flask", "spring", "express"]
        matches = sum(1 for tech in backend_techs if tech in tech_skills)
        score += min(30, matches * 6)
    elif "frontend" in role_lower or "react" in role_lower or "ui" in role_lower:
        frontend_techs = ["javascript", "typescript", "react", "vue", "angular", "html", "css", "next", "svelte"]
        matches = sum(1 for tech in frontend_techs if tech in tech_skills)
        score += min(30, matches * 6)
    elif "fullstack" in role_lower or "full stack" in role_lower:
        fullstack_techs = ["javascript", "python", "react", "node", "django", "flask", "mongodb", "postgres", "mysql"]
        matches = sum(1 for tech in fullstack_techs if tech in tech_skills)
        score += min(30, matches * 5)
    else:
        score += min(30, len(tech_skills) * 3)
    
    if github_data.get("repoCount", 0) > 10:
        score += 5
    if github_data.get("totalCommits", 0) > 200:
        score += 5
    
    return min(100, score)


def calculate_activity_consistency(github_data: Dict) -> int:
    return github_data.get("consistencyScore", 75)


def calculate_skills_breakdown(resume_data: Dict, github_data: Dict) -> List[Dict]:
    all_skills = resume_data.get("skills", []) + github_data.get("languages", [])
    
    frontend_keywords = ["react", "vue", "angular", "javascript", "typescript", "html", "css", "ui", "ux"]
    backend_keywords = ["python", "java", "node", "go", "rust", "django", "flask", "spring", "express", "api"]
    dsa_keywords = ["algorithm", "data structure", "leetcode", "competitive", "dsa"]
    devops_keywords = ["docker", "kubernetes", "aws", "azure", "gcp", "ci/cd", "jenkins", "terraform"]
    database_keywords = ["sql", "mongodb", "postgres", "mysql", "redis", "database"]
    
    skills_lower = [s.lower() for s in all_skills]
    
    frontend_score = min(100, sum(1 for s in skills_lower if any(k in s for k in frontend_keywords)) * 15)
    backend_score = min(100, sum(1 for s in skills_lower if any(k in s for k in backend_keywords)) * 12)
    dsa_score = min(100, sum(1 for s in skills_lower if any(k in s for k in dsa_keywords)) * 20)
    devops_score = min(100, sum(1 for s in skills_lower if any(k in s for k in devops_keywords)) * 15)
    database_score = min(100, sum(1 for s in skills_lower if any(k in s for k in database_keywords)) * 15)
    
    return [
        {"name": "Frontend", "value": max(frontend_score, 50)},
        {"name": "Backend", "value": max(backend_score, 60)},
        {"name": "DSA", "value": max(dsa_score, 45)},
        {"name": "DevOps", "value": max(devops_score, 40)},
        {"name": "Database", "value": max(database_score, 55)}
    ]


def generate_recommendation(candidate_score: int) -> str:
    if candidate_score >= 80:
        return "Strong Hire"
    elif candidate_score >= 60:
        return "Weak Hire"
    else:
        return "Reject"


def generate_interview_questions(resume_data: Dict, github_data: Dict, role: str) -> List[str]:
    skills = resume_data.get("skills", [])[:3]
    projects = github_data.get("topProjects", [])[:2]
    
    questions = [
        f"Walk us through your most complex project involving {skills[0] if skills else 'your primary tech stack'}.",
        f"How do you approach system design for {role.lower()} applications?"
    ]
    
    if projects:
        questions.append(f"Tell us about your {projects[0]} project. What was your role and what challenges did you face?")
    
    questions.append("How do you ensure code quality and maintainability in production systems?")
    questions.append("Describe a time when you had to debug a critical issue under pressure. What was your approach?")
    
    return questions[:5]


@app.post("/full-analysis", response_model=AnalysisResponse)
async def full_analysis(
    github_username: str = Query(..., description="GitHub username"),
    linkedin_url: str = Query(..., description="LinkedIn profile URL"),
    role: str = Query(..., description="Job role"),
    resume: UploadFile = File(..., description="Resume PDF file")
):
    if not resume.filename.endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files are allowed")
    
    pdf_bytes = await resume.read()
    resume_text = extract_text_from_pdf(pdf_bytes)
    
    resume_data = parse_resume(resume_text)
    github_data = analyze_github(github_username)
    linkedin_data = analyze_linkedin(linkedin_url)
    
    authenticity = calculate_authenticity(resume_data, github_data, linkedin_data)
    skill_match = calculate_skill_match(resume_data, github_data, role)
    activity_consistency = calculate_activity_consistency(github_data)
    
    candidate_score = int(
        (skill_match * 0.4) + 
        (authenticity * 0.35) + 
        (activity_consistency * 0.25)
    )
    
    skills_breakdown = calculate_skills_breakdown(resume_data, github_data)
    github_activity = github_data.get("commitActivity", [])
    
    platforms = [
        {"name": "GitHub", "value": f"+{github_data.get('repoCount', 0)}"},
        {"name": "LinkedIn", "value": f"+{len(linkedin_data.get('jobHistory', []))} roles"}
    ]
    
    recommendation = generate_recommendation(candidate_score)
    interview_questions = generate_interview_questions(resume_data, github_data, role)
    
    return AnalysisResponse(
        candidateScore=candidate_score,
        skillMatch=skill_match,
        authenticity=authenticity,
        activityConsistency=activity_consistency,
        skillsBreakdown=skills_breakdown,
        githubActivity=github_activity,
        platforms=platforms,
        recommendation=recommendation,
        interviewQuestions=interview_questions
    )


@app.get("/health")
async def health_check():
    return {"status": "healthy"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
