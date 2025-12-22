"""
https://github.com/ghassenTn/ChartForgeTK
"""
import math
import tkinter as tk

from ChartForgeTK import LineChart

root = tk.Tk()
root.geometry("800x800")

chart = LineChart(root, width=780, height=520)
chart.pack(fill="both", expand=True)

large_data_points = [math.sin(i / 10) * 100 + (i / 2) for i in range(200)]
print(large_data_points)

# y-values.
datasets_large = [
    {
        'data': large_data_points,
        'color': '#FF5733',
        'label': 'Large Dataset (Sine Wave)'
    }
]
datasets_small = [
    {
        'data': [135, 135, 145, 145],
        'label': 'Weights'
    }
]
# chart.plot(datasets_large)
chart.plot(datasets_small)

root.mainloop()