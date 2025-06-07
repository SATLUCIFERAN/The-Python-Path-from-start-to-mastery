
import csv

with open("students.csv", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(f"{row['name']} is {row['age']} years old.")


# Alice is 20 years old.
# Bob is 21 years old.
# Charlie is 19 years old.
