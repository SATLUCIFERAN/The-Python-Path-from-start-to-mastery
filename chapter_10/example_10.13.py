


import sqlite3
from pathlib import Path

conn = sqlite3.connect(Path("data") / "books.db")

cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    author TEXT,
    year INTEGER
)
''')

cursor.execute(
    "INSERT INTO books (title, author, year) VALUES (?, ?, ?)",
    ("1984", "George Orwell", 1949)
)
conn.commit()  # Save the change


cursor.execute(
    "UPDATE books SET year = ? WHERE title = ?",
    (1950, "1984")
)
conn.commit()

cursor.execute("SELECT * FROM books")
rows = cursor.fetchall()

for row in rows:
    print(row)

# (1, '1984', 'George Orwell', 1950)
