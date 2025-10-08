import datetime
from tkinter import *
from tkinter import ttk

import matplotlib.dates as mdates
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np


class ExerciseSet:
    """A set of an exercise."""
    def __init__(self, exercise: str, reps: int, weight: float, partial_reps: bool, date: datetime.date):
        self.exercise = exercise
        self.reps = reps
        self.weight = weight
        self.partial_reps = partial_reps
        self.date = date

root = Tk()

fig = Figure()
ax = fig.add_subplot(111)

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

# x = [1, 1, 2]
# y = [1, 2, 3]

#find line of best fit
# a, b = np.polyfit(x, y, 1)

# Text in the x-axis will be displayed in 'dd Month yy' format.
ax.xaxis.set_major_formatter(mdates.DateFormatter('%d %b %y'))
ax.xaxis.set_major_locator(mdates.DayLocator(interval=1))
# Rotates and right-aligns the x labels so they don't crowd each other.
for label in ax.get_xticklabels(which='major'):
    label.set(rotation=30, horizontalalignment='right')


ax.plot(x, y, marker='o')
# ax.scatter(x, y, marker = 'o')
# ax.plot(x, int(a)*x+b)

canvas = FigureCanvasTkAgg(fig, root)
canvas.draw()  # I guess this renders the figure? Idk if it's needed
canvas.get_tk_widget().pack()

root.mainloop()