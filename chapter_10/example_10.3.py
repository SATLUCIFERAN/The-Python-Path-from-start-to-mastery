
import csv

rows = [
    ["name", "age", "grade"],
    ["Alice", 20, "A"],
    ["Bob", 21, "B+"],
    ["Charlie", 19, "A-"]
]

with open("grades.csv", "w", newline='', encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(rows)
