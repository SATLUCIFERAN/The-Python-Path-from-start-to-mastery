
import pandas as pd

# Sample data
students = ["Alice", "Bob", "Charlie", "Diana", "Ethan"]
scores   = [85, 92, 78, 88, 95]

df = pd.DataFrame({
    "Student": students,
    "Score":   scores
})

# Highlight top performers (90+)
def highlight_top(s):
    return ['background-color: lightgreen' if v >= 90 else '' for v in s]

styled_df = df.style.apply(highlight_top, subset=["Score"])

# Write to Excel with style
styled_df.to_excel("gradebook.xlsx", index=False, engine="openpyxl")
