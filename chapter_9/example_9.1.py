
new_names = ["Diana", "Eve"]

with open("names.txt", "a", encoding="utf-8") as file:
    for name in new_names:
        file.write(name + "\n")
