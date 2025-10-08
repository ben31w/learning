# https://www.pythontutorial.net/tkinter/tkinter-thread/
import tkinter as tk
from tkinter import ttk
import time
from threading import Thread
import random

class GetRandomNumber(Thread):
    def __init__(self):
        super().__init__()
        self.result = None

    def run(self):
        """Wait three seconds, then generate + return a random number."""
        for i in range(3):
            print(f"Thread running... {i+1}/3")
            time.sleep(1)

        r = random.randint(1, 100)
        print(f"Thread done. Result: {r}")
        self.result = r

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("400x130")
        self.title("Tkinter Thread Example")

        # Create a label to display the result
        self.result_var = tk.StringVar()
        self.label = ttk.Label(
            self,
            text="Result will appear here",
            font=("TkDefaultFont", 24),
            textvariable=self.result_var
        )
        self.label.pack(padx=10 ,pady=10)

        # Create a button to start the thread
        self.button = ttk.Button(
            self,
            text="Get a Random Number",
            command=self.handle_click
        )
        self.button.pack(padx=10 ,pady=10)

    def handle_click(self):
        thread = GetRandomNumber()
        thread.start()
        self.monitor(thread)

    def monitor(self, thread):
        if thread.is_alive():
            self.after(100, lambda: self.monitor(thread))
        else:
            self.result_var.set(thread.result)

if __name__ == "__main__":
    app = App()
    app.mainloop()