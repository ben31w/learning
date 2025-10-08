from tkinter import END, Event, INSERT, Menu, SEL, TclError, Text, Tk


class TextEditorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tkinter Text Editor")

        # Create Text widget with undo/redo
        self.edit_area = Text(root, undo=True, wrap="word")
        self.edit_area.pack(expand=True, fill="both")

        # Add a menu bar
        self.menu = Menu(root)
        root.config(menu=self.menu)

        self.edit_menu = Menu(self.menu, tearoff=0)
        self.edit_menu.add_command(label="Undo", command=self.undo, accelerator="Ctrl+Z")
        self.edit_menu.add_command(label="Redo", command=self.redo, accelerator="Ctrl+Y")
        self.menu.add_cascade(label="Edit", menu=self.edit_menu)

        # Add some text
        self.edit_area.insert(INSERT, "Select some text then right click in this window")

        # Key bindings
        # Three ways to assign bindings:
        #   1. bind to a class (like Text)
        #   2. bind to the top-level Tk (applies to all widgets)
        #   3. bind to widget
        # root.bind_all("<Control-z>", self.undo)
        # root.bind_all("<Control-Shift-z>", self.redo)
        # Prevent default Ctrl+Y paste
        self.edit_area.bind_class("Text", "<Control-y>", lambda e: "break")
        self.edit_area.bind("<Control-z>", self.undo)
        # The Control-Shift-z binding doesn't appear to actually call self.redo,
        # yet it still does a redo... weird
        self.edit_area.bind("<Control-Shift-z>", self.redo)
        self.edit_area.bind("<Control-a>", self.select_all)
        self.edit_area.bind("<Control-A>", self.select_all)  # just in case caps lock is on

    def undo(self, event=None):
        print("UNDO CALL")
        try:
            self.edit_area.edit_undo()
            return 'break'
        except TclError:
            pass

    def redo(self, event=None):
        print("REDO CALL")
        try:
            self.edit_area.edit_redo()
            return 'break'
        except TclError:
            pass

    # Select all the text in self.edit_area
    def select_all(self, event):
        print("SELECT ALL CALL")
        self.edit_area.tag_add(SEL, "1.0", END)
        self.edit_area.mark_set(INSERT, "1.0")
        self.edit_area.see(INSERT)
        return 'break'

if __name__ == "__main__":
    root = Tk()
    app = TextEditorApp(root)
    root.mainloop()
