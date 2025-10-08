"""
Entry point to the application, used if you are running with the python(3)
command.
"""

try:
    import tkinter as tk
    from tkinter import ttk
except ImportError:
    import Tkinter as tk
    import ttk

from src.date_tab import DateTab

WINDOW_HEIGHT = 100
WINDOW_WIDTH = 900


class MainWindow(tk.Tk):
    def __init__(self, *args, **kwargs):
        # Init window
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("Lift Log")
        self.geometry(f'{WINDOW_WIDTH}x{WINDOW_HEIGHT}')
        self.minsize(WINDOW_WIDTH, WINDOW_HEIGHT)

        notebook = ttk.Notebook(self)
        notebook.pack(fill='both', expand=True)

        tab = DateTab(notebook)
        notebook.add(tab, text="Date")

def main():
    win = MainWindow()
    win.mainloop()

if __name__ == '__main__':
    main()