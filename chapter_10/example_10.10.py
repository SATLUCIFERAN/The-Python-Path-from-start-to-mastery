import pandas as pd

# Read back the data and add 'Stapler'
df = pd.read_excel("office.xlsx")

# Add a new row for 'Stapler'
new_row = pd.DataFrame([{"Item": "Stapler", "Quantity": 1, "Price": 75}])
df = pd.concat([df, new_row], ignore_index=True)

# Update 'Stapler' quantity by adding 3  # Now it's 4
df.loc[df["Item"] == "Stapler", "Quantity"] += 3

# Recalculate total
df["Total"] = df["Quantity"] * df["Price"]

# Save to updated Excel file
df.to_excel("office_updated.xlsx", index=False)
print("✅ 'office_updated.xlsx' saved with updated Stapler quantity.")
