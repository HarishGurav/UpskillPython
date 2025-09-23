 
import json
from typing import List
from fastapi import FastAPI
from pydantic import BaseModel
from .data import skills
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI()
origins = [
    "http://localhost:4200",  # Angular dev server
    # "http://your-domain.com",  # Add your production domain if needed
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,     # List of allowed origins
    allow_credentials=True,    # Allow cookies
    allow_methods=["*"],       # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],       # Allow all headers
)

print(os.getcwd())
# API 1: Get list of skills
@app.get("/skills")
def get_skills():
    return {"skills": skills}

# Load jobs data from JSON
with open("app/jobProfiles.json") as f:
    jobs = json.load(f)

# Request model
class SkillsRequest(BaseModel):
    skills: List[str]

# Response model
class JobResponse(BaseModel):
    title: str
    description: str
    skills: List[str]

# API endpoint
@app.post("/matching-jobs", response_model=List[JobResponse])
def match_jobs(request: SkillsRequest):
    user_skills = set([skill.lower() for skill in request.skills])
    matched_jobs = []

    for job in jobs:
        job_skills = set([s.lower() for s in job["skills"]])
        matched_count = len(user_skills & job_skills)
        if matched_count > 0:
            matched_jobs.append({
                "title": job["title"],
                "description": job["description"],
                "skills": job["skills"],
                "matched_count": matched_count  # optional, for sorting
            })

    # Sort by number of matching skills (highest first)
    matched_jobs.sort(key=lambda j: j["matched_count"], reverse=True)

    # Return only top 5 matches
    top_jobs = matched_jobs[:5]

    # Remove the 'matched_count' key before returning
    for job in top_jobs:
        job.pop("matched_count", None)

    return top_jobs

    user_skills = set([skill.lower() for skill in request.skills])  # case-insensitive match
    matched_jobs = []

    for job in jobs:
        job_skills = set([skill.lower() for skill in job["skills"]])
        intersection = user_skills & job_skills
        if intersection:
            matched_jobs.append({
                "title": job["title"],
                "description": job["description"],
                "skills": job["skills"]
            })

    # Optional: sort by number of matched skills (most relevant first)
    matched_jobs.sort(key=lambda j: len(set([s.lower() for s in j["skills"]]) & user_skills), reverse=True)

    return matched_jobs
