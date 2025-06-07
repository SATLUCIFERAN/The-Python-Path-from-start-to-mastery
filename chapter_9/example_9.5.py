
names = ["Alice", "Bob", "Charlie"]
with open("names.txt", "w", encoding="utf-8") as f:
    f.writelines(name + "\n" for name in names)
