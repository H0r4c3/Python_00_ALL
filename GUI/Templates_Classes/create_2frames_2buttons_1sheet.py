import tkinter as tk
from tkinter import ttk
import tksheet


window = tk.Tk()
window.title("Window")

def method_for_button_OK():
    print("OK")

    frame2 = tk.Frame(window, relief=tk.RIDGE)
    frame2.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)

    # creating a Sheet
    sheet = tksheet.Sheet(frame2, width=1500, height=750)
    sheet.pack(padx=5, pady=5, side=tk.TOP, fill=tk.BOTH, expand=1)

    headers = ("Name","Year","Genre")
    sheet.headers(headers)

    sheet.column_width(column=0, width=750, only_set_if_too_small=True, redraw=True)
    sheet.column_width(column=1, width=350, only_set_if_too_small=True, redraw=True)

    # populate the Sheet
    sheet.set_column_data(0, values="111")
    sheet.set_column_data(1, values="222")
    sheet.set_column_data(2, values="333")

    sheet.change_theme("light blue")


# creating 2 frames: 1 for the buttons, 1 for the Sheet
frame1 = tk.Frame(window, relief=tk.RIDGE)
frame1.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)

frame2 = tk.Frame(window, relief=tk.RIDGE)
frame2.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)

# Create some room around all the internal frames
window['padx'] = 5
window['pady'] = 5

# creating a button that will call the "method_for_button_OK" method
ok_button=ttk.Button(frame1, text = 'OK', command = method_for_button_OK) 
    
# creating a button that will call the "quit" function  
quit_button=ttk.Button(frame1, text = 'Quit', command = window.destroy)

ok_button.pack(padx=5, pady=5, side=tk.LEFT)
quit_button.pack(padx=5, pady=5, side=tk.LEFT)



window.mainloop()





