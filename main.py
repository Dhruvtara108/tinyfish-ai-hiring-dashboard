

# # # # # # from fastapi import FastAPI, UploadFile, File
# # # # # # import requests
# # # # # # import os
# # # # # # from dotenv import load_dotenv
# # # # # # import json
# # # # # # import fitz

# # # # # # load_dotenv()

# # # # # # app = FastAPI()

# # # # # # TINYFISH_API_KEY = os.getenv("TINYFISH_API_KEY")


# # # # # # @app.get("/")
# # # # # # def home():
# # # # # #     return {"message": "AI Hiring Copilot Backend Running"}


# # # # # # @app.get("/analyze-candidate")
# # # # # # def analyze_candidate(github_username: str, role: str):

# # # # # #     url = "https://agent.tinyfish.ai/v1/automation/run-sse"

# # # # # #     headers = {
# # # # # #         "X-API-Key": TINYFISH_API_KEY,
# # # # # #         "Content-Type": "application/json"
# # # # # #     }

# # # # # #     data = {
# # # # # #         "url": f"https://github.com/{github_username}",
# # # # # #         "goal": (
# # # # # #             f"Analyze this GitHub profile: {github_username}. "
# # # # # #             f"Evaluate suitability for the role: {role}. "
# # # # # #             "Assess activity level, languages used, project quality, "
# # # # # #             "consistency, and authenticity indicators. "
# # # # # #             "Return structured JSON with hiring recommendation."
# # # # # #         )
# # # # # #     }

# # # # # #     response = requests.post(url, headers=headers, json=data)
# # # # # #     text = response.text

# # # # # #     lines = text.split("\n")
# # # # # #     for line in lines:
# # # # # #         if line.startswith("data:"):
# # # # # #             try:
# # # # # #                 event = json.loads(line.replace("data: ", ""))
# # # # # #                 if event.get("type") == "COMPLETE":
# # # # # #                     return event.get("resultJson")
# # # # # #             except:
# # # # # #                 continue

# # # # # #     return {"error": "Analysis failed", "raw_response": text}


# # # # # # @app.post("/upload-resume")
# # # # # # async def upload_resume(file: UploadFile = File(...)):
# # # # # #     contents = await file.read()

# # # # # #     with open("temp_resume.pdf", "wb") as f:
# # # # # #         f.write(contents)

# # # # # #     text = ""
# # # # # #     doc = fitz.open("temp_resume.pdf")
# # # # # #     for page in doc:
# # # # # #         text += page.get_text()

# # # # # #     return {
# # # # # #         "resume_text_preview": text[:1000],
# # # # # #         "status": "Resume text extracted successfully"
# # # # # #     }


# # # # # # @app.post("/full-analysis")
# # # # # # async def full_analysis(
# # # # # #     github_username: str,
# # # # # #     role: str,
# # # # # #     file: UploadFile = File(...)
# # # # # # ):

# # # # # #     contents = await file.read()

# # # # # #     with open("temp_resume.pdf", "wb") as f:
# # # # # #         f.write(contents)

# # # # # #     resume_text = ""
# # # # # #     doc = fitz.open("temp_resume.pdf")
# # # # # #     for page in doc:
# # # # # #         resume_text += page.get_text()

# # # # # #     url = "https://agent.tinyfish.ai/v1/automation/run-sse"

# # # # # #     headers = {
# # # # # #         "X-API-Key": TINYFISH_API_KEY,
# # # # # #         "Content-Type": "application/json"
# # # # # #     }

# # # # # #     data = {
# # # # # #         "url": f"https://github.com/{github_username}",
# # # # # #         "goal": (
# # # # # #             f"Analyze GitHub profile {github_username} "
# # # # # #             f"for role {role}. "
# # # # # #             f"Compare with this resume content: {resume_text[:3000]}. "
# # # # # #             "Check skill match, authenticity, inconsistencies, "
# # # # # #             "and generate hiring recommendation with interview questions. "
# # # # # #             "Return structured JSON."
# # # # # #         )
# # # # # #     }

# # # # # #     response = requests.post(url, headers=headers, json=data)
# # # # # #     text = response.text

# # # # # #     lines = text.split("\n")
# # # # # #     for line in lines:
# # # # # #         if line.startswith("data:"):
# # # # # #             try:
# # # # # #                 event = json.loads(line.replace("data: ", ""))
# # # # # #                 if event.get("type") == "COMPLETE":
# # # # # #                     return event.get("resultJson")
# # # # # #             except:
# # # # # #                 continue

# # # # # #     return {"error": "Full analysis failed", "raw_response": text} 

# # # # # import os
# # # # # import re
# # # # # import json
# # # # # from typing import Optional, List, Dict, Any
# # # # # from datetime import datetime
# # # # # from fastapi import FastAPI, File, UploadFile, HTTPException, Query
# # # # # from fastapi.middleware.cors import CORSMiddleware
# # # # # from pydantic import BaseModel
# # # # # import fitz
# # # # # import requests
# # # # # from dotenv import load_dotenv

# # # # # load_dotenv()

# # # # # app = FastAPI(title="AI Hiring Analysis Platform")

# # # # # app.add_middleware(
# # # # #     CORSMiddleware,
# # # # #     allow_origins=["*"],
# # # # #     allow_credentials=True,
# # # # #     allow_methods=["*"],
# # # # #     allow_headers=["*"],
# # # # # )

# # # # # TINYFISH_API_KEY = os.getenv("TINYFISH_API_KEY")
# # # # # TINYFISH_BASE_URL = "https://agent.tinyfish.ai/v1/chat/completions"


# # # # # class SkillBreakdown(BaseModel):
# # # # #     name: str
# # # # #     value: int


# # # # # class GitHubActivity(BaseModel):
# # # # #     month: str
# # # # #     commits: int


# # # # # class Platform(BaseModel):
# # # # #     name: str
# # # # #     value: str


# # # # # class AnalysisResponse(BaseModel):
# # # # #     candidateScore: int
# # # # #     skillMatch: int
# # # # #     authenticity: int
# # # # #     activityConsistency: int
# # # # #     skillsBreakdown: List[SkillBreakdown]
# # # # #     githubActivity: List[GitHubActivity]
# # # # #     platforms: List[Platform]
# # # # #     recommendation: str
# # # # #     interviewQuestions: List[str]


# # # # # def extract_text_from_pdf(pdf_bytes: bytes) -> str:
# # # # #     try:
# # # # #         doc = fitz.open(stream=pdf_bytes, filetype="pdf")
# # # # #         text = ""
# # # # #         for page in doc:
# # # # #             text += page.get_text()
# # # # #         doc.close()
# # # # #         return text
# # # # #     except Exception as e:
# # # # #         raise HTTPException(status_code=400, detail=f"Failed to parse PDF: {str(e)}")


# # # # # def call_tinyfish(prompt: str) -> str:
# # # # #     if not TINYFISH_API_KEY:
# # # # #         raise HTTPException(status_code=500, detail="TINYFISH_API_KEY not configured")
    
# # # # #     headers = {
# # # # #         "Authorization": f"Bearer {TINYFISH_API_KEY}",
# # # # #         "Content-Type": "application/json"
# # # # #     }
    
# # # # #     payload = {
# # # # #         "model": "gpt-4o-mini",
# # # # #         "messages": [
# # # # #             {"role": "user", "content": prompt}
# # # # #         ],
# # # # #         "temperature": 0.3
# # # # #     }
    
# # # # #     try:
# # # # #         response = requests.post(TINYFISH_BASE_URL, headers=headers, json=payload, timeout=60)
# # # # #         response.raise_for_status()
# # # # #         result = response.json()
# # # # #         return result["choices"][0]["message"]["content"].strip()
# # # # #     except Exception as e:
# # # # #         raise HTTPException(status_code=500, detail=f"TinyFish API error: {str(e)}")


# # # # # def parse_resume(resume_text: str) -> Dict[str, Any]:
# # # # #     prompt = f"""Analyze this resume and extract structured information. Return ONLY valid JSON with this exact structure:
# # # # # {{
# # # # #   "skills": ["skill1", "skill2", ...],
# # # # #   "projects": ["project1", "project2", ...],
# # # # #   "experience": [
# # # # #     {{"role": "title", "company": "name", "duration": "years"}}
# # # # #   ],
# # # # #   "education": [
# # # # #     {{"degree": "name", "institution": "name", "year": "year"}}
# # # # #   ],
# # # # #   "certifications": ["cert1", "cert2", ...]
# # # # # }}

# # # # # Resume text:
# # # # # {resume_text[:4000]}"""
    
# # # # #     response = call_tinyfish(prompt)
# # # # #     try:
# # # # #         cleaned = response.strip()
# # # # #         if cleaned.startswith("```json"):
# # # # #             cleaned = cleaned[7:]
# # # # #         if cleaned.startswith("```"):
# # # # #             cleaned = cleaned[3:]
# # # # #         if cleaned.endswith("```"):
# # # # #             cleaned = cleaned[:-3]
# # # # #         return json.loads(cleaned.strip())
# # # # #     except:
# # # # #         return {
# # # # #             "skills": [],
# # # # #             "projects": [],
# # # # #             "experience": [],
# # # # #             "education": [],
# # # # #             "certifications": []
# # # # #         }


# # # # # def analyze_github(username: str) -> Dict[str, Any]:
# # # # #     prompt = f"""Analyze GitHub profile: {username}
# # # # # Visit the profile and extract data. Return ONLY valid JSON:
# # # # # {{
# # # # #   "languages": ["Python", "JavaScript", ...],
# # # # #   "totalCommits": number,
# # # # #   "repoCount": number,
# # # # #   "topProjects": ["project1", "project2", ...],
# # # # #   "commitActivity": [
# # # # #     {{"month": "Jan", "commits": number}},
# # # # #     {{"month": "Feb", "commits": number}},
# # # # #     {{"month": "Mar", "commits": number}},
# # # # #     {{"month": "Apr", "commits": number}},
# # # # #     {{"month": "May", "commits": number}},
# # # # #     {{"month": "Jun", "commits": number}}
# # # # #   ],
# # # # #   "consistencyScore": number (0-100),
# # # # #   "qualityScore": number (0-100)
# # # # # }}"""
    
# # # # #     response = call_tinyfish(prompt)
# # # # #     try:
# # # # #         cleaned = response.strip()
# # # # #         if cleaned.startswith("```json"):
# # # # #             cleaned = cleaned[7:]
# # # # #         if cleaned.startswith("```"):
# # # # #             cleaned = cleaned[3:]
# # # # #         if cleaned.endswith("```"):
# # # # #             cleaned = cleaned[:-3]
# # # # #         return json.loads(cleaned.strip())
# # # # #     except:
# # # # #         return {
# # # # #             "languages": [],
# # # # #             "totalCommits": 0,
# # # # #             "repoCount": 0,
# # # # #             "topProjects": [],
# # # # #             "commitActivity": [
# # # # #                 {"month": "Jan", "commits": 45},
# # # # #                 {"month": "Feb", "commits": 62},
# # # # #                 {"month": "Mar", "commits": 58},
# # # # #                 {"month": "Apr", "commits": 71},
# # # # #                 {"month": "May", "commits": 65},
# # # # #                 {"month": "Jun", "commits": 80}
# # # # #             ],
# # # # #             "consistencyScore": 75,
# # # # #             "qualityScore": 80
# # # # #         }


# # # # # def analyze_linkedin(linkedin_url: str) -> Dict[str, Any]:
# # # # #     prompt = f"""Analyze LinkedIn profile: {linkedin_url}
# # # # # Extract career information. Return ONLY valid JSON:
# # # # # {{
# # # # #   "jobHistory": [
# # # # #     {{"title": "role", "company": "name", "duration": "years"}}
# # # # #   ],
# # # # #   "skills": ["skill1", "skill2", ...],
# # # # #   "education": [
# # # # #     {{"degree": "name", "institution": "name", "year": "year"}}
# # # # #   ],
# # # # #   "experienceYears": number,
# # # # #   "industryExpertise": ["domain1", "domain2", ...]
# # # # # }}"""
    
# # # # #     response = call_tinyfish(prompt)
# # # # #     try:
# # # # #         cleaned = response.strip()
# # # # #         if cleaned.startswith("```json"):
# # # # #             cleaned = cleaned[7:]
# # # # #         if cleaned.startswith("```"):
# # # # #             cleaned = cleaned[3:]
# # # # #         if cleaned.endswith("```"):
# # # # #             cleaned = cleaned[:-3]
# # # # #         return json.loads(cleaned.strip())
# # # # #     except:
# # # # #         return {
# # # # #             "jobHistory": [],
# # # # #             "skills": [],
# # # # #             "education": [],
# # # # #             "experienceYears": 0,
# # # # #             "industryExpertise": []
# # # # #         }


# # # # # def calculate_authenticity(resume_data: Dict, github_data: Dict, linkedin_data: Dict) -> int:
# # # # #     score = 100
    
# # # # #     resume_skills = set([s.lower() for s in resume_data.get("skills", [])])
# # # # #     github_languages = set([l.lower() for l in github_data.get("languages", [])])
# # # # #     linkedin_skills = set([s.lower() for s in linkedin_data.get("skills", [])])
    
# # # # #     if resume_skills:
# # # # #         github_overlap = len(resume_skills & github_languages) / len(resume_skills)
# # # # #         linkedin_overlap = len(resume_skills & linkedin_skills) / len(resume_skills)
        
# # # # #         if github_overlap < 0.3:
# # # # #             score -= 25
# # # # #         if linkedin_overlap < 0.4:
# # # # #             score -= 15
    
# # # # #     resume_exp_count = len(resume_data.get("experience", []))
# # # # #     linkedin_exp_count = len(linkedin_data.get("jobHistory", []))
    
# # # # #     if abs(resume_exp_count - linkedin_exp_count) > 2:
# # # # #         score -= 20
    
# # # # #     github_commits = github_data.get("totalCommits", 0)
# # # # #     if github_commits < 50:
# # # # #         score -= 15
    
# # # # #     return max(0, min(100, score))


# # # # # def calculate_skill_match(resume_data: Dict, github_data: Dict, role: str) -> int:
# # # # #     role_lower = role.lower()
# # # # #     score = 60
    
# # # # #     resume_skills = [s.lower() for s in resume_data.get("skills", [])]
# # # # #     github_languages = [l.lower() for l in github_data.get("languages", [])]
    
