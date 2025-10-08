import tkinter as tk
import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

root = tk.Tk()
fig = Figure()
ax = fig.add_subplot(111)
canvas = FigureCanvasTkAgg(fig, root)
canvas_widget = canvas.get_tk_widget()
canvas_widget.pack()

def update_plot():
    ax.clear()
    x = np.random.rand(10)
    y = np.random.rand(10)
    ax.scatter(x, y)
    canvas.draw_idle()
    root.after(1000, update_plot)  # schedule the next update in 1 sec.

root.after(1000, update_plot)
root.mainloop()