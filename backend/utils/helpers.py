"""
helpers.py

Utility helpers: safe HTTP request, local DB (JSON) load/save, small utilities.
"""

import requests
import time
import json
import os
from typing import Optional

LONG_TERM_PATH = os.path.join("memory", "long_term_memory.json")
LOCAL_DB_PATH = os.path.join("memory", "local_db.json")

def safe_request(url: str, max_retries: int = 3, backoff: float = 0.5, timeout: int = 8) -> Optional[requests.Response]:
    headers = {
        "User-Agent": "DSA-Agent-Bot/1.0 (+https://example.com)"
    }
    for attempt in range(max_retries):
        try:
            r = requests.get(url, headers=headers, timeout=timeout)
            if r.status_code == 200:
                return r
            elif r.status_code in (429, 503):
                # rate-limited or service unavailable: backoff
                time.sleep(backoff * (attempt + 1))
            else:
                # other HTTP errors: break
                return r
        except requests.RequestException:
            time.sleep(backoff * (attempt + 1))
    return None

def load_local_db() -> dict:
    if not os.path.exists(LOCAL_DB_PATH):
        # ensure memory directory exists
        os.makedirs(os.path.dirname(LOCAL_DB_PATH), exist_ok=True)
        # create a starter local DB
        starter = {
            "sample_stats": {
                "solved": 320,
                "topics": {"Array": 40, "DP": 15, "Graph": 10, "Tree": 18},
                "difficulty": {"easy": 150, "medium": 120, "hard": 50}
            },
            "local_problems": {
                "Array": [
                    {"title": "Two Sum", "difficulty": "Easy", "platform": "LeetCode", "link": "https://leetcode.com/problems/two-sum"},
                    {"title": "Subarray Sum Equals K", "difficulty": "Medium", "platform": "LeetCode", "link": "https://leetcode.com/problems/subarray-sum-equals-k"}
                ],
                "Graph": [
                    {"title": "Number of Provinces", "difficulty": "Medium", "platform": "LeetCode", "link": "https://leetcode.com/problems/number-of-provinces"},
                    {"title": "Course Schedule", "difficulty": "Medium", "platform": "LeetCode", "link": "https://leetcode.com/problems/course-schedule"}
                ]
            }
        }
        with open(LOCAL_DB_PATH, "w", encoding="utf-8") as f:
            json.dump(starter, f, indent=2)
        return starter

    try:
        with open(LOCAL_DB_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {}

def save_local_db(data: dict):
    os.makedirs(os.path.dirname(LOCAL_DB_PATH), exist_ok=True)
    with open(LOCAL_DB_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

def slugify(text: str) -> str:
    import re
    s = text.lower().strip()
    s = re.sub(r'[^a-z0-9]+', '-', s)
    s = re.sub(r'-{2,}', '-', s).strip('-')
    return s

def load_long_term_memory():
    if not os.path.exists(LONG_TERM_PATH):
        os.makedirs(os.path.dirname(LONG_TERM_PATH), exist_ok=True)
        starter = {"solved_problems": [], "daily_history": {}, "topic_progress": {}}
        with open(LONG_TERM_PATH, "w") as f:
            json.dump(starter, f, indent=2)
        return starter
    try:
        with open(LONG_TERM_PATH, "r") as f:
            return json.load(f)
    except Exception:
        return {"solved_problems": [], "daily_history": {}, "topic_progress": {}}

def save_long_term_memory(data):
    os.makedirs(os.path.dirname(LONG_TERM_PATH), exist_ok=True)
    with open(LONG_TERM_PATH, "w") as f:
        json.dump(data, f, indent=2)
