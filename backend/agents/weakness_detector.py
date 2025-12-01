from utils.logger import log_info

class WeaknessDetectorAgent:
    def detect(self, user_stats):
        log_info("Weakness Detector Agent running...")

        topics = user_stats.get("topics", {})
        if not topics:
            return ["Array", "Dynamic Programming", "Graph"]  # default seed

        # simple heuristic: topics with solved count < median are weak
        counts = list(topics.values())
        counts_sorted = sorted(counts)
        median = counts_sorted[len(counts_sorted)//2] if counts_sorted else 0

        weak = [t for t, c in topics.items() if c <= median]
        # sort by ascending solved (most weak first)
        weak.sort(key=lambda t: topics.get(t, 0))
        return weak
    