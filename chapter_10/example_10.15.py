
import sqlite3

try:
    conn = sqlite3.connect("books.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM books")
    print(cursor.fetchall())
except sqlite3.Error as e:
    print("Database error:", e)
finally:
    conn.close()
