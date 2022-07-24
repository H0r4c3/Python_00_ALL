

import tkinter as tk
from typing_extensions import IntVar

def method_for_button():
    if i1.get():
        print('Python')
    else:
        print('Unchecked1')
        
    if i2.get():
        print('C++')
    else:
        print('Unchecked2')
        
 
root = tk.Tk()
root.title('Checkbutton')
root.geometry('250x40+600+400')

i1 = tk.IntVar()
i2 = tk.IntVar()

frame1 = tk.Frame(root, relief=tk.RIDGE)
frame1.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5) 

c1 = tk.Checkbutton(frame1, text = "Python", variable=i1)
c1.pack(padx=1, pady=5, side=tk.LEFT)
 
c2 = tk.Checkbutton(frame1, text = "C++", variable=i2)
c2.pack(padx=1, pady=5, side=tk.LEFT)

b = tk.Button(frame1, text="Click here", command = method_for_button)
b.pack(padx=1, pady=5, side=tk.RIGHT)
 

root.mainloop()