# utils.py

import calendar
from datetime import datetime

def is_valid_date(year, month, day):
    """
    Return True if (year, month, day) is a valid calendar date.
    """
    try:
        datetime(year, month, day)
        return True
    except ValueError:
        return False

def format_date(year, month, day):
    """
    Return a zero-padded string "YYYY-MM-DD" for the given year, month, day.
    """
    return f"{year}-{month:02d}-{day:02d}"

def get_month_name(month):
    """
    Return the full English name of the given month (1–12).
    """
    return calendar.month_name[month]
