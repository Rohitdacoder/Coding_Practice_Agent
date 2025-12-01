from fastapi import FastAPI
from backend.main_agent import run_flow
from backend.agents.progress_tracker import ProgressTrackerAgent
from backend.utils.helpers import load_local_db
from fastapi import FastAPI, HTTPException
from typing import Dict, Any
from main_agent import run_flow
from fastapi.middleware.cors import CORSMiddleware
from main_agent import generate_full_profile


import logging
logging.basicConfig(level=logging.DEBUG)


app = FastAPI(title="DSA Agent API")

# Allow CORS from local dev / phone
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/full_profile")
def full_profile(profile: str):
    try:
        return generate_full_profile(profile)
    except Exception as e:
        print("🔥 Full Profile Error:", e)
        return {"error": str(e)}


@app.get("/")
def root():
    return {"message": "DSA Agent API running successfully!"}

@app.get("/stats")
def stats(profile: str):
    try:
        result = generate_full_profile(profile)  # your scraper logic

        return {
            "solved": result["user_stats"]["solved"],
            "difficulty": result["user_stats"]["difficulty"],
            "topics": result["user_stats"]["topics"]
        }

    except Exception as e:
        print("🔥 Stats Error:", e)
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/weak_topics")
def weak_topics(profile: str):
    return run_flow(profile)["weak_topics"]

@app.get("/recommendations")
def recommendations(profile: str):
    try:
        return run_flow(profile)["recommendations"]
    except Exception as e:
        print("🔥 ERROR:", e)
        import traceback
        traceback.print_exc()
        raise e

@app.get("/schedule")
def schedule(profile: str):
    try:
        out = run_flow(profile)
        return out.get("schedule", {})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/learning_path")
def path(profile: str):
    try:
        result = run_flow(profile)
        return {
            "learning_path_preview": result["learning_path_preview"]
        }
    except Exception as e:
        print("🔥 Path Error:", e)
        raise e

@app.post("/mark_solved")
def mark_solved(title: str):
    progress = ProgressTrackerAgent()
    db = load_local_db()
    problems = db.get("local_problems", {})
    for arr in problems.values():
        for p in arr:
            if p.get("title").lower() == title.lower():
                ok = progress.mark_solved(p)
                return {"status": "ok" if ok else "already_marked"}
    return {"status": "not_found"}
