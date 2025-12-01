import json
from tools.fetch_user_stats import fetch_stats
from utils.logger import log_info

class ProfileAnalyzerAgent:
    def analyze(self, profile_url):
        log_info("Profile Analyzer Agent running...")

        stats = fetch_stats(profile_url)

        return {
            "solved": stats.get("solved", 0),
            "topics": stats.get("topics", {}),
            "difficulty": stats.get("difficulty", {})
        }