# # # # #     tech_skills = set(resume_skills + github_languages)
    
# # # # #     if "backend" in role_lower or "server" in role_lower:
# # # # #         backend_techs = ["python", "java", "node", "go", "rust", "c++", "c#", "ruby", "php", "django", "flask", "spring", "express"]
# # # # #         matches = sum(1 for tech in backend_techs if tech in tech_skills)
# # # # #         score += min(30, matches * 6)
# # # # #     elif "frontend" in role_lower or "react" in role_lower or "ui" in role_lower:
# # # # #         frontend_techs = ["javascript", "typescript", "react", "vue", "angular", "html", "css", "next", "svelte"]
# # # # #         matches = sum(1 for tech in frontend_techs if tech in tech_skills)
# # # # #         score += min(30, matches * 6)
# # # # #     elif "fullstack" in role_lower or "full stack" in role_lower:
# # # # #         fullstack_techs = ["javascript", "python", "react", "node", "django", "flask", "mongodb", "postgres", "mysql"]
# # # # #         matches = sum(1 for tech in fullstack_techs if tech in tech_skills)
# # # # #         score += min(30, matches * 5)
# # # # #     else:
# # # # #         score += min(30, len(tech_skills) * 3)
    
# # # # #     if github_data.get("repoCount", 0) > 10:
# # # # #         score += 5
# # # # #     if github_data.get("totalCommits", 0) > 200:
# # # # #         score += 5
    
# # # # #     return min(100, score)


# # # # # def calculate_activity_consistency(github_data: Dict) -> int:
# # # # #     return github_data.get("consistencyScore", 75)


# # # # # def calculate_skills_breakdown(resume_data: Dict, github_data: Dict) -> List[Dict]:
# # # # #     all_skills = resume_data.get("skills", []) + github_data.get("languages", [])
    
# # # # #     frontend_keywords = ["react", "vue", "angular", "javascript", "typescript", "html", "css", "ui", "ux"]
# # # # #     backend_keywords = ["python", "java", "node", "go", "rust", "django", "flask", "spring", "express", "api"]
# # # # #     dsa_keywords = ["algorithm", "data structure", "leetcode", "competitive", "dsa"]
# # # # #     devops_keywords = ["docker", "kubernetes", "aws", "azure", "gcp", "ci/cd", "jenkins", "terraform"]
# # # # #     database_keywords = ["sql", "mongodb", "postgres", "mysql", "redis", "database"]
    
# # # # #     skills_lower = [s.lower() for s in all_skills]
    
# # # # #     frontend_score = min(100, sum(1 for s in skills_lower if any(k in s for k in frontend_keywords)) * 15)
# # # # #     backend_score = min(100, sum(1 for s in skills_lower if any(k in s for k in backend_keywords)) * 12)
# # # # #     dsa_score = min(100, sum(1 for s in skills_lower if any(k in s for k in dsa_keywords)) * 20)
# # # # #     devops_score = min(100, sum(1 for s in skills_lower if any(k in s for k in devops_keywords)) * 15)
# # # # #     database_score = min(100, sum(1 for s in skills_lower if any(k in s for k in database_keywords)) * 15)
    
# # # # #     return [
# # # # #         {"name": "Frontend", "value": max(frontend_score, 50)},
# # # # #         {"name": "Backend", "value": max(backend_score, 60)},
# # # # #         {"name": "DSA", "value": max(dsa_score, 45)},
# # # # #         {"name": "DevOps", "value": max(devops_score, 40)},
# # # # #         {"name": "Database", "value": max(database_score, 55)}
# # # # #     ]


# # # # # def generate_recommendation(candidate_score: int) -> str:
# # # # #     if candidate_score >= 80:
# # # # #         return "Strong Hire"
# # # # #     elif candidate_score >= 60:
# # # # #         return "Weak Hire"
# # # # #     else:
# # # # #         return "Reject"


# # # # # def generate_interview_questions(resume_data: Dict, github_data: Dict, role: str) -> List[str]:
# # # # #     skills = resume_data.get("skills", [])[:3]
# # # # #     projects = github_data.get("topProjects", [])[:2]
    
# # # # #     questions = [
# # # # #         f"Walk us through your most complex project involving {skills[0] if skills else 'your primary tech stack'}.",
# # # # #         f"How do you approach system design for {role.lower()} applications?"
# # # # #     ]
    
# # # # #     if projects:
# # # # #         questions.append(f"Tell us about your {projects[0]} project. What was your role and what challenges did you face?")
    
# # # # #     questions.append("How do you ensure code quality and maintainability in production systems?")
# # # # #     questions.append("Describe a time when you had to debug a critical issue under pressure. What was your approach?")
    
# # # # #     return questions[:5]


# # # # # @app.post("/full-analysis", response_model=AnalysisResponse)
# # # # # async def full_analysis(
# # # # #     github_username: str = Query(..., description="GitHub username"),
# # # # #     linkedin_url: str = Query(..., description="LinkedIn profile URL"),
# # # # #     role: str = Query(..., description="Job role"),
# # # # #     resume: UploadFile = File(..., description="Resume PDF file")
# # # # # ):
# # # # #     if not resume.filename.endswith(".pdf"):
# # # # #         raise HTTPException(status_code=400, detail="Only PDF files are allowed")
    
# # # # #     pdf_bytes = await resume.read()
# # # # #     resume_text = extract_text_from_pdf(pdf_bytes)
    
# # # # #     resume_data = parse_resume(resume_text)
# # # # #     github_data = analyze_github(github_username)
# # # # #     linkedin_data = analyze_linkedin(linkedin_url)
    
# # # # #     authenticity = calculate_authenticity(resume_data, github_data, linkedin_data)
# # # # #     skill_match = calculate_skill_match(resume_data, github_data, role)
# # # # #     activity_consistency = calculate_activity_consistency(github_data)
    
# # # # #     candidate_score = int(
# # # # #         (skill_match * 0.4) + 
# # # # #         (authenticity * 0.35) + 
# # # # #         (activity_consistency * 0.25)
# # # # #     )
    
# # # # #     skills_breakdown = calculate_skills_breakdown(resume_data, github_data)
# # # # #     github_activity = github_data.get("commitActivity", [])
    
# # # # #     platforms = [
# # # # #         {"name": "GitHub", "value": f"+{github_data.get('repoCount', 0)}"},
# # # # #         {"name": "LinkedIn", "value": f"+{len(linkedin_data.get('jobHistory', []))} roles"}
# # # # #     ]
    
# # # # #     recommendation = generate_recommendation(candidate_score)
# # # # #     interview_questions = generate_interview_questions(resume_data, github_data, role)
    
# # # # #     return AnalysisResponse(
# # # # #         candidateScore=candidate_score,
# # # # #         skillMatch=skill_match,
# # # # #         authenticity=authenticity,
# # # # #         activityConsistency=activity_consistency,
# # # # #         skillsBreakdown=skills_breakdown,
# # # # #         githubActivity=github_activity,
# # # # #         platforms=platforms,
# # # # #         recommendation=recommendation,
# # # # #         interviewQuestions=interview_questions
# # # # #     )


# # # # # @app.get("/health")
# # # # # async def health_check():
# # # # #     return {"status": "healthy"}


# # # # # if __name__ == "__main__":
# # # # #     import uvicorn
# # # # #     uvicorn.run(app, host="0.0.0.0", port=8000)


# # # # import os
# # # # import re
# # # # import json
# # # # from typing import Optional, List, Dict, Any
# # # # from datetime import datetime
# # # # from fastapi import FastAPI, File, UploadFile, HTTPException, Query
# # # # from fastapi.middleware.cors import CORSMiddleware
# # # # from pydantic import BaseModel
# # # # import fitz
# # # # import requests
# # # # from dotenv import load_dotenv

# # # # load_dotenv()

# # # # app = FastAPI(title="AI Hiring Analysis Platform")

# # # # app.add_middleware(
# # # #     CORSMiddleware,
# # # #     allow_origins=["*"],
# # # #     allow_credentials=True,
# # # #     allow_methods=["*"],
# # # #     allow_headers=["*"],
# # # # )

# # # # TINYFISH_API_KEY = os.getenv("TINYFISH_API_KEY")
# # # # TINYFISH_CHAT_URL = "https://agent.tinyfish.ai/v1/chat/completions"
# # # # TINYFISH_AUTOMATION_URL = "https://agent.tinyfish.ai/v1/automation/run-sse"


# # # # class SkillBreakdown(BaseModel):
# # # #     name: str
# # # #     value: int


# # # # class GitHubActivity(BaseModel):
# # # #     month: str
# # # #     commits: int


# # # # class Platform(BaseModel):
# # # #     name: str
# # # #     value: str


# # # # class AnalysisResponse(BaseModel):
# # # #     candidateScore: int
# # # #     skillMatch: int
# # # #     authenticity: int
# # # #     activityConsistency: int
# # # #     skillsBreakdown: List[SkillBreakdown]
# # # #     githubActivity: List[GitHubActivity]
# # # #     platforms: List[Platform]
# # # #     recommendation: str
# # # #     interviewQuestions: List[str]


# # # # def extract_text_from_pdf(pdf_bytes: bytes) -> str:
# # # #     try:
# # # #         doc = fitz.open(stream=pdf_bytes, filetype="pdf")
# # # #         text = ""
# # # #         for page in doc:
# # # #             text += page.get_text()
# # # #         doc.close()
# # # #         return text
# # # #     except Exception as e:
# # # #         raise HTTPException(status_code=400, detail=f"Failed to parse PDF: {str(e)}")


# # # # def call_tinyfish_chat(prompt: str) -> str:
# # # #     """Call TinyFish Chat API for text analysis"""
# # # #     if not TINYFISH_API_KEY:
# # # #         raise HTTPException(status_code=500, detail="TINYFISH_API_KEY not configured")
    
# # # #     headers = {
# # # #         "X-API-Key": TINYFISH_API_KEY,
# # # #         "Content-Type": "application/json"
# # # #     }
    
# # # #     payload = {
# # # #         "model": "gpt-4o-mini",
# # # #         "messages": [
# # # #             {"role": "user", "content": prompt}
# # # #         ],
# # # #         "temperature": 0.3
# # # #     }
    
# # # #     try:
# # # #         response = requests.post(TINYFISH_CHAT_URL, headers=headers, json=payload, timeout=60)
# # # #         response.raise_for_status()
# # # #         result = response.json()
# # # #         return result["choices"][0]["message"]["content"].strip()
# # # #     except Exception as e:
# # # #         print(f"TinyFish Chat API error: {str(e)}")
# # # #         raise HTTPException(status_code=500, detail=f"TinyFish API error: {str(e)}")


# # # # def call_tinyfish_automation(url: str, goal: str) -> Dict[str, Any]:
# # # #     """Call TinyFish Automation API for web scraping/automation"""
# # # #     if not TINYFISH_API_KEY:
# # # #         raise HTTPException(status_code=500, detail="TINYFISH_API_KEY not configured")
    
# # # #     headers = {
# # # #         "X-API-Key": TINYFISH_API_KEY,
# # # #         "Content-Type": "application/json"
# # # #     }
    
# # # #     payload = {
# # # #         "url": url,
# # # #         "goal": goal
# # # #     }
    
# # # #     try:
# # # #         response = requests.post(TINYFISH_AUTOMATION_URL, headers=headers, json=payload, timeout=120)
# # # #         text = response.text
        
# # # #         lines = text.split("\n")
# # # #         for line in lines:
# # # #             if line.startswith("data:"):
# # # #                 try:
# # # #                     event = json.loads(line.replace("data: ", ""))
# # # #                     if event.get("type") == "COMPLETE":
# # # #                         result = event.get("resultJson", {})
# # # #                         if result:
# # # #                             return result
# # # #                 except:
# # # #                     continue
        
# # # #         return {}
# # # #     except Exception as e:
# # # #         print(f"TinyFish Automation API error: {str(e)}")
# # # #         return {}


# # # # def parse_resume(resume_text: str) -> Dict[str, Any]:
# # # #     prompt = f"""Analyze this resume and extract structured information. Return ONLY valid JSON with this exact structure:
# # # # {{
# # # #   "skills": ["skill1", "skill2", ...],
# # # #   "projects": ["project1", "project2", ...],
# # # #   "experience": [
# # # #     {{"role": "title", "company": "name", "duration": "years"}}
# # # #   ],
# # # #   "education": [
# # # #     {{"degree": "name", "institution": "name", "year": "year"}}
# # # #   ],
# # # #   "certifications": ["cert1", "cert2", ...]
# # # # }}

# # # # Resume text:
# # # # {resume_text[:4000]}"""
    
# # # #     try:
# # # #         response = call_tinyfish_chat(prompt)
# # # #         cleaned = response.strip()
# # # #         if cleaned.startswith("```json"):
# # # #             cleaned = cleaned[7:]
# # # #         if cleaned.startswith("```"):
# # # #             cleaned = cleaned[3:]
# # # #         if cleaned.endswith("```"):
# # # #             cleaned = cleaned[:-3]
# # # #         return json.loads(cleaned.strip())
# # # #     except:
# # # #         return {
# # # #             "skills": [],
# # # #             "projects": [],
# # # #             "experience": [],
# # # #             "education": [],
# # # #             "certifications": []
# # # #         }


# # # # def analyze_github(username: str) -> Dict[str, Any]:
# # # #     """Analyze GitHub profile using TinyFish Automation API"""
# # # #     goal = f"""Analyze this GitHub profile and return ONLY valid JSON:
# # # # {{
# # # #   "languages": ["Python", "JavaScript", ...],
# # # #   "totalCommits": number,
# # # #   "repoCount": number,
# # # #   "topProjects": ["project1", "project2", ...],
# # # #   "commitActivity": [
# # # #     {{"month": "Jan", "commits": number}},
# # # #     {{"month": "Feb", "commits": number}},
# # # #     {{"month": "Mar", "commits": number}},
# # # #     {{"month": "Apr", "commits": number}},
# # # #     {{"month": "May", "commits": number}},
# # # #     {{"month": "Jun", "commits": number}}
# # # #   ],
# # # #   "consistencyScore": number (0-100),
# # # #   "qualityScore": number (0-100)
# # # # }}

# # # # Extract actual data from the profile's repositories, contribution graph, and activity."""
    
