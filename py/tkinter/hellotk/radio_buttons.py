import tkinter as tk
from tkinter import ttk



class FriendFrame(tk.Tk):
    def __init__(self):
        super().__init__()
        frm = ttk.Frame(self)
        frm.grid(row=0, column=0)

        self.selected_friend = tk.StringVar()

        rb_richard = ttk.Radiobutton(frm, text="Richard", value="Richard", variable=self.selected_friend)
        rb_matt = ttk.Radiobutton(frm, text="Matt", value="Matt", variable=self.selected_friend)
        rb_dat = ttk.Radiobutton(frm, text="Dat", value="Dat", variable=self.selected_friend)

        lbl_friend = ttk.Label(frm, textvariable=self.selected_friend)

        rb_richard.grid(row=0, column=0)
        rb_matt.grid(row=0, column=1)
        rb_dat.grid(row=0, column=2)
        lbl_friend.grid(row=1, column=1)

if __name__ == '__main__':
    ff = FriendFrame()
    ff.mainloop()