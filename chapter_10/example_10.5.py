
import csv

data = [
    {"name": "Alice", "age": 20, "grade": "A"},
    {"name": "Bob",   "age": 21, "grade": "B+"}
]

with open("output.csv", "w", newline='', encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "age", "grade"])
    writer.writeheader()
    writer.writerows(data)
