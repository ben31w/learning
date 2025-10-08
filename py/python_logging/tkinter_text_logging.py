"""
Even more advanced logging example.
Integrates with a Tkinter GUI and writes to a log file and a ScrolledText widget
with color.
"""
import logging
import logging.config
import tkinter as tk
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText


class TextHandler(logging.Handler):
    """
    To send logging output to another area (in this case, a Text widget),
    you must define a Handler class that implements emit.
    """
    def __init__(self, text_widget):
        super().__init__()
        self.text_widget = text_widget

        # Define tags for each log level
        self.text_widget.tag_config("DEBUG", foreground="gray")
        self.text_widget.tag_config("INFO", foreground="black")
        self.text_widget.tag_config("WARNING", foreground="orange")
        self.text_widget.tag_config("ERROR", foreground="red")
        self.text_widget.tag_config("CRITICAL", foreground="white", background="red")

    def emit(self, record):
        msg = self.format(record)
        level = record.levelname

        def append():
            self.text_widget.insert(tk.END, msg + "\n", level)
            self.text_widget.see(tk.END)
        self.text_widget.after(0, append)

def debug_operation():
    logger.debug("Debug in debug_operation")

def info_operation():
    logger.info("Info in info_operation")

def warning_operation():
    logger.warning("Warning in warning_operation")

def error_operation():
    try:
        raise RuntimeError("Something failed.")
    except Exception as e:
        logger.exception("Error in error_operation")
        messagebox.showerror("Error", str(e))

def critical_operation():
    try:
        raise RuntimeError("Something failed.")
    except Exception as e:
        logger.critical("Error in critical_operation", exc_info=True)
        messagebox.showerror("Error", str(e))

def setup_logging(log_text_widget):
    handler = TextHandler(log_text_widget)
    handler.setFormatter(logging.Formatter('[%(asctime)s] %(levelname)s: %(message)s'))

    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    logger.addHandler(handler)

    # Optional: also log to file
    file_handler = logging.FileHandler("app.log")
    file_handler.setFormatter(logging.Formatter('[%(asctime)s] %(levelname)s: %(message)s'))
    logger.addHandler(file_handler)

    return logger

# Tkinter GUI app
def main():
    root = tk.Tk()
    root.title("Tkinter Logging Demo")

    frame = tk.Frame(root)
    frame.pack(padx=10, pady=10)

    log_text = ScrolledText(frame, width=80, height=20)
    # log_text = tk.Text(frame, width=80, height=20, wrap='word', state='normal')
    log_text.pack()

    global logger
    logger = setup_logging(log_text)
    logger.info("App started")

    tk.Button(root, text="Debug", command=debug_operation).pack(pady=10)
    tk.Button(root, text="Info", command=info_operation).pack(pady=10)
    tk.Button(root, text="Warning", command=warning_operation).pack(pady=10)
    tk.Button(root, text="Error", command=error_operation).pack(pady=10)
    tk.Button(root, text="Critical", command=critical_operation).pack(pady=10)

    root.mainloop()
    logger.info("App closed")

if __name__ == "__main__":
    main()
