# main_agent.py  (FINAL FIXED VERSION)

import argparse
import json
from typing import Dict, Any

from agents.leetcode_scraper import LeetCodeScraper
from agents.recommender import (
    build_difficulty_stats,
    build_weak_topics,
    generate_schedule,
    generate_learning_path_preview
)
from agents.recommender_agent import RecommenderAgent


def extract_username_from_profile(profile_link: str) -> str:
    """Extract username from LeetCode profile URL."""
    return profile_link.rstrip("/").split("/")[-1]


def run_flow(profile_link: str) -> Dict[str, Any]:
    """Main data pipeline used internally."""

    username = extract_username_from_profile(profile_link)
    scraper = LeetCodeScraper()

    # Default structure (safe fallback)
    result = {
        "user_stats": {},
        "weak_topics": [],
        "recommendations": [],
        "schedule": {},
        "learning_path_preview": [],
        "recent": []
    }

    # 1. Fetch profile + recent AC
    try:
        profile_data = scraper.fetch_profile(username) or {}
        recent = scraper.fetch_recent_submissions(username) or []
    except Exception:
        profile_data = {}
        recent = []

    # 2. Stats
    difficulty_stats = build_difficulty_stats(profile_data)
    weak_topics = build_weak_topics(profile_data, top_n=4)

    # 3. Recommendations
    rec_agent = RecommenderAgent()
    recommendations = rec_agent.recommend(weak_topics, limit_per_topic=4)

    # 4. Schedule
    schedule = generate_schedule(recommendations, days=7)

    # 5. Learning Path Preview
    learning_path_preview = generate_learning_path_preview(weak_topics, days=7)

    # 6. User Stats (Android StatsResponse model)
    user_stats = {
        "solved": sum(difficulty_stats.values()),
        "topics": {t: 0 for t in weak_topics},
        "difficulty": difficulty_stats,
    }

    # 7. Final structure
    result.update({
        "user_stats": user_stats,
        "weak_topics": weak_topics,
        "recommendations": recommendations,
        "schedule": schedule,
        "learning_path_preview": learning_path_preview,
        "recent": recent
    })

    return result


# -----------------------------------------------------
# ✅ NEW — required for /full_profile endpoint
# -----------------------------------------------------
def generate_full_profile(profile_link: str) -> Dict[str, Any]:
    """
    Wrapper for API server to return the full dataset.
    Your Android app expects EXACTLY this shape.
    """
    data = run_flow(profile_link)

    return {
        "user_stats": data["user_stats"],
        "weak_topics": data["weak_topics"],
        "recommendations": data["recommendations"],
        "schedule": data["schedule"],
        "learning_path_preview": data["learning_path_preview"],
        "recent": data["recent"]
    }


# -----------------------------------------------------
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--profile", type=str, default="https://leetcode.com/u/rohitdacoder/")
    args = parser.parse_args()

    out = run_flow(args.profile)
    print(json.dumps(out, indent=2))
