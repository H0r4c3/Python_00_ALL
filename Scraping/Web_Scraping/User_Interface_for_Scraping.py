

import tkinter as tk
from tkinter import ttk


def label_field_creator():
    name_label = ttk.Label(root, text="Website: ")
    name_label.pack(side="left", padx=(0, 10)) # padx -> the left side of the label and the right side of the label, distance, in pixels, from the left margin of the frame

    name_entry = ttk.Entry(root, width=15, textvariable=user_name) # input field
    name_entry.pack(side="left")
    name_entry.focus() # to have the focus inside the input field

def greet():
    # The get() method is used to fetch the value of a StringVar() instance.
    # If user_name is empty, print Hello, World!
    print(f"Hello, {user_name.get() or 'World'}!") # get is used to retrieve the value of "user_name"


root = tk.Tk()
root.title("Scraper")

# Here we create an instances of the StringVar() class, which is to track the content of widgets (Entry)
user_name = tk.StringVar() # the string entered in the input field

'''
name_label = ttk.Label(root, text="Website: ")
name_label.pack(side="left", padx=(0, 10)) # padx -> the left side of the label and the right side of the label, distance, in pixels, from the left margin of the frame

name_entry = ttk.Entry(root, width=15, textvariable=user_name) # input field
name_entry.pack(side="left")
name_entry.focus() # to have the focus inside the input field
'''

'''
greet_button = ttk.Button(root, text="Scrap", command=greet)
greet_button.pack(side="bottom", expand=False)
'''

label_field_creator()

root.mainloop()
