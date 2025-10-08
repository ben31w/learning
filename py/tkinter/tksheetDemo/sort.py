import tkinter as tk
import tksheet

root = tk.Tk()
sheet = tksheet.Sheet(root,
                      data=[
                          [5, "b"],
                          [1, "a"],
                          [3, "c"]
                      ],
                      headers=["Number", "Letter"])
# sheet.enable_bindings("all")
sheet.readonly_columns(1)
sheet.enable_bindings(("single_select",  # allows cell selection
             "row_select",  # allows row selection
             "column_select",  # allows column selection
             "column_sort",
             "arrowkeys",  # navigation
             "right_click_popup_menu",
             # "rc_select",
             "copy",
             "select_all",
             "drag_select",
             "column_width_resize",
             "double_click_column_resize",
                       "rc_menu",
                       # "sort_cell",
                       # "sort_cells",
                       # "sort_column",
                       # "sort_columns",
                       # "sort_row",
                       "sort_rows",  # THIS IS THE IMPORTANT ONE
                       "find",
                       "replace"
                       ))
sheet.pack(fill="both", expand=True)

root.mainloop()