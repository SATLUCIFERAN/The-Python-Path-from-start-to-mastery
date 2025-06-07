
try:
    with open("notes.txt", encoding="utf-8") as f:
        print(f.read())
except FileNotFoundError:
    print("File not found.")
except PermissionError:
    print("You don't have permission to access this file.")
except Exception as e:
    print("Unknown error:", e)
