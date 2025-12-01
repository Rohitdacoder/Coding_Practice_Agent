import json
import os
from datetime import datetime

METRICS_PATH = "logs/metrics.json"

def ensure_metrics():
    os.makedirs("logs", exist_ok=True)
    if not os.path.exists(METRICS_PATH):
        with open(METRICS_PATH, "w") as f:
            json.dump({"runs": []}, f, indent=2)

def push_metrics(run_id, payload):
    ensure_metrics()
    data = {}
    with open(METRICS_PATH, "r") as f:
        data = json.load(f)
    payload["run_id"] = run_id
    payload["timestamp"] = datetime.utcnow().isoformat() + "Z"
    data.setdefault("runs", []).append(payload)
    with open(METRICS_PATH, "w") as f:
        json.dump(data, f, indent=2)
