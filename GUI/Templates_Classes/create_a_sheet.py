import tkinter as tk
from tkinter import ttk
import tksheet


class CreateSheet():

    def __init__(self, parent):
        self.parent = parent

    def create_a_sheet(self, value1, value2, value3):
        self.sheet = tksheet.Sheet(self.parent.window, width=1500, height=750)
        self.sheet.pack(padx=5, pady=5, side=tk.TOP, fill=tk.BOTH, expand=1)

        self.headers = ("Name","Year","Genre","Torrent","IMDB")
        self.sheet.headers(self.headers)

        self.sheet.column_width(column=0, width=750, only_set_if_too_small=True, redraw=True)
        self.sheet.column_width(column=1, width=350, only_set_if_too_small=True, redraw=True)
        
        self.sheet.set_column_data(0, values=self.parent.input1_list)
        self.sheet.set_column_data(1, values=self.parent.input2_list)
        self.sheet.set_column_data(2, values=self.parent.input3_list)

        # table enable choices listed below:
        self.sheet.enable_bindings(("single_select", "row_select", "column_width_resize", "arrowkeys", "right_click_popup_menu", "rc_select", "rc_insert_row", "rc_delete_row",
                        "copy", "cut", "paste", "delete", "undo", "edit_cell"))

        #self.sheet.extra_bindings([("cell_select", self.open_browser)])

        self.sheet.change_theme("light blue")
