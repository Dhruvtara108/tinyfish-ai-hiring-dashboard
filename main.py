from fastapi import FastAPI, UploadFile, File
import requests
import os
from dotenv import load_dotenv
import json
import fitz

load_dotenv()

app = FastAPI()

TINYFISH_API_KEY = os.getenv("TINYFISH_API_KEY")


@app.get("/")
def home():
    return {"message": "AI Hiring Copilot Backend Running"}


@app.get("/analyze-candidate")
def analyze_candidate(github_username: str, role: str):

    url = "https://agent.tinyfish.ai/v1/automation/run-sse"

    headers = {
        "X-API-Key": TINYFISH_API_KEY,
        "Content-Type": "application/json"
    }

    data = {
        "url": f"https://github.com/{github_username}",
        "goal": (
            f"Analyze this GitHub profile: {github_username}. "
            f"Evaluate suitability for the role: {role}. "
            "Assess activity level, languages used, project quality, "
            "consistency, and authenticity indicators. "
            "Return structured JSON with hiring recommendation."
        )
    }

    response = requests.post(url, headers=headers, json=data)
    text = response.text

    lines = text.split("\n")
    for line in lines:
        if line.startswith("data:"):
            try:
                event = json.loads(line.replace("data: ", ""))
                if event.get("type") == "COMPLETE":
                    return event.get("resultJson")
            except:
                continue

    return {"error": "Analysis failed", "raw_response": text}


@app.post("/upload-resume")
async def upload_resume(file: UploadFile = File(...)):
    contents = await file.read()

    with open("temp_resume.pdf", "wb") as f:
        f.write(contents)

    text = ""
    doc = fitz.open("temp_resume.pdf")
    for page in doc:
        text += page.get_text()

    return {
        "resume_text_preview": text[:1000],
        "status": "Resume text extracted successfully"
    }


@app.post("/full-analysis")
async def full_analysis(
    github_username: str,
    role: str,
    file: UploadFile = File(...)
):

    contents = await file.read()

    with open("temp_resume.pdf", "wb") as f:
        f.write(contents)

    resume_text = ""
    doc = fitz.open("temp_resume.pdf")
    for page in doc:
        resume_text += page.get_text()

    url = "https://agent.tinyfish.ai/v1/automation/run-sse"

    headers = {
        "X-API-Key": TINYFISH_API_KEY,
        "Content-Type": "application/json"
    }

    data = {
        "url": f"https://github.com/{github_username}",
        "goal": (
            f"Analyze GitHub profile {github_username} "
            f"for role {role}. "
            f"Compare with this resume content: {resume_text[:3000]}. "
            "Check skill match, authenticity, inconsistencies, "
            "and generate hiring recommendation with interview questions. "
            "Return structured JSON."
        )
    }

    response = requests.post(url, headers=headers, json=data)
    text = response.text

    lines = text.split("\n")
    for line in lines:
        if line.startswith("data:"):
            try:
                event = json.loads(line.replace("data: ", ""))
                if event.get("type") == "COMPLETE":
                    return event.get("resultJson")
            except:
                continue

    return {"error": "Full analysis failed", "raw_response": text}