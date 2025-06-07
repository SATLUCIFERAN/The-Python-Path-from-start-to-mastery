

try:
    with open("notes.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("File not found.")






    