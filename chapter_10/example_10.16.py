
import csv
from collections import defaultdict

region_totals = defaultdict(int)
monthly_totals = defaultdict(int)

with open("sales.csv", newline="") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        month  = row["Date"][:7]       # YYYY-MM
        sales  = int(row["Sales"])
        region = row["Region"]

        monthly_totals[month] += sales
        region_totals[region] += sales

print("Total Sales by Month:")
for month, total in monthly_totals.items():
    print(f"{month}: ${total}")

print("\nTotal Sales by Region:")
for region, total in region_totals.items():
    print(f"{region}: ${total}")
