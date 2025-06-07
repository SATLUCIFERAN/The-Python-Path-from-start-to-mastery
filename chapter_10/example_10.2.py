
import csv

with open("students.csv", newline='', encoding="utf-8") as f:
    reader = csv.reader(f)
    next(reader)   # skip header
    for row in reader:
        print(f"{row[0]} got a grade of {row[2]}")


# Alice got a grade of A
# Bob got a grade of B+
# Charlie got a grade of A-
