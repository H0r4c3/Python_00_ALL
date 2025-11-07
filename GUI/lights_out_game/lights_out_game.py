'''
Lights Out is an electronic game released by Tiger Electronics in 1995.[1] 
The game consists of a 5 by 5 grid of lights. When the game starts, a random number or a stored pattern of these lights is switched on. 
Pressing any of the lights will toggle it and the adjacent lights. The goal of the puzzle is to switch all the lights off, preferably 
with as few button presses as possible.[1][2]. 
Create a grid 5x5 where I can try solving a randomly starting situation (having a solution) 
where I can click on lights. All in a Class.
'''

import random
import numpy as np

class LightsOut:
    def __init__(self):
        # Initialize the 5x5 grid with all lights off (False)
        self.grid = np.zeros((5, 5), dtype=bool)
        # Generate a solvable puzzle
        self._generate_solvable_puzzle()
        
    def _generate_solvable_puzzle(self):
        """
        Generates a solvable puzzle by performing random valid moves.
        This ensures the puzzle has a solution.
        """
        # Start with all lights off
        self.grid.fill(False)
        
        # Perform random moves to create a solvable puzzle
        num_moves = random.randint(5, 15)
        for _ in range(num_moves):
            row = random.randint(0, 4)
            col = random.randint(0, 4)
            self._toggle_lights(row, col)
    
    def _toggle_lights(self, row, col):
        """
        Toggles the light at the given position and its adjacent lights.
        
        Args:
            row (int): Row index of the light to toggle
            col (int): Column index of the light to toggle
        """
        # Toggle the clicked light
        self.grid[row, col] = not self.grid[row, col]
        
        # Toggle adjacent lights
        adjacent = [
            (row-1, col), # Above
            (row+1, col), # Below
            (row, col-1), # Left
            (row, col+1)  # Right
        ]
        
        for adj_row, adj_col in adjacent:
            if 0 <= adj_row < 5 and 0 <= adj_col < 5:
                self.grid[adj_row, adj_col] = not self.grid[adj_row, adj_col]
    
    def make_move(self, row, col):
        """
        Makes a move at the specified position and returns whether the puzzle is solved.
        
        Args:
            row (int): Row index of the move
            col (int): Column index of the move
            
        Returns:
            bool: True if the puzzle is solved, False otherwise
        """
        if not (0 <= row < 5 and 0 <= col < 5):
            raise ValueError("Invalid position")
            
        self._toggle_lights(row, col)
        return self.is_solved()
    
    def is_solved(self):
        """
        Checks if all lights are turned off.
        
        Returns:
            bool: True if all lights are off, False otherwise
        """
        return not np.any(self.grid)
    
    def get_grid(self):
        """
        Returns the current state of the grid.
        
        Returns:
            numpy.ndarray: 5x5 boolean array representing the grid
        """
        return self.grid.copy()
    
    def display(self):
        """
        Returns a string representation of the grid using O for on and . for off.
        
        Returns:
            str: String representation of the grid
        """
        return '\n'.join([' '.join('O' if cell else '.' for cell in row) 
                         for row in self.grid])
        
# Create a new game
game = LightsOut()

# Display the initial state
print("Initial puzzle:")
print(game.display())

# Make moves (row and column are 0-4)
# For example, to press the light at position (1,2):
game.make_move(1, 2)

print("\nAfter move:")
print(game.display())

# Check if solved
if game.is_solved():
    print("Congratulations! You solved the puzzle!")