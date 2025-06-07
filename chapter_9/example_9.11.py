
filename = "feedback.txt"

try:
    with open(filename, "r", encoding="utf-8") as file:
        previous = file.read()
        if previous.strip():
            print("📋 Previous feedback:\n")
            print(previous)
        else:
            print("🆕 No feedback yet.")
except FileNotFoundError:
    print("📁 No feedback file found yet. This is the first entry!")
