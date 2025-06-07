
with open("users.txt", encoding="utf-8") as f:
    for name in f:
        print("Hello,", name.strip().title())

'''
Hello, Bob
Hello, Charlie
Hello,
'''