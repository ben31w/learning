# https://blog.finxter.com/5-best-ways-to-place-a-plot-on-tkinter-main-window-in-python/

import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

root = tk.Tk()

fig = Figure(figsize=(5, 4), dpi=100)
t = [0, 1, 2, 3, 4]
s = [1, 3, 2, 3, 5]

fig.add_subplot(111).plot(t, s)
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

root.mainloop()