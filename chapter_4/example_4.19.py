
#Adds a single element to the set.

colors = {"red", "green", "blue"}
colors.add("yellow")
print(colors)  # {'red', 'green', 'blue', 'yellow'}

#Adds multiple items from another iterable (like a list, tuple, or another set).
colors = {"red", "green"}
colors.update(["blue", "yellow"])
print(colors)  # {'red', 'green', 'blue', 'yellow'}

'''
However the order is not guaranteed because sets in Python are unordered collections.
So, the actual printed output may vary
'''

