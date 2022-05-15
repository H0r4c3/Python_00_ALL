# In this example, four labels are positioned in a grid of rows and columns

from tkinter import *
root = Tk()

Label(text="Position 1", width=10).grid(row=0, column=1)
Label(text="Position 2", width=10).grid(row=0, column=1)
Label(text="Position 3", width=10).grid(row=1, column=0)
Label(text="Position 4", width=10).grid(row=1, column=1)
root.mainloop()
