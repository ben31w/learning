"""
More advanced logging example.
Integrates with a Tkinter GUI and writes to a log file.
"""
import tkinter as tk
from tkinter import messagebox
import logging
import logging.config

# Logging setup
LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'simple': {'format': '[%(asctime)s] %(levelname)s: %(message)s'}
    },
    'handlers': {
        'console': {'class': 'logging.StreamHandler', 'formatter': 'simple'},
        'file': {'class': 'logging.FileHandler', 'filename': 'app.log', 'formatter': 'simple'},
    },
    'root': {
        'handlers': ['console', 'file'],
        'level': 'INFO',
    },
}
logging.config.dictConfig(LOGGING_CONFIG)
logger = logging.getLogger(__name__)

# Tkinter app
def risky_operation():
    try:
        raise ValueError("This is a simulated error.")
    except Exception as e:
        logger.exception("Something went wrong in risky_operation")
        messagebox.showerror("Error", str(e))

def main():
    root = tk.Tk()
    root.title("Logging Demo")

    tk.Button(root, text="Do something risky", command=risky_operation).pack(pady=20)

    logger.info("App started")
    root.mainloop()
    logger.info("App closed")

if __name__ == "__main__":
    main()
