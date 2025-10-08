import datetime
from tkinter import *
from tkinter import ttk

import matplotlib.dates as mdates
import mplcursors
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure


class ExerciseSet:
    """A set of an exercise."""
    def __init__(self, exercise: str, reps: int, weight: float, partial_reps: bool, date: datetime.date):
        self.exercise = exercise
        self.reps = reps
        self.weight = weight
        self.partial_reps = partial_reps
        self.date = date



exercise_sets = [
    ExerciseSet(exercise='bb bench', reps=6, weight=135, partial_reps=False, date=datetime.date(2021, 6, 2)),
    ExerciseSet(exercise='bb bench', reps=6, weight=135, partial_reps=False, date=datetime.date(2021, 6, 2)),
    ExerciseSet(exercise='bb bench', reps=5, weight=135, partial_reps=False, date=datetime.date(2021, 6, 2)),
    ExerciseSet(exercise='bb bench', reps=5, weight=135, partial_reps=False, date=datetime.date(2021, 6, 2)),
    ExerciseSet(exercise='bb bench', reps=5, weight=135, partial_reps=False, date=datetime.date(2021, 6, 6)),
    ExerciseSet(exercise='bb bench', reps=5, weight=135, partial_reps=False, date=datetime.date(2021, 6, 6)),
    ExerciseSet(exercise='bb bench', reps=5, weight=135, partial_reps=False, date=datetime.date(2021, 6, 6)),
    ExerciseSet(exercise='bb bench', reps=5, weight=135, partial_reps=False, date=datetime.date(2021, 6, 6)),
    ExerciseSet(exercise='bb bench', reps=5, weight=135, partial_reps=False, date=datetime.date(2021, 6, 6))
]

x = [s.date for s in exercise_sets]
y = [s.reps * s.weight for s in exercise_sets]


root = Tk()
frm = ttk.Frame(root)
frm.grid(row=0, column=0)

fig = Figure()
ax = fig.add_subplot(111)

# Text in the x-axis will be displayed in 'dd Month yy' format.
ax.xaxis.set_major_formatter(mdates.DateFormatter('%d %b %y'))
ax.xaxis.set_major_locator(mdates.DayLocator(interval=1))
# Rotates and right-aligns the x labels so they don't crowd each other.
for label in ax.get_xticklabels(which='major'):
    label.set(rotation=30, horizontalalignment='right')

points = ax.scatter(x, y)
ax.set_title("Click somewhere on a line.\nRight-click to deselect.\n"
             "Annotations can be dragged.")

mplcursors.cursor(points)  # or just mplcursors.cursor()

canvas = FigureCanvasTkAgg(fig, frm)
canvas.draw()
canvas.get_tk_widget().pack()

root.mainloop()