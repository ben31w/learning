"""
Even more advanced logging example.
Integrates with a Tkinter GUI and writes to a log file and a ScrolledText widget
with color.
"""

from multifile_app.my_text_window import MyTextWindow


# Tkinter GUI app
def main():
    window = MyTextWindow()
    window.mainloop()

if __name__ == "__main__":
    main()
