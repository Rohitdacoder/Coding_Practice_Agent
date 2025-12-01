from tools.get_questions import get_questions
from tools.google_search_tool import fetch_editorial
from agents.difficulty_balancer import DifficultyBalancerAgent
from agents.editorial_summarizer import EditorialSummarizerAgent
from agents.progress_tracker import ProgressTrackerAgent
from utils.logger import log_info
from utils.metrics import push_metrics
import uuid

class RecommenderAgent:
    def __init__(self):
        self.balancer = DifficultyBalancerAgent()
        self.summarizer = EditorialSummarizerAgent()
        self.progress = ProgressTrackerAgent()

    def recommend(self, weak_topics, limit_per_topic=4):
        run_id = str(uuid.uuid4())
        log_info(f"RecommenderAgent run {run_id}")
        recs = []
        for topic in weak_topics[:6]:
            qs = get_questions(topic, difficulty="medium", limit=limit_per_topic)
            for q in qs:
                # skip if already solved
                if self.progress.is_solved(q.get("title")):
                    continue
                q["topic"] = topic
                # attach editorial url
                q["editorial"] = fetch_editorial(q["title"])
                q["summary"] = self.summarizer.summarize(q)
                recs.append(q)
        recs = self.balancer.balance(recs)
        push_metrics(run_id, {"recommended_count": len(recs), "topics": weak_topics[:6]})
        return recs
