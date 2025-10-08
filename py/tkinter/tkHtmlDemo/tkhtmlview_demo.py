import tkinter as tk
from zlib import adler32

from tkhtmlview import HTMLLabel

from html_string import html_string


print(len(html_string))
print(html_string.__hash__())
print(adler32(html_string.encode('utf-8')))

# root = tk.Tk()
# label = HTMLLabel(root, html=html_string)
# label.pack(fill="both", expand=True)
#
# root.mainloop()
