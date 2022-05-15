'https://www.activestate.com/resources/quick-reads/how-to-position-widgets-in-tkinter/'

import tkinter as tk

root = tk.Tk()

test = tk.Label(root, text="red", bg="red", fg="white")
test.pack(padx=5, pady=15, side=tk.LEFT)
test = tk.Label(root, text="green", bg="green", fg="white")
test.pack(padx=5, pady=20, side=tk.LEFT)
test = tk.Label(root, text="purple", bg="purple", fg="white")
test.pack(padx=5, pady=20, side=tk.LEFT)

root.mainloop()
