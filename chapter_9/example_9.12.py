
import json

filename = "books.json"

# Load existing books or start empty
try:
    with open(filename, encoding="utf-8") as f:
        books = json.load(f)
except FileNotFoundError:
    books = []

# Show books
print("📚 Current catalog:")
for book in books:
    print(f"- {book['title']} by {book['author']}")

# Add a book
title = input("📘 New book title: ")
author = input("✍️ Author: ")
books.append({"title": title, "author": author})

# Save back
with open(filename, "w", encoding="utf-8") as f:
    json.dump(books, f, indent=4)
print("✅ Book added.")
