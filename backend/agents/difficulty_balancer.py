from utils.logger import log_info

class DifficultyBalancerAgent:
    """
    Rebalances recommended problems to match target distribution.
    Default target: 40% easy, 50% medium, 10% hard (by count).
    """
    def __init__(self, target=None):
        self.target = target or {"easy": 0.4, "medium": 0.5, "hard": 0.1}

    def balance(self, recommendations):
        log_info("DifficultyBalancerAgent running...")
        if not recommendations:
            return recommendations

        # convert difficulty names to lowercase
        buckets = {"easy": [], "medium": [], "hard": []}
        for r in recommendations:
            d = (r.get("difficulty") or "medium").lower()
            if d not in buckets:
                d = "medium"
            buckets[d].append(r)

        total = len(recommendations)
        # desired counts
        desired = {k: max(1, int(round(self.target[k]*total))) for k in self.target}
        balanced = []
        # take up to desired from each bucket, then fill remaining
        for k in ["easy","medium","hard"]:
            take = min(len(buckets[k]), desired[k])
            balanced.extend(buckets[k][:take])

        # fill remaining slots with medium/easy/hard priority
        remaining = total - len(balanced)
        pool = buckets["medium"] + buckets["easy"] + buckets["hard"]
        i = 0
        while remaining > 0 and i < len(pool):
            item = pool[i]
            if item not in balanced:
                balanced.append(item)
                remaining -= 1
            i += 1

        return balanced
