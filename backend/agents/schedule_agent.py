from utils.logger import log_info
from datetime import date, timedelta
from agents.topic_rotation import TopicRotationAgent
from agents.progress_tracker import ProgressTrackerAgent

class ScheduleAgent:
    def __init__(self):
        self.rotation = TopicRotationAgent()
        self.progress = ProgressTrackerAgent()

    def generate(self, recommendations):
        log_info("Schedule Agent running...")
        start = date.today()
        # create list of unique topics present in recommendations
        weak_topics = list({r.get("topic") for r in recommendations if r.get("topic")})
        rotation = self.rotation.rotate(weak_topics, days=7)
        schedule = {}
        n = len(recommendations)
        # map topic->problems
        by_topic = {}
        for r in recommendations:
            by_topic.setdefault(r.get("topic","Unknown"), []).append(r)

        for i in range(7):
            day = start + timedelta(days=i)
            topics_for_day = rotation[i]
            items = []
            for t in topics_for_day:
                items.extend(by_topic.get(t, [])[:2])
            # remove duplicates, skip solved
            filtered = []
            for item in items:
                if not self.progress.is_solved(item.get("title")) and item not in filtered:
                    filtered.append(item)
            schedule[day.isoformat()] = filtered
        return schedule
