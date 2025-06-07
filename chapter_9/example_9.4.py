
import json

profile = {"name": "Alice", "score": 95}

with open("profile.json", "w", encoding="utf-8") as f:
    json.dump(profile, f, indent=4)