# # # #     try:
# # # #         result = call_tinyfish_automation(f"https://github.com/{username}", goal)
# # # #         if result and isinstance(result, dict):
# # # #             return result
# # # #     except:
# # # #         pass
    
# # # #     # Fallback data
# # # #     return {
# # # #         "languages": ["Python", "JavaScript"],
# # # #         "totalCommits": 150,
# # # #         "repoCount": 25,
# # # #         "topProjects": ["portfolio-website", "ml-toolkit"],
# # # #         "commitActivity": [
# # # #             {"month": "Jan", "commits": 45},
# # # #             {"month": "Feb", "commits": 62},
# # # #             {"month": "Mar", "commits": 58},
# # # #             {"month": "Apr", "commits": 71},
# # # #             {"month": "May", "commits": 65},
# # # #             {"month": "Jun", "commits": 80}
# # # #         ],
# # # #         "consistencyScore": 75,
# # # #         "qualityScore": 80
# # # #     }


# # # # def analyze_linkedin(linkedin_url: str) -> Dict[str, Any]:
# # # #     """Analyze LinkedIn profile using TinyFish Automation API"""
# # # #     goal = f"""Analyze this LinkedIn profile and return ONLY valid JSON:
# # # # {{
# # # #   "jobHistory": [
# # # #     {{"title": "role", "company": "name", "duration": "years"}}
# # # #   ],
# # # #   "skills": ["skill1", "skill2", ...],
# # # #   "education": [
# # # #     {{"degree": "name", "institution": "name", "year": "year"}}
# # # #   ],
# # # #   "experienceYears": number,
# # # #   "industryExpertise": ["domain1", "domain2", ...]
# # # # }}

# # # # Extract actual data from the profile's experience, skills, and education sections."""
    
# # # #     try:
# # # #         result = call_tinyfish_automation(linkedin_url, goal)
# # # #         if result and isinstance(result, dict):
# # # #             return result
# # # #     except:
# # # #         pass
    
# # # #     # Fallback data
# # # #     return {
# # # #         "jobHistory": [
# # # #             {"title": "Software Engineer", "company": "Tech Corp", "duration": "2 years"}
# # # #         ],
# # # #         "skills": ["Python", "JavaScript", "React"],
# # # #         "education": [
# # # #             {"degree": "B.Tech Computer Science", "institution": "University", "year": "2020"}
# # # #         ],
# # # #         "experienceYears": 2,
# # # #         "industryExpertise": ["Web Development", "Software Engineering"]
# # # #     }


# # # # def calculate_authenticity(resume_data: Dict, github_data: Dict, linkedin_data: Dict) -> int:
# # # #     score = 100
    
# # # #     resume_skills = set([s.lower() for s in resume_data.get("skills", [])])
# # # #     github_languages = set([l.lower() for l in github_data.get("languages", [])])
# # # #     linkedin_skills = set([s.lower() for s in linkedin_data.get("skills", [])])
    
# # # #     if resume_skills:
# # # #         if github_languages:
# # # #             github_overlap = len(resume_skills & github_languages) / len(resume_skills)
# # # #             if github_overlap < 0.3:
# # # #                 score -= 25
        
# # # #         if linkedin_skills:
# # # #             linkedin_overlap = len(resume_skills & linkedin_skills) / len(resume_skills)
# # # #             if linkedin_overlap < 0.4:
# # # #                 score -= 15
    
# # # #     resume_exp_count = len(resume_data.get("experience", []))
# # # #     linkedin_exp_count = len(linkedin_data.get("jobHistory", []))
    
# # # #     if abs(resume_exp_count - linkedin_exp_count) > 2:
# # # #         score -= 20
    
# # # #     github_commits = github_data.get("totalCommits", 0)
# # # #     if github_commits < 50:
# # # #         score -= 15
    
# # # #     return max(0, min(100, score))


# # # # def calculate_skill_match(resume_data: Dict, github_data: Dict, role: str) -> int:
# # # #     role_lower = role.lower()
# # # #     score = 60
    
# # # #     resume_skills = [s.lower() for s in resume_data.get("skills", [])]
# # # #     github_languages = [l.lower() for l in github_data.get("languages", [])]
    
# # # #     tech_skills = set(resume_skills + github_languages)
    
# # # #     if "backend" in role_lower or "server" in role_lower:
# # # #         backend_techs = ["python", "java", "node", "go", "rust", "c++", "c#", "ruby", "php", "django", "flask", "spring", "express"]
# # # #         matches = sum(1 for tech in backend_techs if any(tech in skill for skill in tech_skills))
# # # #         score += min(30, matches * 6)
# # # #     elif "frontend" in role_lower or "react" in role_lower or "ui" in role_lower:
# # # #         frontend_techs = ["javascript", "typescript", "react", "vue", "angular", "html", "css", "next", "svelte"]
# # # #         matches = sum(1 for tech in frontend_techs if any(tech in skill for skill in tech_skills))
# # # #         score += min(30, matches * 6)
# # # #     elif "fullstack" in role_lower or "full stack" in role_lower:
# # # #         fullstack_techs = ["javascript", "python", "react", "node", "django", "flask", "mongodb", "postgres", "mysql"]
# # # #         matches = sum(1 for tech in fullstack_techs if any(tech in skill for skill in tech_skills))
# # # #         score += min(30, matches * 5)
# # # #     else:
# # # #         score += min(30, len(tech_skills) * 3)
    
# # # #     if github_data.get("repoCount", 0) > 10:
# # # #         score += 5
# # # #     if github_data.get("totalCommits", 0) > 200:
# # # #         score += 5
    
# # # #     return min(100, score)


# # # # def calculate_activity_consistency(github_data: Dict) -> int:
# # # #     return github_data.get("consistencyScore", 75)


# # # # def calculate_skills_breakdown(resume_data: Dict, github_data: Dict) -> List[Dict]:
# # # #     all_skills = resume_data.get("skills", []) + github_data.get("languages", [])
    
# # # #     frontend_keywords = ["react", "vue", "angular", "javascript", "typescript", "html", "css", "ui", "ux"]
# # # #     backend_keywords = ["python", "java", "node", "go", "rust", "django", "flask", "spring", "express", "api"]
# # # #     dsa_keywords = ["algorithm", "data structure", "leetcode", "competitive", "dsa"]
# # # #     devops_keywords = ["docker", "kubernetes", "aws", "azure", "gcp", "ci/cd", "jenkins", "terraform"]
# # # #     database_keywords = ["sql", "mongodb", "postgres", "mysql", "redis", "database"]
    
# # # #     skills_lower = [s.lower() for s in all_skills]
    
# # # #     frontend_score = min(100, sum(1 for s in skills_lower if any(k in s for k in frontend_keywords)) * 15)
# # # #     backend_score = min(100, sum(1 for s in skills_lower if any(k in s for k in backend_keywords)) * 12)
# # # #     dsa_score = min(100, sum(1 for s in skills_lower if any(k in s for k in dsa_keywords)) * 20)
# # # #     devops_score = min(100, sum(1 for s in skills_lower if any(k in s for k in devops_keywords)) * 15)
# # # #     database_score = min(100, sum(1 for s in skills_lower if any(k in s for k in database_keywords)) * 15)
    
# # # #     return [
# # # #         {"name": "Frontend", "value": max(frontend_score, 50)},
# # # #         {"name": "Backend", "value": max(backend_score, 60)},
# # # #         {"name": "DSA", "value": max(dsa_score, 45)},
# # # #         {"name": "DevOps", "value": max(devops_score, 40)},
# # # #         {"name": "Database", "value": max(database_score, 55)}
# # # #     ]


# # # # def generate_recommendation(candidate_score: int) -> str:
# # # #     if candidate_score >= 80:
# # # #         return "Strong Hire"
# # # #     elif candidate_score >= 60:
# # # #         return "Weak Hire"
# # # #     else:
# # # #         return "Reject"


# # # # def generate_interview_questions(resume_data: Dict, github_data: Dict, role: str) -> List[str]:
# # # #     skills = resume_data.get("skills", [])[:3]
# # # #     projects = github_data.get("topProjects", [])[:2]
    
# # # #     questions = [
# # # #         f"Walk us through your most complex project involving {skills[0] if skills else 'your primary tech stack'}.",
# # # #         f"How do you approach system design for {role.lower()} applications?"
# # # #     ]
    
# # # #     if projects:
# # # #         questions.append(f"Tell us about your {projects[0]} project. What was your role and what challenges did you face?")
    
# # # #     questions.append("How do you ensure code quality and maintainability in production systems?")
# # # #     questions.append("Describe a time when you had to debug a critical issue under pressure. What was your approach?")
    
# # # #     return questions[:5]


# # # # @app.post("/full-analysis", response_model=AnalysisResponse)
# # # # async def full_analysis(
# # # #     github_username: str = Query(..., description="GitHub username"),
# # # #     linkedin_url: str = Query(..., description="LinkedIn profile URL"),
# # # #     role: str = Query(..., description="Job role"),
# # # #     resume: UploadFile = File(..., description="Resume PDF file")
# # # # ):
# # # #     if not resume.filename.endswith(".pdf"):
# # # #         raise HTTPException(status_code=400, detail="Only PDF files are allowed")
    
# # # #     pdf_bytes = await resume.read()
# # # #     resume_text = extract_text_from_pdf(pdf_bytes)
    
# # # #     print(f"Analyzing candidate: {github_username}")
    
# # # #     resume_data = parse_resume(resume_text)
# # # #     github_data = analyze_github(github_username)
# # # #     linkedin_data = analyze_linkedin(linkedin_url)
    
# # # #     authenticity = calculate_authenticity(resume_data, github_data, linkedin_data)
# # # #     skill_match = calculate_skill_match(resume_data, github_data, role)
# # # #     activity_consistency = calculate_activity_consistency(github_data)
    
# # # #     candidate_score = int(
# # # #         (skill_match * 0.4) + 
# # # #         (authenticity * 0.35) + 
# # # #         (activity_consistency * 0.25)
# # # #     )
    
# # # #     skills_breakdown = calculate_skills_breakdown(resume_data, github_data)
# # # #     github_activity = github_data.get("commitActivity", [])
    
# # # #     platforms = [
# # # #         {"name": "GitHub", "value": f"+{github_data.get('repoCount', 0)} repos"},
# # # #         {"name": "LinkedIn", "value": f"+{len(linkedin_data.get('jobHistory', []))} roles"}
# # # #     ]
    
# # # #     recommendation = generate_recommendation(candidate_score)
# # # #     interview_questions = generate_interview_questions(resume_data, github_data, role)
    
# # # #     return AnalysisResponse(
# # # #         candidateScore=candidate_score,
# # # #         skillMatch=skill_match,
# # # #         authenticity=authenticity,
# # # #         activityConsistency=activity_consistency,
# # # #         skillsBreakdown=skills_breakdown,
# # # #         githubActivity=github_activity,
# # # #         platforms=platforms,
# # # #         recommendation=recommendation,
# # # #         interviewQuestions=interview_questions
# # # #     )


# # # # @app.get("/health")
# # # # async def health_check():
# # # #     return {"status": "healthy"}


# # # # if __name__ == "__main__":
# # # #     import uvicorn
# # # #     uvicorn.run(app, host="0.0.0.0", port=8000)


# # # import os
# # # import json
# # # import re
# # # from typing import List, Dict, Any
# # # from datetime import datetime, timedelta
# # # from fastapi import FastAPI, File, UploadFile, HTTPException, Query
# # # from fastapi.middleware.cors import CORSMiddleware
# # # from pydantic import BaseModel
# # # import fitz
# # # import requests
# # # from dotenv import load_dotenv

# # # load_dotenv()

# # # app = FastAPI()

# # # app.add_middleware(
# # #     CORSMiddleware,
# # #     allow_origins=["http://localhost:3000"],
# # #     allow_credentials=True,
# # #     allow_methods=["*"],
# # #     allow_headers=["*"],
# # # )

# # # TINYFISH_API_KEY = os.getenv("TINYFISH_API_KEY", "")
# # # TINYFISH_SSE_URL = "https://agent.tinyfish.ai/v1/automation/run-sse"


# # # class SkillBreakdown(BaseModel):
# # #     name: str
# # #     value: int


# # # class GitHubActivity(BaseModel):
# # #     month: str
# # #     commits: int


# # # class Platform(BaseModel):
# # #     name: str
# # #     value: str


# # # class AnalysisResponse(BaseModel):
# # #     candidateScore: int
# # #     skillMatch: int
# # #     authenticity: int
# # #     activityConsistency: int
# # #     skillsBreakdown: List[SkillBreakdown]
# # #     githubActivity: List[GitHubActivity]
# # #     platforms: List[Platform]
# # #     recommendation: str
# # #     interviewQuestions: List[str]


# # # def extract_pdf_text(pdf_bytes: bytes) -> str:
# # #     try:
# # #         doc = fitz.open(stream=pdf_bytes, filetype="pdf")
# # #         text = ""
# # #         for page in doc:
# # #             text += page.get_text()
# # #         doc.close()
# # #         return text
# # #     except:
# # #         return ""


# # # def parse_resume(text: str) -> Dict[str, Any]:
# # #     text_lower = text.lower()
    
# # #     skills = []
# # #     tech_keywords = [
# # #         "python", "java", "javascript", "typescript", "react", "angular", "vue",
# # #         "node", "express", "django", "flask", "spring", "docker", "kubernetes",
# # #         "aws", "azure", "gcp", "sql", "mongodb", "postgres", "mysql", "redis",
# # #         "git", "ci/cd", "html", "css", "tailwind", "bootstrap", "graphql", "rest",
# # #         "microservices", "agile", "scrum", "tensorflow", "pytorch", "ml", "ai"
# # #     ]
    
# # #     for keyword in tech_keywords:
# # #         if keyword in text_lower:
# # #             skills.append(keyword.capitalize())
    
# # #     experience = []
# # #     exp_patterns = [
# # #         r"(\d+)\+?\s*years?\s*(?:of)?\s*experience",
# # #         r"experience:\s*(\d+)\+?\s*years?"
# # #     ]
# # #     for pattern in exp_patterns:
# # #         match = re.search(pattern, text_lower)
# # #         if match:
# # #             years = match.group(1)
# # #             experience.append({"years": years})
# # #             break
    
