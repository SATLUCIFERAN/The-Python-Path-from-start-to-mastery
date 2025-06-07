
try:
    with open("data.txt", encoding="utf-8") as f:
        content = f.read()
        print(content)
except FileNotFoundError:
    print("File not found. Please check the file name or path.")
# File not found. Please check the file name or path.
