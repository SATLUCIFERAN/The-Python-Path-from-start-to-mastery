
import json

scores = [1200, 950, 870, 1430]

with open("scores.json", "w", encoding="utf-8") as f:
    json.dump(scores, f)
