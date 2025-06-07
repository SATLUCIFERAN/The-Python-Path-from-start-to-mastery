# import tkinter as tk
# from tkinter import messagebox, simpledialog, ttk
# import sqlite3
# import calendar
# from datetime import datetime

# DB_FILE = "appointments.db"

# class CalendarApp:
#     def __init__(self, master):
#         self.master = master
#         master.title("Calendar & Appointment Scheduler")
#         master.geometry("800x700")
#         master.resizable(True, True)

#         # Initialize database
#         self.init_db()

#         # Track current month/year
#         today = datetime.today()
#         self.current_year = today.year
#         self.current_month = today.month

#         # ---------- TOP CONTAINER ----------
#         top_container = tk.Frame(master, bg="#f0f0f0")
#         top_container.pack(fill=tk.X)

#         # -- Date Picker Frame --
#         dp_frame = tk.Frame(top_container, bg="#f0f0f0", pady=10)
#         dp_frame.pack(fill=tk.X, padx=20)

#         lbl_style = {"font": ("Arial", 10), "bg": "#f0f0f0"}
#         cmb_style = {"font": ("Arial", 10), "width": 6}

#         # Year Combobox
#         years = list(range(today.year - 5, today.year + 6))
#         self.year_var = tk.IntVar(value=self.current_year)
#         year_cb = ttk.Combobox(
#             dp_frame, values=years, textvariable=self.year_var,
#             state="readonly", **cmb_style
#         )
#         year_cb.grid(row=0, column=0, padx=(0, 5))
#         tk.Label(dp_frame, text="Year", **lbl_style).grid(row=1, column=0)

#         # Month Combobox
#         months = list(range(1, 13))
#         self.month_var = tk.IntVar(value=self.current_month)
#         month_cb = ttk.Combobox(
#             dp_frame, values=months, textvariable=self.month_var,
#             state="readonly", **cmb_style
#         )
#         month_cb.grid(row=0, column=1, padx=(0, 5))
#         tk.Label(dp_frame, text="Month", **lbl_style).grid(row=1, column=1)

#         # Day Combobox
#         days = list(range(1, 32))
#         self.day_var = tk.IntVar(value=today.day)
#         day_cb = ttk.Combobox(
#             dp_frame, values=days, textvariable=self.day_var,
#             state="readonly", **cmb_style
#         )
#         day_cb.grid(row=0, column=2, padx=(0, 10))
#         tk.Label(dp_frame, text="Day", **lbl_style).grid(row=1, column=2)

#         # Go Button
#         go_btn = tk.Button(
#             dp_frame, text="Go", font=("Arial", 10, "bold"),
#             command=self.on_dropdown_go, bg="#007acc", fg="white", bd=0, padx=10, pady=5
#         )
#         go_btn.grid(row=0, column=3, rowspan=2, padx=(10, 0))

#         # Separator
#         sep = ttk.Separator(top_container, orient="horizontal")
#         sep.pack(fill=tk.X, padx=20, pady=(0, 10))

#         # -- Month Navigator Frame --
#         nav_frame = tk.Frame(top_container, bg="#f0f0f0")
#         nav_frame.pack(fill=tk.X, pady=(0, 10))

#         self.prev_btn = tk.Button(
#             nav_frame, text="<", font=("Arial", 12), width=3,
#             command=self.go_prev_month, bg="white", bd=1
#         )
#         self.prev_btn.pack(side=tk.LEFT, padx=(20, 5))

#         self.month_label = tk.Label(
#             nav_frame, text="", font=("Arial", 16, "bold"),
#             bg="#f0f0f0"
#         )
#         self.month_label.pack(side=tk.LEFT, padx=5)

#         self.next_btn = tk.Button(
#             nav_frame, text=">", font=("Arial", 12), width=3,
#             command=self.go_next_month, bg="white", bd=1
#         )
#         self.next_btn.pack(side=tk.LEFT, padx=(5, 20))

#         # ---------- CALENDAR GRID CONTAINER ----------
#         self.cal_frame = tk.Frame(master)
#         self.cal_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=(0, 20))

#         # Weekday headers with dark background
#         days_names = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
#         for idx, dname in enumerate(days_names):
#             lbl = tk.Label(
#                 self.cal_frame, text=dname, font=("Arial", 12, "bold"),
#                 bg="#2e2e2e", fg="white"
#             )
#             lbl.grid(row=0, column=idx, padx=2, pady=2, sticky="nsew")

#         # Configure weights so grid expands proportionally
#         for col in range(7):
#             self.cal_frame.columnconfigure(col, weight=1)
#         self.cal_frame.rowconfigure(0, weight=0)
#         for r in range(1, 7):
#             self.cal_frame.rowconfigure(r, weight=1)

