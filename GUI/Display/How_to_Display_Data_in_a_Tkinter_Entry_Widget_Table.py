from tkinter import *

rows = []

for i in range(5):

    cols = []

    for j in range(4):

        e = Entry(relief=GROOVE)

        e.grid(row=i, column=j, sticky=NSEW)

        e.insert(END, '%d.%d' % (i, j))

        cols.append(e)

    rows.append(cols)

mainloop()
