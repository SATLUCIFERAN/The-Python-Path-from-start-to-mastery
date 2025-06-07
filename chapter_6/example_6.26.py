
words = ["apple", "banana", "cherry"]
words.sort(key=lambda word: word[-1])
print(words)  # ['banana', 'apple', 'cherry']