
import pandas as pd

data = {
    "Item": ["Coffee", "Notebook", "Pen", "USB Drive"],
    "Quantity": [2, 1, 5, 1],
    "Price": [60, 45, 10, 120]
}

df = pd.DataFrame(data)

# Calculation each unit
df["Total"] = df["Quantity"] * df["Price"]

# Save DataFrame to Excel
df.to_excel("updated_expenses.xlsx", index=False)

print("✅ Excel file 'updated_expenses.xlsx' saved successfully.")
