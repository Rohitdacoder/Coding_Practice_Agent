"""
Best-effort LeetCode recent submissions using GraphQL.
If it fails, returns empty list.
"""

import requests
from utils.logger import log_info

LEETCODE_GRAPHQL_URL = "https://leetcode.com/graphql"

def fetch_recent_submissions(username, limit=10):
    log_info("fetch_recent_submissions running...")
    query = {
        "query": """
        query recentAcSubmissions($username: String!) {
          recentAcSubmissionList(username: $username) {
            id
            title
            titleSlug
            timestamp
            lang
          }
        }
        """,
        "variables": {"username": username}
    }
    try:
        r = requests.post(LEETCODE_GRAPHQL_URL, json=query, timeout=8)
        if r.status_code == 200:
            data = r.json().get("data", {}).get("recentAcSubmissionList", [])
            return data[:limit]
    except Exception:
        pass
    return []
