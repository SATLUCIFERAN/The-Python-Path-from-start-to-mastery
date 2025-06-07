
colors = {"red", "green", "blue"}  # Set

with open("colors.txt", "w", encoding="utf-8") as f:
    for color in colors:
        f.write(color + "\n")
