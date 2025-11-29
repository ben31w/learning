"""
https://pypi.org/project/tkhtmlview/
HelloWorld tkhtmlview with HTMLText and RenderHTML (renders HTML file).
"""
import tkinter as tk

from tkhtmlview import HTMLText, RenderHTML

root = tk.Tk()
html_label = HTMLText(root, html=RenderHTML('html/index.html'))
html_label.pack(fill="both", expand=True)
html_label.fit_height()
root.mainloop()