from utils.logger import log_info

class EvaluationAgent:
    def validate(self, recommendations):
        log_info("Evaluation Agent running...")
        evaluation = []
        for r in recommendations:
            ok = isinstance(r.get("title"), str) and r.get("link")
            evaluation.append({
                "title": r.get("title"),
                "platform": r.get("platform"),
                "is_valid": bool(ok)
            })
        return evaluation
