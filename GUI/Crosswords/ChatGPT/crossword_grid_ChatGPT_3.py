import tkinter as tk

# Create the Tkinter window
window = tk.Tk()

# Set the window title
window.title("Crossword")

# Create a 10x10 grid of Entry widgets
entries = []
for i in range(10):
    row = []
    for j in range(10):
        entry = tk.Entry(window, width=3)
        entry.grid(row=i, column=j)
        row.append(entry)
    entries.append(row)

# Add black squares to the grid
black_squares = [(3, 0), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7), (3, 8), (3, 9)]
for square in black_squares:
    entries[square[0]][square[1]].configure(bg="black")

# Start the Tkinter event loop
window.mainloop()
