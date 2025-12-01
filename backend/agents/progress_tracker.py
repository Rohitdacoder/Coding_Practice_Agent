import uuid
from utils.helpers import load_long_term_memory, save_long_term_memory
from utils.logger import log_info

class ProgressTrackerAgent:
    """
    Keeps long-term memory of solved problems and daily history.
    Methods:
      - mark_solved(problem_dict)
      - is_solved(title)
      - update_daily_history(entry)
    """

    def __init__(self):
        self.mem = load_long_term_memory()

    def mark_solved(self, problem):
        log_info("ProgressTrackerAgent: mark_solved")
        solved = self.mem.get("solved_problems", [])
        if problem.get("title") not in {p["title"] for p in solved}:
            entry = {
                "id": str(uuid.uuid4()),
                "title": problem.get("title"),
                "platform": problem.get("platform"),
                "link": problem.get("link"),
                "difficulty": problem.get("difficulty")
            }
            solved.append(entry)
            self.mem["solved_problems"] = solved
            save_long_term_memory(self.mem)
            return True
        return False

    def is_solved(self, title):
        solved = self.mem.get("solved_problems", [])
        return any(s.get("title")==title for s in solved)

    def update_daily_history(self, day_str, solved_titles):
        hist = self.mem.get("daily_history", {})
        hist[day_str] = solved_titles
        self.mem["daily_history"] = hist
        save_long_term_memory(self.mem)
