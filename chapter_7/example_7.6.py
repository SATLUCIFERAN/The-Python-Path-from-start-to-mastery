
try:
    with open("file.txt", "r") as f:
        data = f.read()
except FileNotFoundError:
    print("File not found.")
except PermissionError:
    print("You don't have permission to read this file.")

# Output: File not found.