#         # Create 6×7 day-buttons
#         self.day_buttons = []
#         for r in range(1, 7):
#             row_buttons = []
#             for c in range(7):
#                 btn = tk.Button(
#                     self.cal_frame, text="", font=("Arial", 11),
#                     command=lambda r=r, c=c: self.on_day_click(r, c),
#                     bd=1, relief="raised"
#                 )
#                 btn.grid(row=r, column=c, padx=2, pady=2, sticky="nsew")
#                 row_buttons.append(btn)
#             self.day_buttons.append(row_buttons)

#         # Initially populate the calendar
#         self.populate_calendar(self.current_year, self.current_month)


#     # def init_db(self):
#     #     conn = sqlite3.connect(DB_FILE)
#     #     cursor = conn.cursor()
#     #     cursor.execute(
#     #         """
#     #         CREATE TABLE IF NOT EXISTS appointments (
#     #             id INTEGER PRIMARY KEY AUTOINCREMENT,
#     #             date TEXT NOT NULL,
#     #             time TEXT NOT NULL,
#     #             description TEXT NOT NULL
#     #         )
#     #         """
#     #     )
#     #     conn.commit()
#     #     conn.close()


#     # def fetch_appointments(self, date_str):
#     #     conn = sqlite3.connect(DB_FILE)
#     #     cursor = conn.cursor()
#     #     cursor.execute(
#     #         "SELECT id, time, description FROM appointments WHERE date = ? ORDER BY time",
#     #         (date_str,)
#     #     )
#     #     rows = cursor.fetchall()
#     #     conn.close()
#     #     return rows


#     # def add_appointment(self, date_str):
#     #     time_input = simpledialog.askstring(
#     #         "Appointment Time", "Enter time (HH:MM):", parent=self.master
#     #     )
#     #     if not time_input:
#     #         return
#     #     try:
#     #         datetime.strptime(time_input, "%H:%M")
#     #     except ValueError:
#     #         messagebox.showerror("Invalid Time", "Time must be in HH:MM format (24-hour).")
#     #         return

#     #     desc = simpledialog.askstring("Description", "Enter description:", parent=self.master)
#     #     if not desc:
#     #         return

#     #     conn = sqlite3.connect(DB_FILE)
#     #     cursor = conn.cursor()
#     #     cursor.execute(
#     #         "INSERT INTO appointments (date, time, description) VALUES (?, ?, ?)",
#     #         (date_str, time_input, desc)
#     #     )
#     #     conn.commit()
#     #     conn.close()
#     #     messagebox.showinfo("Saved", "Appointment added.")
#     #     self.populate_calendar(self.current_year, self.current_month)


#     # def delete_appointment(self, appt_id):
#     #     conn = sqlite3.connect(DB_FILE)
#     #     cursor = conn.cursor()
#     #     cursor.execute("DELETE FROM appointments WHERE id = ?", (appt_id,))
#     #     conn.commit()
#     #     conn.close()


#     def on_day_click(self, row, col):
#         btn = self.day_buttons[row - 1][col]
#         day_text = btn.cget("text")
#         if not day_text:
#             return
#         day = int(day_text)
#         date_str = f"{self.current_year}-{self.current_month:02d}-{day:02d}"
#         self.open_day_dialog(date_str)


#     def on_dropdown_go(self):
#         y = self.year_var.get()
#         m = self.month_var.get()
#         d = self.day_var.get()

#         # Validate month/day combination
#         try:
#             _, num_days = calendar.monthrange(y, m)
#         except calendar.IllegalMonthError:
#             messagebox.showerror("Invalid Month", f"{m} is not a valid month.")
#             return

#         if d < 1 or d > num_days:
#             messagebox.showerror("Invalid Date", f"{y}-{m:02d}-{d:02d} is not a valid date.")
#             return

#         self.current_year = y
#         self.current_month = m
#         self.populate_calendar(y, m)

#         date_str = f"{y}-{m:02d}-{d:02d}"
#         self.open_day_dialog(date_str)


#     def open_day_dialog(self, date_str):
#         appts = self.fetch_appointments(date_str)

#         dialog = tk.Toplevel(self.master)
#         dialog.title(f"Appointments: {date_str}")
#         dialog.geometry("420x320")
#         dialog.resizable(False, False)

#         listbox = tk.Listbox(dialog, width=55, height=12, font=("Arial", 10))
#         listbox.pack(pady=10)
#         for appt in appts:
#             appt_id, appt_time, appt_desc = appt
#             listbox.insert(tk.END, f"{appt_time}  |  {appt_desc}  (ID:{appt_id})")

