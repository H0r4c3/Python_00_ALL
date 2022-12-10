import tkinter as tk
import os
from tkinter import filedialog

def method_for_button():
    print('Button pressed!')
    path = r'c:\test_file.txt'
    try:
        os.startfile(path)
    except FileNotFoundError as f:
        print(f)
        print('No file found! Select the correct path for the file!')
        
    
    
    
# Let's create the Tkinter window.
window = tk.Tk()
window.title("GUI")
window.geometry('1200x110+400+400')

# You will first create a division with the help of Frame class and align them on TOP and BOTTOM with pack() method.
top_frame = tk.Frame(window).pack()

# Create button
button1 = tk.Button(top_frame, text = "Open File", fg = "red", command = method_for_button).pack() #'fg or foreground' is for coloring the contents (buttons)

window.mainloop()