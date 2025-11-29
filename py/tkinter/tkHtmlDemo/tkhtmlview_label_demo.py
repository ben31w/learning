# import tkinter as tk
# from zlib import adler32
#
# from tkhtmlview import HTMLLabel
#
# from html_string import html_string
#
#
# print(len(html_string))
# print(html_string.__hash__())
# print(adler32(html_string.encode('utf-8')))
#
# root = tk.Tk()
# label = HTMLLabel(root, html=html_string)
# label.pack(fill="both", expand=True)
#
# root.mainloop()


import tkinter as tk
from tkhtmlview import HTMLLabel

root = tk.Tk()
html_label = HTMLLabel(root, html='<h1 style="color: red; text-align: center"> Hello World </H1>')
html_label.pack(fill="both", expand=True)
html_label.fit_height()
root.mainloop()