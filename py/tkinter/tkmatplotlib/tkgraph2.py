# I feel like this is the same as number 1

import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

root = tk.Tk()

fig = Figure()
ax = fig.add_subplot(111)

x = [0, 1, 2, 3, 4]
y = [10, 20, 10, 20, 30]
ax.plot(x, y)

canvas = FigureCanvasTkAgg(fig, root)
canvas_widget = canvas.get_tk_widget()
canvas_widget.pack()

root.mainloop()