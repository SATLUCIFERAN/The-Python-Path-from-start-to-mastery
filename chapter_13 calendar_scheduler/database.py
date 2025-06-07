# database.py

import sqlite3

DB_FILE = "appointments.db"

def init_db():
    """
    Create the appointments table if it doesn’t exist.
    Schema: id (PK), date (TEXT 'YYYY-MM-DD'), time (TEXT 'HH:MM'), description (TEXT).
    """
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS appointments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            time TEXT NOT NULL,
            description TEXT NOT NULL
        )
        """
    )
    conn.commit()
    conn.close()

def fetch_appointments(date_str):
    """
    Return a list of (id, time, description) for appointments on the given date (YYYY-MM-DD).
    """
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute(
        "SELECT id, time, description FROM appointments WHERE date = ? ORDER BY time",
        (date_str,)
    )
    rows = cursor.fetchall()
    conn.close()
    return rows

def add_appointment(date_str, time_str, description):
    """
    Insert a new appointment into the database.
    Returns the new appointment’s ID.
    """
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO appointments (date, time, description) VALUES (?, ?, ?)",
        (date_str, time_str, description)
    )
    conn.commit()
    appt_id = cursor.lastrowid
    conn.close()
    return appt_id

def delete_appointment(appt_id):
    """
    Delete the appointment with the given ID.
    """
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM appointments WHERE id = ?", (appt_id,))
    conn.commit()
    conn.close()

def count_appointments_by_day(year, month):
    """
    Return a dict mapping day (int) → count of appointments on that day for the specified year/month.
    """
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    pattern = f"{year}-{month:02d}-%"
    cursor.execute(
        "SELECT SUBSTR(date, 9, 2) AS day_str, COUNT(*) "
        "FROM appointments WHERE date LIKE ? GROUP BY day_str",
        (pattern,)
    )
    rows = cursor.fetchall()
    conn.close()
    return {int(day_str): count for day_str, count in rows}
