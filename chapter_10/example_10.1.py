
import csv

with open("students.csv", newline='', encoding="utf-8") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

# ['name', 'age', 'grade']
# ['Alice', '20', 'A']
# ['Bob', '21', 'B+']
# ['Charlie', '19', 'A-']
