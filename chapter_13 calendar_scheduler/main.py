# main.py

import tkinter as tk
from ui_calendar import CalendarApp

if __name__ == "__main__":
    root = tk.Tk()
    app = CalendarApp(root)
    root.mainloop()