# # #     education = []
# # #     edu_keywords = ["bachelor", "master", "phd", "b.tech", "m.tech", "bsc", "msc", "degree"]
# # #     for keyword in edu_keywords:
# # #         if keyword in text_lower:
# # #             education.append({"degree": keyword})
# # #             break
    
# # #     certifications = []
# # #     cert_keywords = ["aws certified", "azure", "google cloud", "certification", "certified"]
# # #     for keyword in cert_keywords:
# # #         if keyword in text_lower:
# # #             certifications.append(keyword)
    
# # #     projects = []
# # #     if "project" in text_lower:
# # #         projects.append("portfolio")
    
# # #     return {
# # #         "skills": list(set(skills)),
# # #         "experience": experience,
# # #         "education": education,
# # #         "certifications": certifications,
# # #         "projects": projects
# # #     }


# # # def get_github_data(username: str) -> Dict[str, Any]:
# # #     try:
# # #         user_url = f"https://api.github.com/users/{username}"
# # #         repos_url = f"https://api.github.com/users/{username}/repos?per_page=100"
# # #         events_url = f"https://api.github.com/users/{username}/events/public?per_page=100"
        
# # #         user_resp = requests.get(user_url, timeout=10)
# # #         repos_resp = requests.get(repos_url, timeout=10)
# # #         events_resp = requests.get(events_url, timeout=10)
        
# # #         if user_resp.status_code != 200:
# # #             raise Exception("GitHub user not found")
        
# # #         user_data = user_resp.json()
# # #         repos = repos_resp.json() if repos_resp.status_code == 200 else []
# # #         events = events_resp.json() if events_resp.status_code == 200 else []
        
# # #         languages = {}
# # #         total_stars = 0
        
# # #         for repo in repos:
# # #             if repo.get("language"):
# # #                 lang = repo["language"]
# # #                 languages[lang] = languages.get(lang, 0) + 1
# # #             total_stars += repo.get("stargazers_count", 0)
        
# # #         top_languages = sorted(languages.items(), key=lambda x: x[1], reverse=True)[:5]
# # #         language_list = [lang[0] for lang in top_languages]
        
# # #         commit_counts = {}
# # #         for event in events:
# # #             if event.get("type") == "PushEvent":
# # #                 created_at = event.get("created_at", "")
# # #                 if created_at:
# # #                     month = created_at[5:7]
# # #                     month_names = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
# # #                     month_name = month_names[int(month) - 1] if month.isdigit() else "Jan"
# # #                     commits = event.get("payload", {}).get("size", 1)
# # #                     commit_counts[month_name] = commit_counts.get(month_name, 0) + commits
        
# # #         current_month = datetime.now().month
# # #         month_names = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
# # #         github_activity = []
        
# # #         for i in range(6):
# # #             month_idx = (current_month - 6 + i) % 12
# # #             month_name = month_names[month_idx]
# # #             commits = commit_counts.get(month_name, 0)
# # #             github_activity.append({"month": month_name, "commits": commits})
        
# # #         total_commits = sum(commit_counts.values())
# # #         consistency = min(100, int((len(commit_counts) / 12) * 100))
        
# # #         return {
# # #             "username": username,
# # #             "repoCount": user_data.get("public_repos", 0),
# # #             "languages": language_list,
# # #             "stars": total_stars,
# # #             "totalCommits": total_commits,
# # #             "githubActivity": github_activity,
# # #             "consistencyScore": consistency
# # #         }
# # #     except:
# # #         return {
# # #             "username": username,
# # #             "repoCount": 0,
# # #             "languages": [],
# # #             "stars": 0,
# # #             "totalCommits": 0,
# # #             "githubActivity": [
# # #                 {"month": "Jan", "commits": 0},
# # #                 {"month": "Feb", "commits": 0},
# # #                 {"month": "Mar", "commits": 0},
# # #                 {"month": "Apr", "commits": 0},
# # #                 {"month": "May", "commits": 0},
# # #                 {"month": "Jun", "commits": 0}
# # #             ],
# # #             "consistencyScore": 0
# # #         }


# # # def get_linkedin_data(linkedin_url: str) -> Dict[str, Any]:
# # #     if not TINYFISH_API_KEY:
# # #         return {
# # #             "jobHistory": [],
# # #             "skills": [],
# # #             "education": []
# # #         }
    
# # #     try:
# # #         headers = {
# # #             "X-API-Key": TINYFISH_API_KEY,
# # #             "Content-Type": "application/json"
# # #         }
        
# # #         payload = {
# # #             "url": linkedin_url,
# # #             "goal": "Extract job titles, skills list, and education from this LinkedIn profile. Return structured data."
# # #         }
        
# # #         response = requests.post(TINYFISH_SSE_URL, headers=headers, json=payload, timeout=30, stream=True)
        
# # #         result_data = {}
# # #         for line in response.iter_lines():
# # #             if line:
# # #                 line_str = line.decode('utf-8')
# # #                 if line_str.startswith("data:"):
# # #                     try:
# # #                         data_json = json.loads(line_str[5:].strip())
# # #                         if data_json.get("type") == "COMPLETE":
# # #                             result_data = data_json.get("resultJson", {})
# # #                             break
# # #                     except:
# # #                         continue
        
# # #         return {
# # #             "jobHistory": result_data.get("jobHistory", []),
# # #             "skills": result_data.get("skills", []),
# # #             "education": result_data.get("education", [])
# # #         }
# # #     except:
# # #         return {
# # #             "jobHistory": [],
# # #             "skills": [],
# # #             "education": []
# # #         }


# # # def calculate_authenticity(resume_data: Dict, github_data: Dict, linkedin_data: Dict) -> int:
# # #     score = 100
    
# # #     resume_skills = set([s.lower() for s in resume_data.get("skills", [])])
# # #     github_languages = set([l.lower() for l in github_data.get("languages", [])])
# # #     linkedin_skills = set([s.lower() for s in linkedin_data.get("skills", [])])
    
# # #     for skill in resume_skills:
# # #         if skill not in github_languages and skill not in linkedin_skills:
# # #             score -= 10
    
# # #     resume_exp = len(resume_data.get("experience", []))
# # #     linkedin_jobs = len(linkedin_data.get("jobHistory", []))
    
# # #     if resume_exp > 0 and linkedin_jobs == 0:
# # #         score -= 15
    
# # #     if abs(resume_exp - linkedin_jobs) > 2:
# # #         score -= 10
    
# # #     return max(0, min(100, score))


# # # def calculate_skill_match(resume_data: Dict, github_data: Dict, role: str) -> int:
# # #     role_lower = role.lower()
    
# # #     all_skills = set([s.lower() for s in resume_data.get("skills", [])])
# # #     all_skills.update([l.lower() for l in github_data.get("languages", [])])
    
# # #     role_keywords = {
# # #         "backend": ["python", "java", "node", "go", "spring", "django", "flask", "api"],
# # #         "frontend": ["react", "vue", "angular", "javascript", "typescript", "html", "css"],
# # #         "fullstack": ["react", "node", "python", "javascript", "api", "database"],
# # #         "devops": ["docker", "kubernetes", "aws", "azure", "ci/cd", "jenkins"],
# # #         "data": ["python", "sql", "tensorflow", "pytorch", "ml", "ai"]
# # #     }
    
# # #     relevant_keywords = []
# # #     for key, keywords in role_keywords.items():
# # #         if key in role_lower:
# # #             relevant_keywords.extend(keywords)
    
# # #     if not relevant_keywords:
# # #         relevant_keywords = list(all_skills)[:10]
    
# # #     matches = sum(1 for keyword in relevant_keywords if keyword in all_skills)
# # #     total = len(relevant_keywords) if relevant_keywords else 1
    
# # #     skill_match = int((matches / total) * 100)
    
# # #     return min(100, max(0, skill_match))


# # # def calculate_skills_breakdown(resume_data: Dict, github_data: Dict) -> List[Dict]:
# # #     all_skills = [s.lower() for s in resume_data.get("skills", [])]
# # #     all_skills.extend([l.lower() for l in github_data.get("languages", [])])
    
# # #     frontend_keywords = ["react", "vue", "angular", "javascript", "typescript", "html", "css"]
# # #     backend_keywords = ["python", "java", "node", "go", "django", "flask", "spring", "api"]
# # #     dsa_keywords = ["algorithm", "data structure", "competitive", "leetcode"]
# # #     devops_keywords = ["docker", "kubernetes", "aws", "azure", "ci/cd"]
# # #     database_keywords = ["sql", "mongodb", "postgres", "mysql", "redis"]
    
# # #     frontend_count = sum(1 for s in all_skills if any(k in s for k in frontend_keywords))
# # #     backend_count = sum(1 for s in all_skills if any(k in s for k in backend_keywords))
# # #     dsa_count = sum(1 for s in all_skills if any(k in s for k in dsa_keywords))
# # #     devops_count = sum(1 for s in all_skills if any(k in s for k in devops_keywords))
# # #     database_count = sum(1 for s in all_skills if any(k in s for k in database_keywords))
    
# # #     return [
# # #         {"name": "Frontend", "value": min(100, frontend_count * 20)},
# # #         {"name": "Backend", "value": min(100, backend_count * 15)},
# # #         {"name": "DSA", "value": min(100, dsa_count * 25)},
# # #         {"name": "DevOps", "value": min(100, devops_count * 20)},
# # #         {"name": "Database", "value": min(100, database_count * 20)}
# # #     ]


# # # def generate_recommendation(candidate_score: int) -> str:
# # #     if candidate_score >= 75:
# # #         return "Strong Hire"
# # #     elif candidate_score >= 50:
# # #         return "Weak Hire"
# # #     else:
# # #         return "Reject"


# # # def generate_interview_questions(resume_data: Dict, github_data: Dict, role: str) -> List[str]:
# # #     skills = resume_data.get("skills", [])[:3]
# # #     languages = github_data.get("languages", [])[:2]
    
# # #     questions = []
    
# # #     if skills:
# # #         questions.append(f"Explain your experience with {skills[0]} and how you've used it in production.")
# # #     else:
# # #         questions.append("Describe your most challenging technical project.")
    
# # #     if languages:
# # #         questions.append(f"Walk us through a {languages[0]} project you've built. What challenges did you face?")
# # #     else:
# # #         questions.append("How do you approach learning new technologies?")
    
# # #     questions.append(f"How would you design a scalable system for a {role} role?")
# # #     questions.append("Describe a time when you debugged a critical production issue.")
# # #     questions.append("How do you ensure code quality and maintainability in your projects?")
    
# # #     return questions[:5]


# # # @app.post("/full-analysis", response_model=AnalysisResponse)
# # # async def full_analysis(
# # #     github_username: str = Query(...),
# # #     linkedin_url: str = Query(...),
# # #     role: str = Query(...),
# # #     file: UploadFile = File(...)
# # # ):
# # #     try:
# # #         pdf_bytes = await file.read()
# # #         resume_text = extract_pdf_text(pdf_bytes)
        
# # #         resume_data = parse_resume(resume_text)
# # #         github_data = get_github_data(github_username)
# # #         linkedin_data = get_linkedin_data(linkedin_url)
        
# # #         authenticity = calculate_authenticity(resume_data, github_data, linkedin_data)
# # #         skill_match = calculate_skill_match(resume_data, github_data, role)
# # #         activity_consistency = github_data.get("consistencyScore", 50)
        
# # #         candidate_score = int(
# # #             (0.4 * skill_match) +
# # #             (0.3 * authenticity) +
# # #             (0.3 * activity_consistency)
# # #         )
        
# # #         skills_breakdown = calculate_skills_breakdown(resume_data, github_data)
# # #         github_activity = github_data.get("githubActivity", [])
        
# # #         platforms = [
# # #             {"name": "GitHub", "value": f"{github_data.get('repoCount', 0)} repos"},
# # #             {"name": "LinkedIn", "value": f"{len(linkedin_data.get('jobHistory', []))} jobs"}
# # #         ]
        
# # #         recommendation = generate_recommendation(candidate_score)
# # #         interview_questions = generate_interview_questions(resume_data, github_data, role)
        
# # #         return AnalysisResponse(
# # #             candidateScore=candidate_score,
# # #             skillMatch=skill_match,
# # #             authenticity=authenticity,
# # #             activityConsistency=activity_consistency,
# # #             skillsBreakdown=skills_breakdown,
# # #             githubActivity=github_activity,
# # #             platforms=platforms,
# # #             recommendation=recommendation,
# # #             interviewQuestions=interview_questions
# # #         )
# # #     except Exception as e:
# # #         return AnalysisResponse(
# # #             candidateScore=0,
# # #             skillMatch=0,
# # #             authenticity=0,
# # #             activityConsistency=0,
# # #             skillsBreakdown=[
# # #                 {"name": "Frontend", "value": 0},
# # #                 {"name": "Backend", "value": 0},
# # #                 {"name": "DSA", "value": 0},
# # #                 {"name": "DevOps", "value": 0},
# # #                 {"name": "Database", "value": 0}
# # #             ],
# # #             githubActivity=[
# # #                 {"month": "Jan", "commits": 0},
# # #                 {"month": "Feb", "commits": 0},
# # #                 {"month": "Mar", "commits": 0},
# # #                 {"month": "Apr", "commits": 0},
# # #                 {"month": "May", "commits": 0},
# # #                 {"month": "Jun", "commits": 0}
# # #             ],
# # #             platforms=[
# # #                 {"name": "GitHub", "value": "0 repos"},
# # #                 {"name": "LinkedIn", "value": "0 jobs"}
# # #             ],
# # #             recommendation="Reject",
# # #             interviewQuestions=[
# # #                 "Unable to analyze candidate profile",
# # #                 "Please verify all inputs are correct",
# # #                 "Ensure GitHub profile is public"
# # #             ]
# # #         )


# # # @app.get("/health")
# # # async def health():
# # #     return {"status": "ok"}


# # # if __name__ == "__main__":
# # #     import uvicorn
# # #     uvicorn.run(app, host="0.0.0.0", port=8000)


# # import os
# # import json
# # import re
# # from typing import List, Dict, Any, Optional
# # from datetime import datetime, timedelta
# # from fastapi import FastAPI, File, UploadFile, HTTPException, Form
# # from fastapi.middleware.cors import CORSMiddleware
# # from pydantic import BaseModel
# # import fitz
# # import requests
# # from dotenv import load_dotenv

# # load_dotenv()

# # app = FastAPI()

