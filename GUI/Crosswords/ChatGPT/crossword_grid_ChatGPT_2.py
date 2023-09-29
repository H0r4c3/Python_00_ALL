import tkinter as tk

class CrosswordGrid:
    def __init__(self, master, size):
        self.master = master
        self.size = size
        self.cells = {}
        for row in range(size):
            for col in range(size):
                cell = tk.Entry(master, width=2, font=('Arial', 50))
                cell.grid(row=row, column=col)
                self.cells[(row, col)] = cell

if __name__ == '__main__':
    root = tk.Tk()
    crossword = CrosswordGrid(root, size=10)
    
    # Add black squares to the grid
    crossword.cells[1, 1].configure(bg="black")
    crossword.cells[3, 3].configure(bg="black")
    
    root.mainloop()
