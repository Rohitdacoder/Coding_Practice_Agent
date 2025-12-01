"""
Attempts to fetch basic stats from a public profile URL.
Supports LeetCode (profile pages), CodeChef (user profile), and GeeksforGeeks (user).
This is a best-effort scraper with safe fallbacks.

If scraping fails, you get a fallback sample dict.
"""

import requests
from bs4 import BeautifulSoup
import re
from utils.helpers import safe_request, load_local_db, save_local_db

def _parse_leetcode_profile(html):
    """
    LeetCode profile pages often embed JSON inside <script> or window object.
    We look for "profileUser" or "userContestRanking" or simple stat numbers.
    """
    soup = BeautifulSoup(html, "html.parser")
    # Strategy: find scripts containing "profileUser" or "submissionNum"
    text = soup.get_text()
    # quick regex for "Solved" number
    m = re.search(r'(\d{1,5})\s+problems?\s+solved', text, re.IGNORECASE)
    solved = int(m.group(1)) if m else None

    # fallback: look for "Solved" label in page
    if solved is None:
        badges = soup.find_all("span")
        for b in badges:
            try:
                if "solved" in b.get_text().lower():
                    v = re.sub(r'[^0-9]', '', b.get_text())
                    if v:
                        solved = int(v)
                        break
            except Exception:
                continue

    # no reliable topic breakdown via scraping easily; return empty topics dict
    return {"solved": solved or 0, "topics": {}, "difficulty": {}}


def _parse_codechef_profile(html):
    soup = BeautifulSoup(html, "html.parser")
    # CodeChef shows problem-solved on profile page in a specific span/class - best effort:
    el = soup.find("div", {"class": "rating-number"})
    solved = None
    if el:
        try:
            solved = int(el.get_text().strip())
        except:
            solved = None
    return {"solved": solved or 0, "topics": {}, "difficulty": {}}


from tools.fetch_leetcode_api import fetch_leetcode_stats
from utils.helpers import load_local_db

def fetch_stats(profile_url):
    """
    Decides platform using URL.
    Currently supports:
    - LeetCode (GraphQL API)
    """

    if "leetcode.com" in profile_url:
        # extract username
        try:
            username = profile_url.rstrip("/").split("/")[-1]
        except:
            username = None

        if username:
            data = fetch_leetcode_stats(username)
            if data:
                return data

    # fallback if API fails
    return load_local_db().get("sample_stats", {
        "solved": 200,
        "topics": {"Array": 30, "DP": 15, "Graph": 12, "Tree": 18},
        "difficulty": {"easy": 90, "medium": 80, "hard": 30}
    })
