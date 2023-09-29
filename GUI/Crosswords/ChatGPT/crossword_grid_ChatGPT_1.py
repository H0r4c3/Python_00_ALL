'''
ChatGPT

To create a crossword grid in Python using tkinter, you can follow these steps:

Import the tkinter module
Create a main window using the Tk() function
Create a 2D list to represent the grid
Create a for loop to create the grid squares using the Canvas widget
Add the grid squares to the main window using the grid() method
Add labels to the grid squares for the clue numbers using the create_text() method of the Canvas widget
Here's some example code to get you started:
This code creates a 15x15 grid of white squares with black borders, and adds clue numbers to the first row and first column. 
You can customize the size and appearance of the grid squares and clue numbers to fit your needs.
'''

import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Crossword Grid")

# Create the grid
grid = []
for i in range(10):
    row = []
    for j in range(10):
        square = tk.Canvas(root, width=30, height=30, bg='white', highlightthickness=1, highlightbackground='black')
        square.grid(row=i, column=j)
        row.append(square)
    grid.append(row)

# Add clue numbers
for i in range(1, 11):
    grid[0][i-1].create_text(10, 10, text=str(i))
    grid[i-1][0].create_text(10, 10, text=str(i))

grid[1][1].create_text(10, 10, text='A')

# Run the main loop
root.mainloop()
