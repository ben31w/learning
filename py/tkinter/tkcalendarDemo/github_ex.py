# https://github.com/j4321/tkcalendar/issues/110

from tkinter import BOTH, X, ttk
from typing import Optional, Tuple, Union
import customtkinter as ctk
import tkinter as tk
from tkinter import END
from tkcalendar import DateEntry
import threading


class AppLabel(ctk.CTkLabel):
    def __init__(self, parent, text, size, color='black'):
        if size == 'titre':
            font = ('Arial Black', 22, 'bold')
        elif size == 'categorie':
            font = ('Arial', 20, 'underline')
        elif size == 'attribut':
            font = ('Arial', 20)
        elif size == 'formulaire18':
            font = ('Arial', 18)
        elif size == 'formulaire15':
            font = ('Arial', 15)
        else:
            font = ('Arial', 14)  # Taille par défaut si aucune correspondance n'est trouvée

        super().__init__(parent, text=text, font=font, text_color=color)


class LabeledDatePicker(ctk.CTkFrame):
    def __init__(self, parent, text_label, size, width_entry=250, color='black', out_focus_bind_command=None):
        super().__init__(parent)
        self.master = parent
        self.out_focus_bind_command = out_focus_bind_command
        self.entry = DateEntry(self, font=('Arial', 18), position='topright', calendar=False)
        self.entry.configure(date_pattern='dd/MM/y')
        if self.out_focus_bind_command:
            self.entry.bind("<FocusOut>", self.out_focus_bind_command)
        self.entry.grid(row=0, column=1, padx=5, pady=5, sticky='e')
        self.grid_columnconfigure(0, weight=1)

    def get_value(self):
        return self.entry.get_date()

    def update(self, value):
        self.entry.set_date(value)


class ProjectWindowShow(ctk.CTkToplevel):
    def __init__(self, parent: ctk.CTk, code_projet: str, *args, fg_color: str | Tuple[str, str] | None = None,
                 **kwargs):
        super().__init__(parent)
        self.grab_set()
        self.parent = parent
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.chargement_frame = ctk.CTkFrame(self)
        self.chargement_frame.pack(fill=BOTH, expand=True)
        self.chargement_label = ctk.CTkLabel(self.chargement_frame, text='Chargement...')
        self.chargement_label.pack(fill=BOTH, expand=True)
        self.main_frame = ctk.CTkFrame(self, fg_color='transparent')
        self.main_frame.columnconfigure(0, weight=1)
        self.main_frame.rowconfigure(1, weight=1)
        threading.Thread(target=self.show_datas).start()

    def show_datas(self):
        self.cstartdate = LabeledDatePicker(self.main_frame, text_label='début', size='attribut')
        self.cstartdate.grid()
        self.chargement_frame.destroy()
        self.main_frame.pack(fill=BOTH, expand=True)


class MainWindow(ctk.CTk):
    def __init__(self, fg_color: str | Tuple[str, str] | None = None, **kwargs):
        super().__init__(fg_color, **kwargs)
        self.btn = ctk.CTkButton(self, text='nouveau projet', command=self.open_project)
        self.btn.pack()

    def open_project(self):
        id = None
        self.pwindow = ProjectWindowShow(self, code_projet=id)


window = MainWindow()
window.mainloop()