"""
Another entry point to the application, utilized by PyInstaller.
This entry point exists in the project top-level, and it imports src.main.

Using this setup, we don't have to dual-import everything inside our src code.
i.e., import src.myfile, import myfile

pyInstallerDemo/
|__src/
| |__main.py
|__run.py

Create the PyInstaller executable with this file!
- one-folder: `pyinstaller run.py`
- one-file:   `pyinstaller --onefile run.py`
"""
from src.main import main

if __name__ == '__main__':
    main()