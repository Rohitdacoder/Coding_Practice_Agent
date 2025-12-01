# agents/leetcode_scraper.py

import requests
from typing import Dict, Any, List
import time


class LeetCodeScraper:

    BASE_URL = "https://leetcode.com/graphql"
    HEADERS = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0",
        "Referer": "https://leetcode.com/",
        "Origin": "https://leetcode.com"
    }

    # ---------------------------
    # SAFE REQUEST WRAPPER
    # ---------------------------
    def _safe_post(self, payload):
        for attempt in range(3):
            try:
                resp = requests.post(
                    self.BASE_URL,
                    json=payload,
                    headers=self.HEADERS,
                    timeout=15   # longer timeout
                )
                return resp.json()
            except Exception as e:
                print(f"⚠️ LeetCode timeout, retrying {attempt+1}/3...", e)
                time.sleep(1.5)
        print("❌ FAILED even after retries — return fallback")
        return {}

    # ---------------------------
    # FETCH PROFILE
    # ---------------------------
    def fetch_profile(self, username: str) -> Dict[str, Any]:

        query = """
        query userProfile($username: String!) {
            matchedUser(username: $username) {
                username
                submitStats {
                    acSubmissionNum {
                        difficulty
                        count
                    }
                }
            }
        }
        """

        payload = {
            "query": query,
            "variables": {"username": username}
        }

        data = self._safe_post(payload)

        if not data or "data" not in data or not data["data"].get("matchedUser"):
            print("❌ Profile Not Found — fallback to empty profile")
            return {}

        return data["data"]["matchedUser"]

    # ---------------------------
    # FETCH RECENT SUBMISSIONS
    # ---------------------------
    def fetch_recent_submissions(self, username: str) -> List[Dict[str, Any]]:
        query = """
        query recentAc($username: String!) {
          recentAcSubmissionList(username: $username, limit: 20) {
            id
            title
            titleSlug
            timestamp
          }
        }
        """

        payload = {
            "query": query,
            "variables": {"username": username}
        }

        data = self._safe_post(payload)

        if not data or "data" not in data:
            return []

        return data["data"].get("recentAcSubmissionList", [])