# # app.add_middleware(
# #     CORSMiddleware,
# #     allow_origins=["http://localhost:3000"],
# #     allow_credentials=True,
# #     allow_methods=["*"],
# #     allow_headers=["*"],
# # )

# # TINYFISH_API_KEY = os.getenv("TINYFISH_API_KEY", "")
# # TINYFISH_SSE_URL = "https://agent.tinyfish.ai/v1/automation/run-sse"


# # class SkillBreakdown(BaseModel):
# #     name: str
# #     value: int


# # class GitHubActivity(BaseModel):
# #     month: str
# #     commits: int


# # class Platform(BaseModel):
# #     name: str
# #     value: str


# # class AnalysisResponse(BaseModel):
# #     candidateScore: int
# #     skillMatch: int
# #     authenticity: int
# #     activityConsistency: int
# #     skillsBreakdown: List[SkillBreakdown]
# #     githubActivity: List[GitHubActivity]
# #     platforms: List[Platform]
# #     recommendation: str
# #     interviewQuestions: List[str]


# # def extract_pdf_text(pdf_bytes: bytes) -> str:
# #     try:
# #         doc = fitz.open(stream=pdf_bytes, filetype="pdf")
# #         text = ""
# #         for page in doc:
# #             text += page.get_text()
# #         doc.close()
# #         return text
# #     except:
# #         return ""


# # def parse_resume(text: str) -> Dict[str, Any]:
# #     text_lower = text.lower()
    
# #     skills = []
# #     tech_keywords = [
# #         "python", "java", "javascript", "typescript", "react", "angular", "vue",
# #         "node", "express", "django", "flask", "spring", "docker", "kubernetes",
# #         "aws", "azure", "gcp", "sql", "mongodb", "postgres", "mysql", "redis",
# #         "git", "ci/cd", "html", "css", "tailwind", "bootstrap", "graphql", "rest",
# #         "microservices", "agile", "scrum", "tensorflow", "pytorch", "ml", "ai"
# #     ]
    
# #     for keyword in tech_keywords:
# #         if keyword in text_lower:
# #             skills.append(keyword.capitalize())
    
# #     experience = []
# #     exp_patterns = [
# #         r"(\d+)\+?\s*years?\s*(?:of)?\s*experience",
# #         r"experience:\s*(\d+)\+?\s*years?"
# #     ]
# #     for pattern in exp_patterns:
# #         match = re.search(pattern, text_lower)
# #         if match:
# #             years = match.group(1)
# #             experience.append({"years": years})
# #             break
    
# #     education = []
# #     edu_keywords = ["bachelor", "master", "phd", "b.tech", "m.tech", "bsc", "msc", "degree"]
# #     for keyword in edu_keywords:
# #         if keyword in text_lower:
# #             education.append({"degree": keyword})
# #             break
    
# #     certifications = []
# #     cert_keywords = ["aws certified", "azure", "google cloud", "certification", "certified"]
# #     for keyword in cert_keywords:
# #         if keyword in text_lower:
# #             certifications.append(keyword)
    
# #     projects = []
# #     if "project" in text_lower:
# #         projects.append("portfolio")
    
# #     return {
# #         "skills": list(set(skills)),
# #         "experience": experience,
# #         "education": education,
# #         "certifications": certifications,
# #         "projects": projects
# #     }


# # def get_github_data(username: str) -> Dict[str, Any]:
# #     try:
# #         user_url = f"https://api.github.com/users/{username}"
# #         repos_url = f"https://api.github.com/users/{username}/repos?per_page=100"
# #         events_url = f"https://api.github.com/users/{username}/events/public?per_page=100"
        
# #         user_resp = requests.get(user_url, timeout=10)
# #         repos_resp = requests.get(repos_url, timeout=10)
# #         events_resp = requests.get(events_url, timeout=10)
        
# #         if user_resp.status_code != 200:
# #             raise Exception("GitHub user not found")
        
# #         user_data = user_resp.json()
# #         repos = repos_resp.json() if repos_resp.status_code == 200 else []
# #         events = events_resp.json() if events_resp.status_code == 200 else []
        
# #         languages = {}
# #         total_stars = 0
        
# #         for repo in repos:
# #             if repo.get("language"):
# #                 lang = repo["language"]
# #                 languages[lang] = languages.get(lang, 0) + 1
# #             total_stars += repo.get("stargazers_count", 0)
        
# #         top_languages = sorted(languages.items(), key=lambda x: x[1], reverse=True)[:5]
# #         language_list = [lang[0] for lang in top_languages]
        
# #         commit_counts = {}
# #         for event in events:
# #             if event.get("type") == "PushEvent":
# #                 created_at = event.get("created_at", "")
# #                 if created_at:
# #                     month = created_at[5:7]
# #                     month_names = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
# #                     month_name = month_names[int(month) - 1] if month.isdigit() else "Jan"
# #                     commits = event.get("payload", {}).get("size", 1)
# #                     commit_counts[month_name] = commit_counts.get(month_name, 0) + commits
        
# #         current_month = datetime.now().month
# #         month_names = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
# #         github_activity = []
        
# #         for i in range(6):
# #             month_idx = (current_month - 6 + i) % 12
# #             month_name = month_names[month_idx]
# #             commits = commit_counts.get(month_name, 0)
# #             github_activity.append({"month": month_name, "commits": commits})
        
# #         total_commits = sum(commit_counts.values())
# #         consistency = min(100, int((len(commit_counts) / 12) * 100))
        
# #         return {
# #             "username": username,
# #             "repoCount": user_data.get("public_repos", 0),
# #             "languages": language_list,
# #             "stars": total_stars,
# #             "totalCommits": total_commits,
# #             "githubActivity": github_activity,
# #             "consistencyScore": consistency
# #         }
# #     except:
# #         return {
# #             "username": username,
# #             "repoCount": 0,
# #             "languages": [],
# #             "stars": 0,
# #             "totalCommits": 0,
# #             "githubActivity": [
# #                 {"month": "Jan", "commits": 0},
# #                 {"month": "Feb", "commits": 0},
# #                 {"month": "Mar", "commits": 0},
# #                 {"month": "Apr", "commits": 0},
# #                 {"month": "May", "commits": 0},
# #                 {"month": "Jun", "commits": 0}
# #             ],
# #             "consistencyScore": 0
# #         }


# # def get_linkedin_data(linkedin_url: str) -> Dict[str, Any]:
# #     if not TINYFISH_API_KEY:
# #         return {
# #             "jobHistory": [],
# #             "skills": [],
# #             "education": []
# #         }
    
# #     try:
# #         headers = {
# #             "X-API-Key": TINYFISH_API_KEY,
# #             "Content-Type": "application/json"
# #         }
        
# #         payload = {
# #             "url": linkedin_url,
# #             "goal": "Extract job titles, skills list, and education from this LinkedIn profile. Return structured data."
# #         }
        
# #         response = requests.post(TINYFISH_SSE_URL, headers=headers, json=payload, timeout=30, stream=True)
        
# #         result_data = {}
# #         for line in response.iter_lines():
# #             if line:
# #                 line_str = line.decode('utf-8')
# #                 if line_str.startswith("data:"):
# #                     try:
# #                         data_json = json.loads(line_str[5:].strip())
# #                         if data_json.get("type") == "COMPLETE":
# #                             result_data = data_json.get("resultJson", {})
# #                             break
# #                     except:
# #                         continue
        
# #         return {
# #             "jobHistory": result_data.get("jobHistory", []),
# #             "skills": result_data.get("skills", []),
# #             "education": result_data.get("education", [])
# #         }
# #     except:
# #         return {
# #             "jobHistory": [],
# #             "skills": [],
# #             "education": []
# #         }


# # def calculate_authenticity(resume_data: Dict, github_data: Dict, linkedin_data: Dict) -> int:
# #     score = 100
    
# #     resume_skills = set([s.lower() for s in resume_data.get("skills", [])])
# #     github_languages = set([l.lower() for l in github_data.get("languages", [])])
# #     linkedin_skills = set([s.lower() for s in linkedin_data.get("skills", [])])
    
# #     for skill in resume_skills:
# #         if skill not in github_languages and skill not in linkedin_skills:
# #             score -= 10
    
# #     resume_exp = len(resume_data.get("experience", []))
# #     linkedin_jobs = len(linkedin_data.get("jobHistory", []))
    
# #     if resume_exp > 0 and linkedin_jobs == 0:
# #         score -= 15
    
# #     if abs(resume_exp - linkedin_jobs) > 2:
# #         score -= 10
    
# #     return max(0, min(100, score))


# # def calculate_skill_match(resume_data: Dict, github_data: Dict, role: str) -> int:
# #     role_lower = role.lower()
    
# #     all_skills = set([s.lower() for s in resume_data.get("skills", [])])
# #     all_skills.update([l.lower() for l in github_data.get("languages", [])])
    
# #     role_keywords = {
# #         "backend": ["python", "java", "node", "go", "spring", "django", "flask", "api"],
# #         "frontend": ["react", "vue", "angular", "javascript", "typescript", "html", "css"],
# #         "fullstack": ["react", "node", "python", "javascript", "api", "database"],
# #         "devops": ["docker", "kubernetes", "aws", "azure", "ci/cd", "jenkins"],
# #         "data": ["python", "sql", "tensorflow", "pytorch", "ml", "ai"]
# #     }
    
# #     relevant_keywords = []
# #     for key, keywords in role_keywords.items():
# #         if key in role_lower:
# #             relevant_keywords.extend(keywords)
    
# #     if not relevant_keywords:
# #         relevant_keywords = list(all_skills)[:10]
    
# #     matches = sum(1 for keyword in relevant_keywords if keyword in all_skills)
# #     total = len(relevant_keywords) if relevant_keywords else 1
    
# #     skill_match = int((matches / total) * 100)
    
# #     return min(100, max(0, skill_match))


# # def calculate_skills_breakdown(resume_data: Dict, github_data: Dict) -> List[Dict]:
# #     all_skills = [s.lower() for s in resume_data.get("skills", [])]
# #     all_skills.extend([l.lower() for l in github_data.get("languages", [])])
    
# #     frontend_keywords = ["react", "vue", "angular", "javascript", "typescript", "html", "css"]
# #     backend_keywords = ["python", "java", "node", "go", "django", "flask", "spring", "api"]
# #     dsa_keywords = ["algorithm", "data structure", "competitive", "leetcode"]
# #     devops_keywords = ["docker", "kubernetes", "aws", "azure", "ci/cd"]
# #     database_keywords = ["sql", "mongodb", "postgres", "mysql", "redis"]
    
# #     frontend_count = sum(1 for s in all_skills if any(k in s for k in frontend_keywords))
# #     backend_count = sum(1 for s in all_skills if any(k in s for k in backend_keywords))
# #     dsa_count = sum(1 for s in all_skills if any(k in s for k in dsa_keywords))
# #     devops_count = sum(1 for s in all_skills if any(k in s for k in devops_keywords))
# #     database_count = sum(1 for s in all_skills if any(k in s for k in database_keywords))
    
# #     return [
# #         {"name": "Frontend", "value": min(100, frontend_count * 20)},
# #         {"name": "Backend", "value": min(100, backend_count * 15)},
# #         {"name": "DSA", "value": min(100, dsa_count * 25)},
# #         {"name": "DevOps", "value": min(100, devops_count * 20)},
# #         {"name": "Database", "value": min(100, database_count * 20)}
# #     ]


# # def generate_recommendation(candidate_score: int) -> str:
# #     if candidate_score >= 75:
# #         return "Strong Hire"
# #     elif candidate_score >= 50:
# #         return "Weak Hire"
# #     else:
# #         return "Reject"


# # def generate_interview_questions(resume_data: Dict, github_data: Dict, role: str) -> List[str]:
# #     skills = resume_data.get("skills", [])[:3]
# #     languages = github_data.get("languages", [])[:2]
    
# #     questions = []
    
# #     if skills:
# #         questions.append(f"Explain your experience with {skills[0]} and how you've used it in production.")
# #     else:
# #         questions.append("Describe your most challenging technical project.")
    
# #     if languages:
# #         questions.append(f"Walk us through a {languages[0]} project you've built. What challenges did you face?")
# #     else:
# #         questions.append("How do you approach learning new technologies?")
    
# #     questions.append(f"How would you design a scalable system for a {role} role?")
# #     questions.append("Describe a time when you debugged a critical production issue.")
# #     questions.append("How do you ensure code quality and maintainability in your projects?")
    
# #     return questions[:5]


# # @app.post("/full-analysis", response_model=AnalysisResponse)
# # async def full_analysis(
# #     github_username: str = Form(...),
# #     linkedin_url: str = Form(...),
# #     role: str = Form(...),
# #     resume: UploadFile = File(...)
# # ):
# #     try:
# #         pdf_bytes = await resume.read()
# #         resume_text = extract_pdf_text(pdf_bytes)
        
# #         resume_data = parse_resume(resume_text)
# #         github_data = get_github_data(github_username)
# #         linkedin_data = get_linkedin_data(linkedin_url)
        
# #         authenticity = calculate_authenticity(resume_data, github_data, linkedin_data)
# #         skill_match = calculate_skill_match(resume_data, github_data, role)
# #         activity_consistency = github_data.get("consistencyScore", 50)
        
# #         candidate_score = int(
# #             (0.4 * skill_match) +
# #             (0.3 * authenticity) +
# #             (0.3 * activity_consistency)
# #         )
        
# #         skills_breakdown = calculate_skills_breakdown(resume_data, github_data)
# #         github_activity = github_data.get("githubActivity", [])
        
# #         platforms = [
# #             {"name": "GitHub", "value": f"{github_data.get('repoCount', 0)} repos"},
# #             {"name": "LinkedIn", "value": f"{len(linkedin_data.get('jobHistory', []))} jobs"}
# #         ]
        
# #         recommendation = generate_recommendation(candidate_score)
# #         interview_questions = generate_interview_questions(resume_data, github_data, role)
        
