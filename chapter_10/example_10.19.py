
import sqlite3

conn = sqlite3.connect("contacts.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS contacts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    phone TEXT,
    email TEXT
)
""")
conn.commit()

# Only insert sample data if table is empty
cursor.execute("SELECT COUNT(*) FROM contacts")
count = cursor.fetchone()[0]

if count == 0:
    contacts = [
        ("Alice Smith",   "555-1234", "alice@example.com"),
        ("Bob Jones",     "555-5678", "bob@example.com"),
        ("Charlie King",  "555-9012", "charlie@example.com")
    ]

    cursor.executemany(
        "INSERT INTO contacts (name, phone, email) VALUES (?, ?, ?)",
        contacts
    )
    conn.commit()

def search_contacts(keyword):
    cursor.execute(
        "SELECT name, phone, email FROM contacts WHERE name LIKE ?",
        (f"%{keyword}%",)
    )
    results = cursor.fetchall()

    if results:
        for name, phone, email in results:
            print(f"Name: {name}, Phone: {phone}, Email: {email}")
    else:
        print("No matches found.")

# Example usage:
search_contacts("alice")  # dont worry about letter case
# Name: Alice Smith, Phone: 555-1234, Email: alice@example.com

search_contacts("king")   # dont worry about letter case
# Name: Charlie King, Phone: 555-9012, Email: charlie@example.com

search_contacts("Jon")    # it's ok, no need to fully type "Bob Jones"
# Name: Bob Jones, Phone: 555-5678, Email: bob@example.com