#         btn_frame = tk.Frame(dialog)
#         btn_frame.pack(pady=5)

#         def refresh_list():
#             listbox.delete(0, tk.END)
#             updated = self.fetch_appointments(date_str)
#             for appt in updated:
#                 appt_id, appt_time, appt_desc = appt
#                 listbox.insert(tk.END, f"{appt_time}  |  {appt_desc}  (ID:{appt_id})")

#         def on_add():
#             self.add_appointment(date_str)
#             refresh_list()

#         def on_delete():
#             sel = listbox.curselection()
#             if not sel:
#                 messagebox.showwarning("No Selection", "Please select an appointment to delete.", parent=dialog)
#                 return
#             index = sel[0]
#             appt_line = listbox.get(index)
#             try:
#                 appt_id = int(appt_line.split("(ID:")[1].rstrip(")"))
#             except (IndexError, ValueError):
#                 messagebox.showerror("Error", "Could not parse appointment ID.", parent=dialog)
#                 return

#             confirm = messagebox.askyesno("Confirm Delete", "Delete selected appointment?", parent=dialog)
#             if confirm:
#                 self.delete_appointment(appt_id)
#                 refresh_list()
#                 self.populate_calendar(self.current_year, self.current_month)

#         add_btn = tk.Button(
#             btn_frame, text="Add", font=("Arial", 10, "bold"),
#             command=on_add, bg="#28a745", fg="white", bd=0, padx=10, pady=5
#         )
#         add_btn.grid(row=0, column=0, padx=5)

#         delete_btn = tk.Button(
#             btn_frame, text="Delete", font=("Arial", 10, "bold"),
#             command=on_delete, bg="#dc3545", fg="white", bd=0, padx=10, pady=5
#         )
#         delete_btn.grid(row=0, column=1, padx=5)

#         close_btn = tk.Button(
#             btn_frame, text="Close", font=("Arial", 10, "bold"),
#             command=dialog.destroy, bg="#6c757d", fg="white", bd=0, padx=10, pady=5
#         )
#         close_btn.grid(row=0, column=2, padx=5)


#     def go_prev_month(self):
#         if self.current_month == 1:
#             self.current_month = 12
#             self.current_year -= 1
#         else:
#             self.current_month -= 1
#         self.populate_calendar(self.current_year, self.current_month)


#     def go_next_month(self):
#         if self.current_month == 12:
#             self.current_month = 1
#             self.current_year += 1
#         else:
#             self.current_month += 1
#         self.populate_calendar(self.current_year, self.current_month)


#     def populate_calendar(self, year, month):
#         month_name = calendar.month_name[month]
#         self.month_label.config(text=f"{month_name} {year}")

#         first_weekday, num_days = calendar.monthrange(year, month)

#         # Clear all buttons
#         for r in range(6):
#             for c in range(7):
#                 btn = self.day_buttons[r][c]
#                 btn.config(text="", bg="SystemButtonFace", fg="black", state=tk.NORMAL, relief="raised")

#         # Highlight days with appointments
#         conn = sqlite3.connect(DB_FILE)
#         cursor = conn.cursor()
#         pattern = f"{year}-{month:02d}-%"
#         cursor.execute(
#             "SELECT SUBSTR(date, 9, 2) AS day, COUNT(*) FROM appointments WHERE date LIKE ? GROUP BY day",
#             (pattern,)
#         )
#         rows = cursor.fetchall()
#         conn.close()
#         days_with_appts = {int(day): count for day, count in rows}

#         today = datetime.today()
#         is_current_month = (year == today.year and month == today.month)

#         day_num = 1
#         row = 0
#         col = first_weekday

#         while day_num <= num_days:
#             btn = self.day_buttons[row][col]
#             btn.config(text=str(day_num))

#             # Highlight today’s date with a border
#             if is_current_month and day_num == today.day:
#                 btn.config(relief="solid", bd=2)

#             # Highlight appointment days
#             if day_num in days_with_appts:
#                 btn.config(bg="#a0c4ff", fg="black")
#             else:
#                 btn.config(bg="SystemButtonFace", fg="black")

#             day_num += 1
#             col += 1
#             if col > 6:
#                 col = 0
#                 row += 1

#         # Disable leftover empty buttons
#         while row < 6:
#             while col < 7:
#                 btn = self.day_buttons[row][col]
#                 if not btn.cget("text"):
#                     btn.config(state=tk.DISABLED)
#                 col += 1
#             row += 1
#             col = 0


# if __name__ == "__main__":
#     root = tk.Tk()
#     app = CalendarApp(root)
#     root.mainloop()
