import tkinter as tk
from cupcake import Editor, Languages

root = tk.Tk()
root.minsize(800, 600)

e = Editor(root, language=Languages.TYPESCRIPT)
e.pack(expand=1, fill=tk.BOTH)

e.content.insert("end", """
// check this out
import "./global.css";
import App from './App.svelte';

const app = new App({
	target: document.body
});

export default app;
""")

root.mainloop()