import logging
import logging.config
from tkinter import *
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
            self.text_widget.insert(END, msg + "\n", level)
            self.text_widget.see(END)
        self.text_widget.after(0, append)


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

class MyTextWindow(Tk):
    def __init__(self):
        super().__init__()
        self.title("Tkinter Logging Demo")

        frame = Frame(self)
        frame.pack(padx=10, pady=10)

        log_text = ScrolledText(frame, width=80, height=20)
        # log_text = Text(frame, width=80, height=20, wrap='word', state='normal')
        log_text.pack()

        self.logger = setup_logging(log_text)
        self.logger.info("App started")

        Button(self, text="Debug",    command=self.debug_operation).pack(pady=10)
        Button(self, text="Info",     command=self.info_operation).pack(pady=10)
        Button(self, text="Warning",  command=self.warning_operation).pack(pady=10)
        Button(self, text="Error",    command=self.error_operation).pack(pady=10)
        Button(self, text="Critical", command=self.critical_operation).pack(pady=10)

        self.protocol("WM_DELETE_WINDOW", self.close)
        # self.mainloop()
        # logger.info("App closed")

    def debug_operation(self):
        self.logger.debug("Debug in debug_operation")

    def info_operation(self):
        self.logger.info("Info in info_operation")

    def warning_operation(self):
        self.logger.warning("Warning in warning_operation")

    def error_operation(self):
        try:
            raise RuntimeError("Something failed.")
        except Exception as e:
            self.logger.exception("Error in error_operation")
            messagebox.showerror("Error", str(e))

    def critical_operation(self):
        try:
            raise RuntimeError("Something failed.")
        except Exception as e:
            self.logger.critical("Error in critical_operation", exc_info=True)
            messagebox.showerror("Error", str(e))

    def close(self):
        self.logger.info("App closed")
        self.destroy()