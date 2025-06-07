

import pandas as pd

# Sample data
students = ["Alice", "Bob", "Charlie", "Diana", "Ethan"]
scores   = [85,      92,    78,        88,      95]

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



# Count grades into ranges
bins = [0, 60, 70, 80, 90, 100]
labels = ["F", "D", "C", "B", "A"]
df['Grade'] = pd.cut(df['Score'], bins=bins, labels=labels, right=False)

distribution = df['Grade'].value_counts().sort_index()

# Create writer for multiple sheets
with pd.ExcelWriter("gradebook_with_distribution.xlsx", engine='openpyxl') as writer:
    df.to_excel(writer, sheet_name="Scores", index=False)
    distribution.to_frame(name="Count").to_excel(writer, sheet_name="Distribution")
