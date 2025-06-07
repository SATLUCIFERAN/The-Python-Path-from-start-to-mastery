
import json

user = {"name": "Alice", "age": 28, "is_admin": False}

with open("user.json", "w", encoding="utf-8") as f:
    json.dump(user, f, indent=4)
