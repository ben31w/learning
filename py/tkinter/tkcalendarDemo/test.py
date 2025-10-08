# import tkinter as tk
#
# root = tk.Tk()
#
# # one row container that stretches horizontally
# row_frame = tk.Frame(root)
# row_frame.pack(fill='x', padx=10, pady=10)
#
# # left sub‑frame: pack to the left
# left_frame = tk.Frame(row_frame)
# left_frame.pack(side='left')
#
# # right sub‑frame: pack to the right
# right_frame = tk.Frame(row_frame)
# right_frame.pack(side='right')
#
# # add some widgets into the left frame
# for txt in ("Left 1", "Left 2", "Left 3"):
#     btn = tk.Button(left_frame, text=txt)
#     btn.pack(side='left', padx=2)
#
# # add some widgets into the right frame
# for txt in ("Right A", "Right B"):
#     btn = tk.Button(right_frame, text=txt)
#     btn.pack(side='right', padx=2)
#
# root.mainloop()


import tkinter as tk

root = tk.Tk()

# configure column “1” to expand and push columns 0 and 2 to the edges
root.columnconfigure(1, weight=1)

# left group goes in column 0, sticky West
btn_L1 = tk.Button(root, text="Left 1")
btn_L2 = tk.Button(root, text="Left 2")
btn_L1.grid(row=0, column=0, sticky='w', padx=(10, 2))
btn_L2.grid(row=0, column=0, sticky='w', padx=(70, 2))  # adjust offset as needed

# (column 1 is empty – it just expands)

# right group goes in column 2, sticky East
btn_R1 = tk.Button(root, text="Right A")
btn_R2 = tk.Button(root, text="Right B")
btn_R1.grid(row=0, column=2, sticky='e', padx=(2, 70))
btn_R2.grid(row=0, column=2, sticky='e', padx=(2, 10))

root.mainloop()

