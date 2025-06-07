
import json

with open("user.json", "r", encoding="utf-8") as f:
    user_data = json.load(f)

print(user_data["name"])

# Alice