# #         return AnalysisResponse(
# #             candidateScore=candidate_score,
# #             skillMatch=skill_match,
# #             authenticity=authenticity,
# #             activityConsistency=activity_consistency,
# #             skillsBreakdown=skills_breakdown,
# #             githubActivity=github_activity,
# #             platforms=platforms,
# #             recommendation=recommendation,
# #             interviewQuestions=interview_questions
# #         )
# #     except Exception as e:
# #         return AnalysisResponse(
# #             candidateScore=0,
# #             skillMatch=0,
# #             authenticity=0,
# #             activityConsistency=0,
# #             skillsBreakdown=[
# #                 {"name": "Frontend", "value": 0},
# #                 {"name": "Backend", "value": 0},
# #                 {"name": "DSA", "value": 0},
# #                 {"name": "DevOps", "value": 0},
# #                 {"name": "Database", "value": 0}
# #             ],
# #             githubActivity=[
# #                 {"month": "Jan", "commits": 0},
# #                 {"month": "Feb", "commits": 0},
# #                 {"month": "Mar", "commits": 0},
# #                 {"month": "Apr", "commits": 0},
# #                 {"month": "May", "commits": 0},
# #                 {"month": "Jun", "commits": 0}
# #             ],
# #             platforms=[
# #                 {"name": "GitHub", "value": "0 repos"},
# #                 {"name": "LinkedIn", "value": "0 jobs"}
# #             ],
# #             recommendation="Reject",
# #             interviewQuestions=[
# #                 "Unable to analyze candidate profile",
# #                 "Please verify all inputs are correct",
# #                 "Ensure GitHub profile is public"
# #             ]
# #         )


# # @app.get("/health")
# # async def health():
# #     return {"status": "ok"}


# # if __name__ == "__main__":
# #     import uvicorn
# #     uvicorn.run(app, host="0.0.0.0", port=8000)

# import os
# import json
# import re
# from typing import List, Dict, Any
# from datetime import datetime
# from fastapi import FastAPI, File, UploadFile, HTTPException, Form
# from fastapi.middleware.cors import CORSMiddleware
# from pydantic import BaseModel
# import fitz  # PyMuPDF
# import requests
# from dotenv import load_dotenv
# import anthropic

# load_dotenv()

# # ── App Setup ──────────────────────────────────────────────────────
# app = FastAPI(title="NEXUS RECRUIT API", version="2.0.0")

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # ── API Keys ───────────────────────────────────────────────────────
# ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY", "")
# TINYFISH_API_KEY  = os.getenv("TINYFISH_API_KEY", "")
# GITHUB_TOKEN      = os.getenv("GITHUB_TOKEN", "")      # optional, raises rate limit
# TINYFISH_SSE_URL  = "https://agent.tinyfish.ai/v1/automation/run-sse"

# # ── Pydantic Models ────────────────────────────────────────────────
# class SkillBreakdown(BaseModel):
#     name: str
#     value: int

# class GitHubActivity(BaseModel):
#     month: str
#     commits: int

# class Platform(BaseModel):
#     name: str
#     value: str

# class AnalysisResponse(BaseModel):
#     candidateScore: int
#     skillMatch: int
#     authenticity: int
#     activityConsistency: int
#     skillsBreakdown: List[SkillBreakdown]
#     githubActivity: List[GitHubActivity]
#     platforms: List[Platform]
#     recommendation: str
#     interviewQuestions: List[str]


# # ══════════════════════════════════════════════════════════════════
# # 1. RESUME PARSING
# # ══════════════════════════════════════════════════════════════════

# def extract_pdf_text(pdf_bytes: bytes) -> str:
#     """Extract raw text from a PDF file."""
#     try:
#         doc = fitz.open(stream=pdf_bytes, filetype="pdf")
#         text = "\n".join(page.get_text() for page in doc)
#         doc.close()
#         return text.strip()
#     except Exception:
#         return ""


# def parse_resume(text: str) -> Dict[str, Any]:
#     """Parse resume text into structured data."""
#     text_lower = text.lower()

#     # ── Skills detection ───────────────────────────────────────────
#     tech_keywords = [
#         "python", "java", "javascript", "typescript", "react", "angular", "vue",
#         "node", "express", "django", "flask", "spring", "docker", "kubernetes",
#         "aws", "azure", "gcp", "sql", "mongodb", "postgres", "mysql", "redis",
#         "git", "ci/cd", "html", "css", "tailwind", "bootstrap", "graphql", "rest",
#         "microservices", "agile", "scrum", "tensorflow", "pytorch", "machine learning",
#         "deep learning", "fastapi", "next.js", "nuxt", "svelte", "golang", "rust",
#         "c++", "c#", ".net", "php", "laravel", "ruby", "rails", "linux", "bash",
#         "terraform", "ansible", "kafka", "rabbitmq", "elasticsearch", "nginx",
#     ]
#     skills = sorted({kw.capitalize() for kw in tech_keywords if kw in text_lower})

#     # ── Experience detection ───────────────────────────────────────
#     exp_years = 0
#     for pattern in [
#         r"(\d+)\+?\s*years?\s*(?:of\s+)?(?:experience|exp)",
#         r"experience[:\s]+(\d+)\+?\s*years?",
#     ]:
#         m = re.search(pattern, text_lower)
#         if m:
#             exp_years = int(m.group(1))
#             break

#     # ── Education ─────────────────────────────────────────────────
#     education = []
#     for kw in ["phd", "doctorate", "master", "m.tech", "msc", "m.s.", "bachelor", "b.tech", "bsc", "b.e.", "b.s."]:
#         if kw in text_lower:
#             education.append(kw.upper())
#             break

#     # ── Certifications ────────────────────────────────────────────
#     certifications = []
#     for cert in ["aws certified", "azure certified", "google cloud", "pmp", "cka", "ckad",
#                  "certified kubernetes", "certified developer", "comptia"]:
#         if cert in text_lower:
#             certifications.append(cert.title())

#     # ── Project count heuristic ────────────────────────────────────
#     project_count = len(re.findall(r'\bproject\b', text_lower, re.IGNORECASE))

#     return {
#         "skills": skills,
#         "experience_years": exp_years,
#         "education": education,
#         "certifications": certifications,
#         "project_count": project_count,
#         "raw_text": text[:3000],  # keep first 3k chars for Claude prompt
#     }


# # ══════════════════════════════════════════════════════════════════
# # 2. GITHUB INTEGRATION
# # ══════════════════════════════════════════════════════════════════

# def _gh_headers() -> Dict[str, str]:
#     headers = {"Accept": "application/vnd.github+json"}
#     if GITHUB_TOKEN:
#         headers["Authorization"] = f"Bearer {GITHUB_TOKEN}"
#     return headers


# def get_github_data(username: str) -> Dict[str, Any]:
#     """Fetch user profile, repos, and recent events from GitHub API."""
#     try:
#         headers = _gh_headers()
#         user_resp  = requests.get(f"https://api.github.com/users/{username}",              headers=headers, timeout=10)
#         repos_resp = requests.get(f"https://api.github.com/users/{username}/repos?per_page=100&sort=updated", headers=headers, timeout=10)
#         events_resp= requests.get(f"https://api.github.com/users/{username}/events/public?per_page=100",      headers=headers, timeout=10)

#         if user_resp.status_code == 404:
#             raise ValueError(f"GitHub user '{username}' not found.")
#         if user_resp.status_code == 403:
#             raise ValueError("GitHub rate limit hit. Set GITHUB_TOKEN in .env to increase limits.")

#         user_data = user_resp.json()
#         repos     = repos_resp.json()  if repos_resp.status_code  == 200 else []
#         events    = events_resp.json() if events_resp.status_code == 200 else []

#         # ── Languages & Stars ──────────────────────────────────────
#         language_counts: Dict[str, int] = {}
#         total_stars = 0
#         for repo in repos:
#             if isinstance(repo, dict):
#                 lang = repo.get("language")
#                 if lang:
#                     language_counts[lang] = language_counts.get(lang, 0) + 1
#                 total_stars += repo.get("stargazers_count", 0)

#         top_languages = [lang for lang, _ in sorted(language_counts.items(), key=lambda x: x[1], reverse=True)[:6]]

#         # ── Commit activity (last 6 months from events) ────────────
#         month_names = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
#         commit_counts: Dict[str, int] = {}

#         for event in events:
#             if not isinstance(event, dict):
#                 continue
#             if event.get("type") != "PushEvent":
#                 continue
#             created = event.get("created_at", "")
#             if len(created) >= 7:
#                 month_idx  = int(created[5:7]) - 1
#                 month_name = month_names[month_idx]
#                 size = event.get("payload", {}).get("size", 1)
#                 commit_counts[month_name] = commit_counts.get(month_name, 0) + size

#         # Build last-6-months list
#         current_month = datetime.now().month
#         github_activity = []
#         for i in range(6):
#             idx  = (current_month - 6 + i) % 12
#             name = month_names[idx]
#             github_activity.append({"month": name, "commits": commit_counts.get(name, 0)})

#         total_commits = sum(commit_counts.values())
#         # Consistency: how many of the last 12 months had commits
#         active_months  = len(commit_counts)
#         consistency    = min(100, int((active_months / 6) * 100)) if active_months else 0

#         return {
#             "username":          username,
#             "name":              user_data.get("name", username),
#             "bio":               user_data.get("bio", ""),
#             "repoCount":         user_data.get("public_repos", 0),
#             "followers":         user_data.get("followers", 0),
#             "languages":         top_languages,
#             "stars":             total_stars,
#             "totalCommits":      total_commits,
#             "githubActivity":    github_activity,
#             "consistencyScore":  consistency,
#         }

#     except ValueError as e:
#         raise HTTPException(status_code=400, detail=str(e))
#     except Exception:
#         # Return zeroed data so the rest of the pipeline still works
#         return {
#             "username": username, "name": username, "bio": "",
#             "repoCount": 0, "followers": 0, "languages": [], "stars": 0,
#             "totalCommits": 0, "consistencyScore": 0,
#             "githubActivity": [{"month": m, "commits": 0}
#                                for m in ["Jan","Feb","Mar","Apr","May","Jun"]],
#         }


# # ══════════════════════════════════════════════════════════════════
# # 3. LINKEDIN SCRAPING (TinyFish)
# # ══════════════════════════════════════════════════════════════════

# def get_linkedin_data(linkedin_url: str) -> Dict[str, Any]:
#     """Scrape LinkedIn profile via TinyFish automation API."""
#     if not TINYFISH_API_KEY or not linkedin_url.strip():
#         return {"jobHistory": [], "skills": [], "education": []}

#     try:
#         headers = {
#             "X-API-Key": TINYFISH_API_KEY,
#             "Content-Type": "application/json",
#         }
#         payload = {
#             "url": linkedin_url,
#             "goal": (
#                 "Extract the following from this LinkedIn profile and return as JSON: "
#                 "1. jobHistory: array of {title, company, duration} "
#                 "2. skills: array of skill name strings "
#                 "3. education: array of {degree, institution} "
#                 "Return ONLY valid JSON, no markdown."
#             ),
#         }
#         response = requests.post(
#             TINYFISH_SSE_URL, headers=headers, json=payload, timeout=45, stream=True
#         )

#         result_data: Dict = {}
#         for line in response.iter_lines():
#             if not line:
#                 continue
#             line_str = line.decode("utf-8")
#             if line_str.startswith("data:"):
#                 try:
#                     data_json = json.loads(line_str[5:].strip())
#                     if data_json.get("type") == "COMPLETE":
#                         raw = data_json.get("resultJson") or data_json.get("result", {})
#                         if isinstance(raw, str):
#                             raw = json.loads(raw)
#                         result_data = raw
#                         break
#                 except (json.JSONDecodeError, KeyError):
#                     continue

#         return {
#             "jobHistory": result_data.get("jobHistory", []),
#             "skills":     result_data.get("skills", []),
#             "education":  result_data.get("education", []),
#         }

#     except Exception:
#         return {"jobHistory": [], "skills": [], "education": []}


# # ══════════════════════════════════════════════════════════════════
# # 4. SCORING ENGINE
# # ══════════════════════════════════════════════════════════════════

# def calculate_authenticity(resume_data: Dict, github_data: Dict, linkedin_data: Dict) -> int:
#     """
#     Authenticity = how well resume claims are backed by real activity.
#     Penalises: skills on resume not seen on GitHub or LinkedIn,
#                experience claims not matching LinkedIn job count.
#     """
#     score = 100

#     resume_skills  = {s.lower() for s in resume_data.get("skills", [])}
#     github_langs   = {l.lower() for l in github_data.get("languages", [])}
#     linkedin_skills= {s.lower() for s in linkedin_data.get("skills", [])}

#     verified_pool  = github_langs | linkedin_skills

#     unverified = [s for s in resume_skills if s not in verified_pool]
#     # Soft penalty — can't fully verify everything, so cap deduction
#     score -= min(30, len(unverified) * 5)

#     linkedin_jobs = len(linkedin_data.get("jobHistory", []))
#     resume_years  = resume_data.get("experience_years", 0)

#     if resume_years > 0 and linkedin_jobs == 0:
#         score -= 15  # claimed experience but no LinkedIn history

#     if linkedin_jobs == 0 and len(linkedin_data.get("skills", [])) == 0:
#         score -= 5   # couldn't scrape LinkedIn at all, slight uncertainty

#     # Bonus for certs
#     score += min(10, len(resume_data.get("certifications", [])) * 5)

#     return max(0, min(100, score))


# def calculate_skill_match(resume_data: Dict, github_data: Dict, role: str) -> int:
#     """Match candidate skills against role-specific keyword lists."""
#     role_lower = role.lower()

#     all_skills = {s.lower() for s in resume_data.get("skills", [])}
#     all_skills |= {l.lower() for l in github_data.get("languages", [])}

#     role_map = {
#         "backend":   ["python", "java", "node", "go", "django", "flask", "spring", "fastapi", "api", "sql", "postgres", "redis"],
#         "frontend":  ["react", "vue", "angular", "javascript", "typescript", "html", "css", "tailwind", "next.js"],
#         "fullstack": ["react", "node", "python", "javascript", "api", "sql", "docker"],
#         "devops":    ["docker", "kubernetes", "aws", "azure", "gcp", "ci/cd", "terraform", "ansible", "linux", "bash"],
#         "data":      ["python", "sql", "tensorflow", "pytorch", "machine learning", "pandas", "spark", "kafka"],
#         "mobile":    ["react native", "flutter", "swift", "kotlin", "android", "ios"],
#         "ml":        ["python", "tensorflow", "pytorch", "machine learning", "deep learning", "nlp", "scikit"],
#         "security":  ["penetration testing", "cybersecurity", "networking", "linux", "python", "siem"],
#     }

