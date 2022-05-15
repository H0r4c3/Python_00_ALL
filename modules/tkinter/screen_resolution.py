
import tkinter as tk
import ctypes
ctypes.windll.shcore.SetProcessDpiAwareness(2) # your windows version should >= 8.1,it will raise exception.

root = tk.Tk()

width = root.winfo_screenwidth()
height = root.winfo_screenheight()
print(f'Screen dimensions: {width} x {height}')

root.mainloop()