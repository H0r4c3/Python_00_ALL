import tkinter as tk
from tkinter import ttk
import tksheet


class CreateSheet():

    def __init__(self, parent):
        self.parent = parent

    def create_a_sheet(self):
        self.sheet = tksheet.Sheet(self.parent.window, width=1500, height=750)
        self.sheet.pack(padx=5, pady=5, side=tk.TOP, fill=tk.BOTH, expand=1)

        self.headers = ("Name","Year","Genre", "Quality", "IMDB Rating", "IMDB Nr. Votes", "Torrent","IMDB")
        self.sheet.headers(self.headers)

        self.sheet.column_width(column=0, width=250, only_set_if_too_small=True, redraw=True)
        self.sheet.column_width(column=1, width=3, only_set_if_too_small=True, redraw=True)
        self.sheet.column_width(column=2, width=300, only_set_if_too_small=True, redraw=True)
        self.sheet.column_width(column=3, width=3, only_set_if_too_small=True, redraw=True)
        self.sheet.column_width(column=4, width=3, only_set_if_too_small=True, redraw=True)
        self.sheet.column_width(column=5, width=3, only_set_if_too_small=True, redraw=True)
        self.sheet.column_width(column=6, width=650, only_set_if_too_small=True, redraw=True)
        self.sheet.column_width(column=7, width=350, only_set_if_too_small=True, redraw=True)
        
        self.sheet.set_column_data(0, values=self.parent.Name)
        self.sheet.set_column_data(1, values=self.parent.Year)
        self.sheet.set_column_data(2, values=self.parent.Genre)
        self.sheet.set_column_data(3, values=self.parent.Quality)
        self.sheet.set_column_data(4, values=self.parent.Imdb_Rating)
        self.sheet.set_column_data(5, values=self.parent.Imdb_Votes)
        self.sheet.set_column_data(6, values=self.parent.Torrent)
        self.sheet.set_column_data(7, values=self.parent.Imdb)

        # table enable choices listed below:
        self.sheet.enable_bindings(("single_select", "row_select", "column_width_resize", "arrowkeys", "right_click_popup_menu", "rc_select", "rc_insert_row", "rc_delete_row",
                        "copy", "cut", "paste", "delete", "undo", "edit_cell"))

        #self.sheet.extra_bindings([("cell_select", self.open_browser)])

        self.sheet.change_theme("light blue")
