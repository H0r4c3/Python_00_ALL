import tkinter as tk
from tkinter import messagebox
import numpy as np

class LightsOutGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Lights Out Game")
        
        # Initialize game state using numpy array (False = off, True = on)
        self.grid = np.zeros((5, 5), dtype=bool)
        
        # Colors for the buttons
        self.ON_COLOR = "#ffff00"  # Yellow for lit buttons
        self.OFF_COLOR = "#404040"  # Dark gray for unlit buttons
        
        # Create main frame with padding
        self.main_frame = tk.Frame(self.root, padx=10, pady=10)
        self.main_frame.pack(expand=True)
        
        # Create title label
        title = tk.Label(self.main_frame, text="Lights Out", font=('Arial', 16, 'bold'))
        title.pack(pady=(0, 10))
        
        # Create game board frame
        self.board_frame = tk.Frame(self.main_frame)
        self.board_frame.pack()
        
        # Create buttons for the 5x5 grid
        self.buttons = []
        for i in range(5):
            row_buttons = []
            for j in range(5):
                # Create button with specific size and styling
                btn = tk.Button(self.board_frame, width=4, height=2,
                              relief="raised", borderwidth=3)
                btn.grid(row=i, column=j, padx=2, pady=2)
                # Bind click event using lambda to pass coordinates
                btn.configure(command=lambda x=i, y=j: self.handle_click(x, y))
                row_buttons.append(btn)
            self.buttons.append(row_buttons)
        
        # Create control buttons
        control_frame = tk.Frame(self.main_frame)
        control_frame.pack(pady=10)
        
        new_game_btn = tk.Button(control_frame, text="New Game", 
                                command=self.new_game)
        new_game_btn.pack(side=tk.LEFT, padx=5)
        
        reset_btn = tk.Button(control_frame, text="Reset", 
                             command=self.reset_game)
        reset_btn.pack(side=tk.LEFT, padx=5)
        
        # Initialize moves counter
        self.moves_count = 0
        self.moves_label = tk.Label(self.main_frame, text="Moves: 0")
        self.moves_label.pack(pady=5)
        
        # Start new game
        self.initial_state = None
        self.new_game()
    
    def handle_click(self, row, col):
        """Handle button clicks and update the game state"""
        self.toggle_lights(row, col)
        self.moves_count += 1
        self.moves_label.config(text=f"Moves: {self.moves_count}")
        
        # Check if puzzle is solved
        if self.is_solved():
            messagebox.showinfo("Congratulations!", 
                              f"You solved the puzzle in {self.moves_count} moves!")
    
    def toggle_lights(self, row, col):
        """Toggle the clicked light and adjacent lights"""
        # Define adjacent positions (including clicked position)
        positions = [(row, col)]  # Center
        if row > 0: positions.append((row-1, col))  # Up
        if row < 4: positions.append((row+1, col))  # Down
        if col > 0: positions.append((row, col-1))  # Left
        if col < 4: positions.append((row, col+1))  # Right
        
        # Toggle each position
        for pos_row, pos_col in positions:
            self.grid[pos_row, pos_col] = not self.grid[pos_row, pos_col]
            # Update button color
            self.update_button_color(pos_row, pos_col)
    
    def update_button_color(self, row, col):
        """Update the color of a button based on its state"""
        color = self.ON_COLOR if self.grid[row, col] else self.OFF_COLOR
        self.buttons[row][col].configure(bg=color)
    
    def is_solved(self):
        """Check if all lights are off"""
        return not np.any(self.grid)
    
    def generate_solvable_puzzle(self):
        """Generate a new solvable puzzle"""
        self.grid.fill(False)
        # Make random moves to create a solvable puzzle
        num_moves = np.random.randint(5, 15)
        for _ in range(num_moves):
            row = np.random.randint(0, 5)
            col = np.random.randint(0, 5)
            self.toggle_lights(row, col)
        # Store initial state for reset functionality
        self.initial_state = self.grid.copy()
    
    def new_game(self):
        """Start a new game"""
        self.moves_count = 0
        self.moves_label.config(text="Moves: 0")
        self.generate_solvable_puzzle()
        # Update all button colors
        for i in range(5):
            for j in range(5):
                self.update_button_color(i, j)
    
    def reset_game(self):
        """Reset the current game to its initial state"""
        if self.initial_state is not None:
            self.grid = self.initial_state.copy()
            self.moves_count = 0
            self.moves_label.config(text="Moves: 0")
            # Update all button colors
            for i in range(5):
                for j in range(5):
                    self.update_button_color(i, j)

# Create and run the application
if __name__ == "__main__":
    root = tk.Tk()
    game = LightsOutGUI(root)
    root.mainloop()