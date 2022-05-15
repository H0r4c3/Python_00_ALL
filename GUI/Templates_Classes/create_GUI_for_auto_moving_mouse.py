import tkinter as tk
from tkinter import ttk

import pyautogui


window = tk.Tk()
window.title("Window")

def method_for_button_START():
    print("START")

    i = 100

    while i>0:
      pyautogui.moveTo(200, 200, duration=1)
      pyautogui.moveTo(300, 200, duration=1)
      pyautogui.moveTo(300, 300, duration=1)
      pyautogui.moveTo(200, 300, duration=1)


# creating 2 frames: 1 for the buttons, 1 for the Sheet
frame1 = tk.Frame(window, relief=tk.RIDGE)
frame1.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)

frame2 = tk.Frame(window, relief=tk.RIDGE)
frame2.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)

# Create some room around all the internal frames
window['padx'] = 5
window['pady'] = 5

# creating a button that will call the "method_for_button_OK" method
ok_button=ttk.Button(frame1, text = 'START', command = method_for_button_START)
    
# creating a button that will call the "quit" function
quit_button=ttk.Button(frame1, text = 'Quit', command = window.destroy)

ok_button.pack(padx=5, pady=5, side=tk.LEFT)
quit_button.pack(padx=5, pady=5, side=tk.LEFT)



window.mainloop()





