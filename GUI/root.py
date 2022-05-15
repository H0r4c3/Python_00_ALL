'https://www.udemy.com/course/the-art-of-doing-master-the-basics-of-python-guis/learn/lecture/21373774#overview'

import tkinter as tk

root = tk.Tk()
root.title("root")
root.iconbitmap(r'C:\Users\Horace.000\eclipse-workspace\Python_Project_6_Online_Courses\00_ALL\GUI\black-cat-eyes.ico')

# dimensions of the window
root.geometry('500x500+500+200')

# for resizable=yes, put 1 for (width, height)
root.resizable(0,0)

# color of the background
root.config(background='blue')

# second window
top = tk.Toplevel()
top.title("Second Window")
top.geometry('400x200+1000+400')
top.config(bg="#123456")


root.mainloop()