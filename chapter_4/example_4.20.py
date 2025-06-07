
colors = {"red", "green", "blue"}
colors.remove("green")
print(colors)  # {'red', 'blue'}

colors = {"red", "green", "blue"}
colors.discard("green")
print(colors)  # {'red', 'blue'}

colors = {"red", "green", "blue"}
removed = colors.pop()
print(removed)  # Random item
print(colors)   # Set with one less item

colors = {"red", "green", "blue"}
colors.clear()
print(colors)  # set()
