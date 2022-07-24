'https://pythonguides.com/python-tkinter-text-box/'

from tkinter import *

ws = Tk()
ws.title('PythonGuides')
ws.geometry('400x300')
ws.config(bg='#A67449')

message ='''
Dear Reader,

    Don't let this situation
    blind your future. We at
    PythonGuides write tutorials
    with real life examples to 
    make you understand the concept
    in best possible way.

Thanks & Regards,
Team PythonGuides '''

text_box = Text(
    ws,
    height=13,
    width=40
)
text_box.pack(expand=True)
text_box.insert('end', message)

ws.mainloop()