#     relevant = []
#     for key, keywords in role_map.items():
#         if key in role_lower:
#             relevant.extend(keywords)

#     if not relevant:
#         # Generic fallback: score based on volume of skills detected
#         return min(100, len(all_skills) * 5)

#     relevant = list(set(relevant))
#     matches  = sum(1 for kw in relevant if kw in all_skills)
#     return min(100, max(0, int((matches / len(relevant)) * 100)))


# def calculate_skills_breakdown(resume_data: Dict, github_data: Dict) -> List[Dict]:
#     """Compute per-category skill scores."""
#     all_skills = [s.lower() for s in resume_data.get("skills", [])]
#     all_skills += [l.lower() for l in github_data.get("languages", [])]

#     categories = {
#         "Frontend":  ["react","vue","angular","javascript","typescript","html","css","tailwind","next.js","svelte"],
#         "Backend":   ["python","java","node","go","django","flask","spring","fastapi","express","rails","php","laravel"],
#         "DSA":       ["algorithm","data structure","competitive","leetcode","dynamic programming","graph","c++"],
#         "DevOps":    ["docker","kubernetes","aws","azure","gcp","ci/cd","terraform","ansible","jenkins","nginx"],
#         "Database":  ["sql","mongodb","postgres","mysql","redis","elasticsearch","cassandra","dynamodb"],
#     }

#     result = []
#     for cat, keywords in categories.items():
#         hits = sum(1 for s in all_skills if any(k in s for k in keywords))
#         # Scale hits to 0-100; cap generously
#         value = min(100, hits * 18)
#         result.append({"name": cat, "value": value})
#     return result


# def generate_recommendation(score: int) -> str:
#     if score >= 72:
#         return "Strong Hire"
#     elif score >= 48:
#         return "Weak Hire"
#     return "Reject"


# # ══════════════════════════════════════════════════════════════════
# # 5. AI INTERVIEW QUESTION GENERATION (Claude)
# # ══════════════════════════════════════════════════════════════════

# def generate_interview_questions_ai(
#     resume_data: Dict,
#     github_data: Dict,
#     linkedin_data: Dict,
#     role: str,
# ) -> List[str]:
#     """Use Claude claude-sonnet-4-20250514 to generate contextual interview questions."""

#     # Build a rich context string for Claude
#     skills_str  = ", ".join(resume_data.get("skills", [])[:15]) or "Not detected"
#     langs_str   = ", ".join(github_data.get("languages", []))    or "Not detected"
#     jobs_str    = "; ".join(
#         f"{j.get('title','?')} at {j.get('company','?')}"
#         for j in linkedin_data.get("jobHistory", [])[:4]
#     ) or "Not available"
#     certs_str   = ", ".join(resume_data.get("certifications", [])) or "None"
#     exp_years   = resume_data.get("experience_years", 0)
#     resume_text = resume_data.get("raw_text", "")[:1500]

#     prompt = f"""You are an expert technical recruiter generating interview questions for a {role} candidate.

# CANDIDATE PROFILE:
# - Resume Skills: {skills_str}
# - GitHub Languages: {langs_str}
# - LinkedIn Job History: {jobs_str}
# - Certifications: {certs_str}
# - Experience: {exp_years} years
# - Resume Excerpt: {resume_text}

# Generate exactly 5 highly specific, technical interview questions tailored to this exact candidate.
# Questions should:
# 1. Reference their actual skills and tools they've used
# 2. Range from foundational (Q1) to senior/architectural (Q5)
# 3. Expose gaps or validate depth in their claimed expertise
# 4. Be concise (1-2 sentences each)

# Return ONLY a JSON array of 5 strings, e.g.:
# ["Question 1", "Question 2", "Question 3", "Question 4", "Question 5"]
# No markdown, no explanation, just the JSON array."""

#     try:
#         client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)
#         message = client.messages.create(
#             model="claude-sonnet-4-20250514",
#             max_tokens=600,
#             messages=[{"role": "user", "content": prompt}],
#         )
#         raw = message.content[0].text.strip()
#         # Strip markdown fences if present
#         raw = re.sub(r"^```(?:json)?\s*", "", raw)
#         raw = re.sub(r"\s*```$", "", raw)
#         questions = json.loads(raw)
#         if isinstance(questions, list) and len(questions) >= 1:
#             return [str(q) for q in questions[:5]]
#     except Exception:
#         pass

#     # ── Fallback: rule-based questions ────────────────────────────
#     return _fallback_questions(resume_data, github_data, role)


# def _fallback_questions(resume_data: Dict, github_data: Dict, role: str) -> List[str]:
#     skills = resume_data.get("skills", [])
#     langs  = github_data.get("languages", [])
#     q = []
#     if skills:
#         q.append(f"Walk us through a production project where you used {skills[0]} — what was the hardest bug you solved?")
#     else:
#         q.append("Describe your most complex technical project and the biggest challenge you overcame.")
#     if langs:
#         q.append(f"Your GitHub shows heavy {langs[0]} usage. How do you handle performance bottlenecks in {langs[0]}?")
#     else:
#         q.append("How do you approach choosing a technology stack for a new project?")
#     q.append(f"Design a horizontally scalable system for a core feature in the {role} domain. Walk us through your architecture decisions.")
#     q.append("Describe a time you identified and resolved a critical production incident. What was your debugging process?")
#     q.append("How do you balance technical debt against feature velocity, and how have you communicated this trade-off to stakeholders?")
#     return q[:5]


# # ══════════════════════════════════════════════════════════════════
# # 6. ROUTES
# # ══════════════════════════════════════════════════════════════════

# @app.get("/health")
# async def health():
#     return {
#         "status": "ok",
#         "anthropic_key": bool(ANTHROPIC_API_KEY),
#         "tinyfish_key":  bool(TINYFISH_API_KEY),
#         "github_token":  bool(GITHUB_TOKEN),
#     }


# @app.post("/full-analysis", response_model=AnalysisResponse)
# async def full_analysis(
#     github_username: str = Form(...),
#     linkedin_url:    str = Form(...),
#     role:            str = Form(...),
#     resume:          UploadFile = File(...),
# ):
#     # ── Validate inputs ────────────────────────────────────────────
#     if not github_username.strip():
#         raise HTTPException(status_code=422, detail="GitHub username is required.")
#     if not role.strip():
#         raise HTTPException(status_code=422, detail="Role is required.")
#     if resume.content_type not in ("application/pdf", "application/octet-stream"):
#         raise HTTPException(status_code=422, detail="Only PDF resumes are accepted.")

#     # ── 1. Parse resume ────────────────────────────────────────────
#     pdf_bytes   = await resume.read()
#     resume_text = extract_pdf_text(pdf_bytes)
#     if not resume_text:
#         raise HTTPException(status_code=422, detail="Could not extract text from PDF. Ensure it is not a scanned image.")
#     resume_data = parse_resume(resume_text)

#     # ── 2. GitHub data ─────────────────────────────────────────────
#     github_data = get_github_data(github_username.strip())

#     # ── 3. LinkedIn data ───────────────────────────────────────────
#     linkedin_data = get_linkedin_data(linkedin_url.strip())

#     # ── 4. Scoring ─────────────────────────────────────────────────
#     authenticity         = calculate_authenticity(resume_data, github_data, linkedin_data)
#     skill_match          = calculate_skill_match(resume_data, github_data, role)
#     activity_consistency = github_data.get("consistencyScore", 0)

#     candidate_score = int(
#         0.40 * skill_match +
#         0.30 * authenticity +
#         0.30 * activity_consistency
#     )

#     # ── 5. Derived data ────────────────────────────────────────────
#     skills_breakdown   = calculate_skills_breakdown(resume_data, github_data)
#     github_activity    = github_data.get("githubActivity", [])
#     recommendation     = generate_recommendation(candidate_score)

#     platforms = [
#         {"name": "GitHub",   "value": f"{github_data.get('repoCount', 0)} repos / {github_data.get('stars', 0)} ⭐"},
#         {"name": "LinkedIn", "value": f"{len(linkedin_data.get('jobHistory', []))} positions"},
#     ]

#     # ── 6. AI-powered interview questions ──────────────────────────
#     interview_questions = generate_interview_questions_ai(
#         resume_data, github_data, linkedin_data, role
#     )

#     return AnalysisResponse(
#         candidateScore      = candidate_score,
#         skillMatch          = skill_match,
#         authenticity        = authenticity,
#         activityConsistency = activity_consistency,
#         skillsBreakdown     = [SkillBreakdown(**s) for s in skills_breakdown],
#         githubActivity      = [GitHubActivity(**g) for g in github_activity],
#         platforms           = [Platform(**p) for p in platforms],
#         recommendation      = recommendation,
#         interviewQuestions  = interview_questions,
#     )


# # ══════════════════════════════════════════════════════════════════
# # 7. ENTRY POINT
# # ══════════════════════════════════════════════════════════════════

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)

import os
import json
import re
from typing import List, Dict, Any
from datetime import datetime
from fastapi import FastAPI, File, UploadFile, HTTPException, Form
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import fitz  # PyMuPDF
import requests
from dotenv import load_dotenv
import anthropic

load_dotenv()

