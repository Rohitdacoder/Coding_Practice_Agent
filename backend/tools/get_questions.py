"""
get_questions(topic, difficulty, limit)

This function tries to query a local problems DB (JSON) first.
If a local DB is missing or empty, it uses a light scraping strategy:
 - It will check a cached local JSON file 'local_problems.json'.
 - If not present, it returns placeholder problems.

You can later populate 'memory/local_problems.json' with real problems.
"""

import os
import json
from utils.helpers import load_local_db
from urllib.parse import quote_plus

LOCAL_DB_KEY = "local_problems"

def _fallback_questions(topic, difficulty, limit=4):
    return [
        {
            "title": f"{topic} - Classic Problem {i+1}",
            "difficulty": difficulty.capitalize() if difficulty else "Medium",
            "platform": "LocalDB",
            "link": ""
        }
        for i in range(limit)
    ]

def get_questions(topic, difficulty="medium", limit=4):
    db = load_local_db()
    problems = []
    # local structure expected: {"local_problems": {"Array": [...], "Graph": [...]}}
    lp = db.get(LOCAL_DB_KEY, {})
    if lp and topic in lp:
        problems = lp[topic][:limit]
    else:
        # try fuzzy match across keys
        for k, v in lp.items():
            if topic.lower() in k.lower():
                problems.extend(v[:limit])
            if len(problems) >= limit:
                break

    if not problems:
        # return fallback synthetic list
        return _fallback_questions(topic, difficulty, limit)

    # normalize: ensure each item has required keys
    normalized = []
    for p in problems[:limit]:
        normalized.append({
            "title": p.get("title", f"{topic} Problem"),
            "difficulty": p.get("difficulty", difficulty.capitalize()),
            "platform": p.get("platform", "Unknown"),
            "link": p.get("link", "")
        })
    return normalized
