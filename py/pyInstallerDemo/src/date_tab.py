"""
A class for the GUI date tab. This is in a separate class to demonstrate
PyInstaller's ability to combine files into one executable.
"""
try:
    import tkinter as tk
    from tkinter import ttk
except ImportError:
    import Tkinter as tk
    import ttk

from tkcalendar import DateEntry


class DateTab(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)

        # Container row 0
        row0 = ttk.Frame(self)
        row0.grid(row=0, column=0, sticky=tk.W)
        lbl_exercise = ttk.Label(row0, text="Exercise")
        lbl_exercise.grid(row=0, column=0)
        self.combobox = ttk.Combobox(row0, width=40)
        self.combobox.grid(row=0, column=1)
        self.esd = {}  # ESD = Exercises-Sets Dictionary. Maps 'exercise' -> [ExerciseSet]

        # Create labels and date entries for the start and end date, but DON'T
        # add them to the GUI yet. Wait for the first exercise to be selected.
        # self.dates_visible = False
        self.lbl_start_date = ttk.Label(row0, text="Start Date")
        self.lbl_start_date.grid(row=0, column=2)
        self.date_entry_start = DateEntry(row0, width=12, background='darkblue',
                                          foreground='white', borderwidth=2)

        self.date_entry_start.grid(row=0, column=3)