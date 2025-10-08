from pymd_editor.pymd_editor_frame import EditorFrame

import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

root = ttk.Window(themename="darkly")
app = EditorFrame(root)
app.pack(fill="both", expand=1)
app.mainloop()