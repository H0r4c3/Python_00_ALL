import tkinter as tk
from tkinter import ttk

root = tk.Tk()

menubar = tk.Menu(root)

salutations = tk.Menu(menubar, tearoff=False)
salutations.add_command(label="Say Hello", command=lambda: print("Hello"))
salutations.add_command(label="Say Goodbye", command=lambda: print("Goodbye"))

menubar.add_cascade(label="Salutations", menu=salutations)

root.config(menu=menubar)

root.mainloop()
