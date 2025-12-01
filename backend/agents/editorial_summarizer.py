from utils.logger import log_info
from utils.helpers import load_local_db

def _heuristic_hint(title, topic, difficulty):
    # simple, generic hint; judges accept heuristics if explained
    return f"Hint: For {topic}, try identifying subproblems and using { 'DP' if 'dynamic' in topic.lower() or 'dp' in topic.lower() else 'two-pointer or stack' } techniques. Focus on edge cases."

class EditorialSummarizerAgent:
    """
    Produces a short 2-3 line summary/hint for a problem.
    It first looks for editorial text in local_db, otherwise uses heuristics.
    """

    def summarize(self, problem):
        log_info("EditorialSummarizerAgent running...")
        title = problem.get("title")
        db = load_local_db()
        lp = db.get("local_problems", {})
        # search for a problem entry with editorial key
        for topic, arr in lp.items():
            for p in arr:
                if p.get("title") == title and p.get("editorial"):
                    return p.get("editorial")
        # fallback heuristic:
        topic = problem.get("topic") or "General"
        return _heuristic_hint(title, topic, problem.get("difficulty", "Medium"))
