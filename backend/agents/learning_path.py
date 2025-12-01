from utils.logger import log_info
from datetime import date, timedelta

class LearningPathAgent:
    """
    Generate a 30-day learning path based on weak topics.
    Very simple algorithm:
      - focus more on weakest topics first
      - gradually increase difficulty
    """

    def generate_30_day(self, weak_topics, problems_by_topic, start_date=None):
        log_info("LearningPathAgent running...")
        if not start_date:
            start_date = date.today()
        plan = {}
        n = len(weak_topics) if weak_topics else 1
        # For each day, assign 2 problems rotating topics, increase difficulty every 7 days.
        for i in range(30):
            day = (start_date + timedelta(days=i)).isoformat()
            t = weak_topics[i % n] if weak_topics else "Array"
            # pick 2 problems from problems_by_topic
            candidates = problems_by_topic.get(t, [])[:4]
            # choose two (if present)
            day_problems = []
            if candidates:
                day_problems.append(candidates[i % len(candidates)])
                if len(candidates) > 1:
                    day_problems.append(candidates[(i+1) % len(candidates)])
            plan[day] = day_problems
        return plan