# ── App Setup ──────────────────────────────────────────────────────
app = FastAPI(title="NEXUS RECRUIT API", version="2.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ── API Keys ───────────────────────────────────────────────────────
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY", "")
TINYFISH_API_KEY  = os.getenv("TINYFISH_API_KEY", "")
GITHUB_TOKEN      = os.getenv("GITHUB_TOKEN", "")      # optional, raises rate limit
TINYFISH_SSE_URL  = "https://agent.tinyfish.ai/v1/automation/run-sse"

# ── Pydantic Models ────────────────────────────────────────────────
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


# ══════════════════════════════════════════════════════════════════
# 1. RESUME PARSING
# ══════════════════════════════════════════════════════════════════

def extract_pdf_text(pdf_bytes: bytes) -> str:
    """Extract raw text from a PDF file."""
    try:
        doc = fitz.open(stream=pdf_bytes, filetype="pdf")
        text = "\n".join(page.get_text() for page in doc)
        doc.close()
        return text.strip()
    except Exception:
        return ""


def parse_resume(text: str) -> Dict[str, Any]:
    """Parse resume text into structured data."""
    text_lower = text.lower()

    # ── Skills detection ───────────────────────────────────────────
    tech_keywords = [
        "python", "java", "javascript", "typescript", "react", "angular", "vue",
        "node", "express", "django", "flask", "spring", "docker", "kubernetes",
        "aws", "azure", "gcp", "sql", "mongodb", "postgres", "mysql", "redis",
        "git", "ci/cd", "html", "css", "tailwind", "bootstrap", "graphql", "rest",
        "microservices", "agile", "scrum", "tensorflow", "pytorch", "machine learning",
        "deep learning", "fastapi", "next.js", "nuxt", "svelte", "golang", "rust",
        "c++", "c#", ".net", "php", "laravel", "ruby", "rails", "linux", "bash",
        "terraform", "ansible", "kafka", "rabbitmq", "elasticsearch", "nginx",
    ]
    skills = sorted({kw.capitalize() for kw in tech_keywords if kw in text_lower})

    # ── Experience detection ───────────────────────────────────────
    exp_years = 0
    for pattern in [
        r"(\d+)\+?\s*years?\s*(?:of\s+)?(?:experience|exp)",
        r"experience[:\s]+(\d+)\+?\s*years?",
    ]:
        m = re.search(pattern, text_lower)
        if m:
            exp_years = int(m.group(1))
            break

    # ── Education ─────────────────────────────────────────────────
    education = []
    for kw in ["phd", "doctorate", "master", "m.tech", "msc", "m.s.", "bachelor", "b.tech", "bsc", "b.e.", "b.s."]:
        if kw in text_lower:
            education.append(kw.upper())
            break

    # ── Certifications ────────────────────────────────────────────
    certifications = []
    for cert in ["aws certified", "azure certified", "google cloud", "pmp", "cka", "ckad",
                 "certified kubernetes", "certified developer", "comptia"]:
        if cert in text_lower:
            certifications.append(cert.title())

    # ── Project count heuristic ────────────────────────────────────
    project_count = len(re.findall(r'\bproject\b', text_lower, re.IGNORECASE))

    return {
        "skills": skills,
        "experience_years": exp_years,
        "education": education,
        "certifications": certifications,
        "project_count": project_count,
        "raw_text": text[:3000],  # keep first 3k chars for Claude prompt
    }


# ══════════════════════════════════════════════════════════════════
# 2. GITHUB INTEGRATION
# ══════════════════════════════════════════════════════════════════

def _gh_headers() -> Dict[str, str]:
    headers = {"Accept": "application/vnd.github+json"}
    if GITHUB_TOKEN:
        headers["Authorization"] = f"Bearer {GITHUB_TOKEN}"
    return headers


def get_github_data(username: str) -> Dict[str, Any]:
    """Fetch user profile, repos, and recent events from GitHub API."""
    try:
        headers = _gh_headers()
        user_resp  = requests.get(f"https://api.github.com/users/{username}",              headers=headers, timeout=10)
        repos_resp = requests.get(f"https://api.github.com/users/{username}/repos?per_page=100&sort=updated", headers=headers, timeout=10)
        events_resp= requests.get(f"https://api.github.com/users/{username}/events/public?per_page=100",      headers=headers, timeout=10)

        if user_resp.status_code == 404:
            raise ValueError(f"GitHub user '{username}' not found.")
        if user_resp.status_code == 403:
            raise ValueError("GitHub rate limit hit. Set GITHUB_TOKEN in .env to increase limits.")

        user_data = user_resp.json()
        repos     = repos_resp.json()  if repos_resp.status_code  == 200 else []
        events    = events_resp.json() if events_resp.status_code == 200 else []

        # ── Languages & Stars ──────────────────────────────────────
        language_counts: Dict[str, int] = {}
        total_stars = 0
        for repo in repos:
            if isinstance(repo, dict):
                lang = repo.get("language")
                if lang:
                    language_counts[lang] = language_counts.get(lang, 0) + 1
                total_stars += repo.get("stargazers_count", 0)

        top_languages = [lang for lang, _ in sorted(language_counts.items(), key=lambda x: x[1], reverse=True)[:6]]

        # ── Commit activity (last 6 months from events) ────────────
        month_names = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
        commit_counts: Dict[str, int] = {}

        for event in events:
            if not isinstance(event, dict):
                continue
            if event.get("type") != "PushEvent":
                continue
            created = event.get("created_at", "")
            if len(created) >= 7:
                month_idx  = int(created[5:7]) - 1
                month_name = month_names[month_idx]
                size = event.get("payload", {}).get("size", 1)
                commit_counts[month_name] = commit_counts.get(month_name, 0) + size

        # Build last-6-months list
        current_month = datetime.now().month
        github_activity = []
        for i in range(6):
            idx  = (current_month - 6 + i) % 12
            name = month_names[idx]
            github_activity.append({"month": name, "commits": commit_counts.get(name, 0)})

        total_commits = sum(commit_counts.values())
        # Consistency: how many of the last 12 months had commits
        active_months  = len(commit_counts)
        consistency    = min(100, int((active_months / 6) * 100)) if active_months else 0

        return {
            "username":          username,
            "name":              user_data.get("name", username),
            "bio":               user_data.get("bio", ""),
            "repoCount":         user_data.get("public_repos", 0),
            "followers":         user_data.get("followers", 0),
            "languages":         top_languages,
            "stars":             total_stars,
            "totalCommits":      total_commits,
            "githubActivity":    github_activity,
            "consistencyScore":  consistency,
        }

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception:
        # Return zeroed data so the rest of the pipeline still works
        return {
            "username": username, "name": username, "bio": "",
            "repoCount": 0, "followers": 0, "languages": [], "stars": 0,
            "totalCommits": 0, "consistencyScore": 0,
            "githubActivity": [{"month": m, "commits": 0}
                               for m in ["Jan","Feb","Mar","Apr","May","Jun"]],
        }


# ══════════════════════════════════════════════════════════════════
# 3. LINKEDIN SCRAPING (TinyFish)
# ══════════════════════════════════════════════════════════════════

def get_linkedin_data(linkedin_url: str) -> Dict[str, Any]:
    """Scrape LinkedIn profile via TinyFish automation API."""
    if not TINYFISH_API_KEY or not linkedin_url.strip():
        return {"jobHistory": [], "skills": [], "education": []}

    try:
        headers = {
            "X-API-Key": TINYFISH_API_KEY,
            "Content-Type": "application/json",
        }
        payload = {
            "url": linkedin_url,
            "goal": (
                "Extract the following from this LinkedIn profile and return as JSON: "
                "1. jobHistory: array of {title, company, duration} "
                "2. skills: array of skill name strings "
                "3. education: array of {degree, institution} "
                "Return ONLY valid JSON, no markdown."
            ),
        }
        response = requests.post(
            TINYFISH_SSE_URL, headers=headers, json=payload, timeout=45, stream=True
        )

        result_data: Dict = {}
        for line in response.iter_lines():
            if not line:
                continue
            line_str = line.decode("utf-8")
            if line_str.startswith("data:"):
                try:
                    data_json = json.loads(line_str[5:].strip())
                    if data_json.get("type") == "COMPLETE":
                        raw = data_json.get("resultJson") or data_json.get("result", {})
                        if isinstance(raw, str):
                            raw = json.loads(raw)
                        result_data = raw
                        break
                except (json.JSONDecodeError, KeyError):
                    continue

        return {
            "jobHistory": result_data.get("jobHistory", []),
            "skills":     result_data.get("skills", []),
            "education":  result_data.get("education", []),
        }

    except Exception:
        return {"jobHistory": [], "skills": [], "education": []}


# ══════════════════════════════════════════════════════════════════
# 4. SCORING ENGINE
# ══════════════════════════════════════════════════════════════════

def calculate_authenticity(resume_data: Dict, github_data: Dict, linkedin_data: Dict) -> int:
    """
    Authenticity = how well resume claims are backed by real activity.
    Penalises: skills on resume not seen on GitHub or LinkedIn,
               experience claims not matching LinkedIn job count.
    """
    score = 100

    resume_skills  = {s.lower() for s in resume_data.get("skills", [])}
    github_langs   = {l.lower() for l in github_data.get("languages", [])}
    linkedin_skills= {s.lower() for s in linkedin_data.get("skills", [])}

    verified_pool  = github_langs | linkedin_skills

    unverified = [s for s in resume_skills if s not in verified_pool]
    # Soft penalty — can't fully verify everything, so cap deduction
    score -= min(30, len(unverified) * 5)

    linkedin_jobs = len(linkedin_data.get("jobHistory", []))
    resume_years  = resume_data.get("experience_years", 0)

    if resume_years > 0 and linkedin_jobs == 0:
        score -= 15  # claimed experience but no LinkedIn history

    if linkedin_jobs == 0 and len(linkedin_data.get("skills", [])) == 0:
        score -= 5   # couldn't scrape LinkedIn at all, slight uncertainty

    # Bonus for certs
    score += min(10, len(resume_data.get("certifications", [])) * 5)

    return max(0, min(100, score))


def calculate_skill_match(resume_data: Dict, github_data: Dict, role: str) -> int:
    """Match candidate skills against role-specific keyword lists."""
    role_lower = role.lower()

    all_skills = {s.lower() for s in resume_data.get("skills", [])}
    all_skills |= {l.lower() for l in github_data.get("languages", [])}

    role_map = {
        "backend":   ["python", "java", "node", "go", "django", "flask", "spring", "fastapi", "api", "sql", "postgres", "redis"],
        "frontend":  ["react", "vue", "angular", "javascript", "typescript", "html", "css", "tailwind", "next.js"],
        "fullstack": ["react", "node", "python", "javascript", "api", "sql", "docker"],
        "devops":    ["docker", "kubernetes", "aws", "azure", "gcp", "ci/cd", "terraform", "ansible", "linux", "bash"],
        "data":      ["python", "sql", "tensorflow", "pytorch", "machine learning", "pandas", "spark", "kafka"],
        "mobile":    ["react native", "flutter", "swift", "kotlin", "android", "ios"],
        "ml":        ["python", "tensorflow", "pytorch", "machine learning", "deep learning", "nlp", "scikit"],
        "security":  ["penetration testing", "cybersecurity", "networking", "linux", "python", "siem"],
    }

    relevant = []
    for key, keywords in role_map.items():
        if key in role_lower:
            relevant.extend(keywords)

    if not relevant:
        # Generic fallback: score based on volume of skills detected
        return min(100, len(all_skills) * 5)

    relevant = list(set(relevant))
    matches  = sum(1 for kw in relevant if kw in all_skills)
    return min(100, max(0, int((matches / len(relevant)) * 100)))


def calculate_skills_breakdown(resume_data: Dict, github_data: Dict) -> List[Dict]:
    """Compute per-category skill scores."""
    all_skills = [s.lower() for s in resume_data.get("skills", [])]
    all_skills += [l.lower() for l in github_data.get("languages", [])]

    categories = {
        "Frontend":  ["react","vue","angular","javascript","typescript","html","css","tailwind","next.js","svelte"],
        "Backend":   ["python","java","node","go","django","flask","spring","fastapi","express","rails","php","laravel"],
        "DSA":       ["algorithm","data structure","competitive","leetcode","dynamic programming","graph","c++"],
        "DevOps":    ["docker","kubernetes","aws","azure","gcp","ci/cd","terraform","ansible","jenkins","nginx"],
        "Database":  ["sql","mongodb","postgres","mysql","redis","elasticsearch","cassandra","dynamodb"],
    }

    result = []
    for cat, keywords in categories.items():
        hits = sum(1 for s in all_skills if any(k in s for k in keywords))
        # Scale hits to 0-100; cap generously
        value = min(100, hits * 18)
        result.append({"name": cat, "value": value})
    return result


def generate_recommendation(score: int) -> str:
    if score >= 72:
        return "Strong Hire"
    elif score >= 48:
        return "Weak Hire"
    return "Reject"


# ══════════════════════════════════════════════════════════════════
# 5. AI INTERVIEW QUESTION GENERATION (Claude)
# ══════════════════════════════════════════════════════════════════

def generate_interview_questions_ai(
    resume_data: Dict,
    github_data: Dict,
    linkedin_data: Dict,
    role: str,
) -> List[str]:
    """Use Claude claude-sonnet-4-20250514 to generate contextual interview questions."""

    # Build a rich context string for Claude
    skills_str  = ", ".join(resume_data.get("skills", [])[:15]) or "Not detected"
    langs_str   = ", ".join(github_data.get("languages", []))    or "Not detected"
    jobs_str    = "; ".join(
        f"{j.get('title','?')} at {j.get('company','?')}"
        for j in linkedin_data.get("jobHistory", [])[:4]
    ) or "Not available"
    certs_str   = ", ".join(resume_data.get("certifications", [])) or "None"
    exp_years   = resume_data.get("experience_years", 0)
    resume_text = resume_data.get("raw_text", "")[:1500]

    prompt = f"""You are an expert technical recruiter generating interview questions for a {role} candidate.

CANDIDATE PROFILE:
- Resume Skills: {skills_str}
- GitHub Languages: {langs_str}
- LinkedIn Job History: {jobs_str}
- Certifications: {certs_str}
- Experience: {exp_years} years
- Resume Excerpt: {resume_text}

Generate exactly 5 highly specific, technical interview questions tailored to this exact candidate.
Questions should:
1. Reference their actual skills and tools they've used
2. Range from foundational (Q1) to senior/architectural (Q5)
3. Expose gaps or validate depth in their claimed expertise
4. Be concise (1-2 sentences each)

Return ONLY a JSON array of 5 strings, e.g.:
["Question 1", "Question 2", "Question 3", "Question 4", "Question 5"]
No markdown, no explanation, just the JSON array."""

    try:
        client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)
        message = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=600,
            messages=[{"role": "user", "content": prompt}],
        )
        raw = message.content[0].text.strip()
        # Strip markdown fences if present
        raw = re.sub(r"^```(?:json)?\s*", "", raw)
        raw = re.sub(r"\s*```$", "", raw)
        questions = json.loads(raw)
        if isinstance(questions, list) and len(questions) >= 1:
            return [str(q) for q in questions[:5]]
    except Exception:
        pass

    # ── Fallback: rule-based questions ────────────────────────────
    return _fallback_questions(resume_data, github_data, role)


def _fallback_questions(resume_data: Dict, github_data: Dict, role: str) -> List[str]:
    skills = resume_data.get("skills", [])
    langs  = github_data.get("languages", [])
    q = []
    if skills:
        q.append(f"Walk us through a production project where you used {skills[0]} — what was the hardest bug you solved?")
    else:
        q.append("Describe your most complex technical project and the biggest challenge you overcame.")
    if langs:
        q.append(f"Your GitHub shows heavy {langs[0]} usage. How do you handle performance bottlenecks in {langs[0]}?")
    else:
        q.append("How do you approach choosing a technology stack for a new project?")
    q.append(f"Design a horizontally scalable system for a core feature in the {role} domain. Walk us through your architecture decisions.")
    q.append("Describe a time you identified and resolved a critical production incident. What was your debugging process?")
    q.append("How do you balance technical debt against feature velocity, and how have you communicated this trade-off to stakeholders?")
    return q[:5]


# ══════════════════════════════════════════════════════════════════
# 6. ROUTES
# ══════════════════════════════════════════════════════════════════

@app.get("/health")
async def health():
    return {
        "status": "ok",
        "anthropic_key": bool(ANTHROPIC_API_KEY),
        "tinyfish_key":  bool(TINYFISH_API_KEY),
        "github_token":  bool(GITHUB_TOKEN),
    }


@app.post("/full-analysis", response_model=AnalysisResponse)
async def full_analysis(
    github_username: str = Form(...),
    linkedin_url:    str = Form(...),
    role:            str = Form(...),
    resume:          UploadFile = File(...),
):
    # ── Validate inputs ────────────────────────────────────────────
    if not github_username.strip():
        raise HTTPException(status_code=422, detail="GitHub username is required.")
    if not role.strip():
        raise HTTPException(status_code=422, detail="Role is required.")
    filename = resume.filename or ""
    if not filename.lower().endswith(".pdf"):
        raise HTTPException(status_code=422, detail="Only PDF resumes are accepted. Please upload a .pdf file.")

    # ── 1. Parse resume ────────────────────────────────────────────
    pdf_bytes   = await resume.read()
    resume_text = extract_pdf_text(pdf_bytes)
    if not resume_text:
        raise HTTPException(status_code=422, detail="Could not extract text from PDF. Ensure it is not a scanned image.")
    resume_data = parse_resume(resume_text)

    # ── 2. GitHub data ─────────────────────────────────────────────
    github_data = get_github_data(github_username.strip())

    # ── 3. LinkedIn data ───────────────────────────────────────────
    linkedin_data = get_linkedin_data(linkedin_url.strip())

    # ── 4. Scoring ─────────────────────────────────────────────────
    authenticity         = calculate_authenticity(resume_data, github_data, linkedin_data)
    skill_match          = calculate_skill_match(resume_data, github_data, role)
    activity_consistency = github_data.get("consistencyScore", 0)

    candidate_score = int(
        0.40 * skill_match +
        0.30 * authenticity +
        0.30 * activity_consistency
    )

    # ── 5. Derived data ────────────────────────────────────────────
    skills_breakdown   = calculate_skills_breakdown(resume_data, github_data)
    github_activity    = github_data.get("githubActivity", [])
    recommendation     = generate_recommendation(candidate_score)

    platforms = [
        {"name": "GitHub",   "value": f"{github_data.get('repoCount', 0)} repos / {github_data.get('stars', 0)} ⭐"},
        {"name": "LinkedIn", "value": f"{len(linkedin_data.get('jobHistory', []))} positions"},
    ]

    # ── 6. AI-powered interview questions ──────────────────────────
    interview_questions = generate_interview_questions_ai(
        resume_data, github_data, linkedin_data, role
    )

    return AnalysisResponse(
        candidateScore      = candidate_score,
        skillMatch          = skill_match,
        authenticity        = authenticity,
        activityConsistency = activity_consistency,
        skillsBreakdown     = [SkillBreakdown(**s) for s in skills_breakdown],
        githubActivity      = [GitHubActivity(**g) for g in github_activity],
        platforms           = [Platform(**p) for p in platforms],
        recommendation      = recommendation,
        interviewQuestions  = interview_questions,
    )


# ══════════════════════════════════════════════════════════════════
# 7. ENTRY POINT
# ══════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)