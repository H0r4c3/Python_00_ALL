import tkinter as tk
from tkinter import ttk
import tksheet


class CreateSheet():

    def __init__(self, parent):
        self.parent = parent

    def create_a_sheet(self):
        from create_window_for_selecting_paths import CreateMenusFieldsButtons
        from check_values_in_two_files import FileWork

        self.sheet = tksheet.Sheet(self.parent.window, width=1500, height=750)
        self.sheet.pack(padx=5, pady=5, side=tk.TOP, fill=tk.BOTH, expand=1)

        self.headers = ("Variables","HMF File")
        self.sheet.headers(self.headers)

        self.sheet.column_width(column=0, width=500, only_set_if_too_small=True, redraw=True)
        self.sheet.column_width(column=1, width=250, only_set_if_too_small=True, redraw=True)
        
        
        self.sheet.set_column_data(0, values=self.parent.list_of_variables)
        self.sheet.set_column_data(1, values=self.parent.list_of_values)
        

        # table enable choices listed below:
        self.sheet.enable_bindings(("single_select", "row_select", "column_width_resize", "arrowkeys", "right_click_popup_menu", "rc_select", "rc_insert_row", "rc_delete_row",
                        "copy", "cut", "paste", "delete", "undo", "edit_cell"))

        #self.sheet.extra_bindings([("cell_select", self.open_browser)])

        self.sheet.change_theme("light blue")
