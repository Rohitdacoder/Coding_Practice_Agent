# agents/recommender.py
"""
This file contains all modern recommendation helpers used by main_agent.py:
- topic weakness detection
- difficulty stats
- question recommendations
- schedule generation
- learning path generation
"""

from agents.question_fetcher import fetch_topic_questions
import random



# ---------------------------------------------------------
# 1. Difficulty Stats
# ---------------------------------------------------------

def build_difficulty_stats(profile):
    stats = {"easy": 0, "medium": 0, "hard": 0}

    arr = profile.get("submitStats", {}).get("acSubmissionNum", [])

    for entry in arr:
        d = entry.get("difficulty", "").lower()
        if d in stats:
            stats[d] = entry.get("count", 0)

    return stats



# ---------------------------------------------------------
# 2. Weak Topics
# ---------------------------------------------------------

def build_weak_topics(profile_data, top_n=4):
    fallback_topics = [
        "Arrays", "Strings", "Binary Search", "DP", "Hashing",
        "Two Pointers", "Stack", "Tree", "Graph", "Recursion"
    ]

    # If LeetCode API failed OR topics could not be extracted → fallback
    if not profile_data:
        random.shuffle(fallback_topics)
        return fallback_topics[:top_n]

    # TODO: extract real weak topics later
    random.shuffle(fallback_topics)
    return fallback_topics[:top_n]



# ---------------------------------------------------------
# 3. Recommendation Generator
# ---------------------------------------------------------

def generate_recommendations(weak_topics, difficulty_stats, limit=20):
    """
    Build simple hardcoded recommendations based on weak topics.
    Later: integrate real scraping.
    """

    sample_questions = [
        {"title": "Two Sum", "platform": "LeetCode", "difficulty": "Easy", "link": "https://leetcode.com/problems/two-sum/"},
        {"title": "Climbing Stairs", "platform": "LeetCode", "difficulty": "Easy", "link": "https://leetcode.com/problems/climbing-stairs/"},
        {"title": "Binary Search", "platform": "LeetCode", "difficulty": "Easy", "link": "https://leetcode.com/problems/binary-search/"},
        {"title": "Valid Parentheses", "platform": "LeetCode", "difficulty": "Easy", "link": "https://leetcode.com/problems/valid-parentheses/"},
        {"title": "House Robber", "platform": "LeetCode", "difficulty": "Medium", "link": "https://leetcode.com/problems/house-robber/"}
    ]

    out = []

    for t in weak_topics:
        for q in sample_questions:
            out.append({
                **q,
                "topic": t,
                "editorial": f"https://www.google.com/search?q={q['title']}+editorial",
                "summary": f"Hint: This question belongs to {t}. Try applying subproblem breakdown."
            })

    return out[:limit]


# ---------------------------------------------------------
# 4. Schedule Generator
# ---------------------------------------------------------

def generate_schedule(recommendations, days=7):
    """
    Distribute problems across N days.
    """
    schedule = {}

    i = 0
    for day in range(1, days + 1):
        schedule[f"Day {day}"] = recommendations[i:i + 3]
        i += 3

    return schedule


# ---------------------------------------------------------
# 5. Learning Path Preview
# ---------------------------------------------------------
def generate_learning_path_preview(weak_topics, days=7):
    if not weak_topics:
        return []
    
    path = []

    for i in range(days):
        topic = weak_topics[i % len(weak_topics)]
        problems = fetch_topic_questions(topic, limit=3)

        if not problems:
            # fallback if API fails
            problems = [{"title": f"{topic} Problem {k+1}", "difficulty": "Medium"} for k in range(3)]

        path.append({
            "day": i+1,
            "topic": topic,
            "problems": problems[:3]
        })

    return path
