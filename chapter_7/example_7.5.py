
# Vague exception handling (not recommended)
try:
    with open("file.txt", "r") as f:
        data = f.read()
except:
    print("Something went wrong.")  # Too vague!





    