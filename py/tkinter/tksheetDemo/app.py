from tksheet import Sheet
import tkinter as tk


def on_cell_select(event):
    # cell_value = self.sheet.get_cell_data(event.row, event.column)
    # print(cell_value)
    content = event["selected"]
    cell_value = app.sheet.get_cell_data(content.row, content.column)
    cell_note = app.sheet.props(content.row, content.column, "note")
    print(f"{cell_value} ({content.row}, {content.column})")
    if cell_note:
        print(f"  NOTE: {cell_note}")
    # if cell_value == "Delete":
    if content.column == 3:
        print("  Are you sure you want to delete?")


class demo(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.grid_columnconfigure(0, weight = 1)
        self.grid_rowconfigure(0, weight = 1)
        self.frame = tk.Frame(self)
        self.frame.grid_columnconfigure(0, weight = 1)
        self.frame.grid_rowconfigure(0, weight = 1)
        self.minsize(800, 400)

        sheet_data = []
        for r in range(10):
            sheet_data.append(["HTML", "Today", "users/ben/myawesomefilepath.txt", "Delete"])

        self.sheet = Sheet(self.frame,
                           data=sheet_data,
                           headers = ["Method", "Date Time", "File", "Delete"],
                           note_corners=True
        )
                           # data = [[f"Row {r}, Column {c}\nnewline1\nnewline2" for c in range(50)] for r in range(500)])

        # Override default bindings
        # Note: exclude "edit_cell" to prevent editing
        self.sheet.enable_bindings(
            ("single_select",  # allows cell selection
            "row_select",  # allows row selection
            "column_select",  # allows column selection
            "arrowkeys",  # navigation
            "right_click_popup_menu",
            "rc_select",
            "copy",
            "select_all",
            "drag_select",
             "column_width_resize",
             "double_click_column_resize")
        )

        # Extra bindings enables a function call when you select a cell
        self.sheet.extra_bindings("cell_select", on_cell_select)

        # Add note to cell
        self.sheet.note(0,  0, note="This is cell A1, the first cell.")

        # Resize cells
        self.sheet.set_all_cell_sizes_to_text()

        # Color a certain column
        self.sheet.highlight_cells(row="all",
                              column=3,
                              bg="red",  # background color
                              fg="white",  # text color
                              overwrite=True)  # overwrite previous styling

        self.frame.grid(row = 0, column = 0, sticky = "nswe")
        self.sheet.grid(row = 0, column = 0, sticky = "nswe")


app = demo()
app.mainloop()