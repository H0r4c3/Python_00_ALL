class Cell:
    """
    Represents a cell in a 5x5 grid with position-determined value, light status, and automatic neighbor setup.
    Values are automatically assigned based on position (1-25) starting from top-left,
    going row by row.
    """
    
    # Class variable to store all created cells
    _grid = {}
    # Dictionary to map values to cell positions for quick lookup
    _value_to_position = {}
    
    def __init__(self, row, column, light=False):
        """
        Initialize a new Cell object and set up its neighbors.
        
        Args:
            row (int): Row position (0-4)
            column (int): Column position (0-4)
            light (bool, optional): Initial light status. Defaults to False.
        """
        # Validate input parameters
        if not (0 <= row <= 4 and 0 <= column <= 4):
            raise ValueError("Row and column must be between 0 and 4")
            
        self._row = row
        self._column = column
        
        # Calculate value based on position (1-25)
        self._value = row * 5 + column + 1
        
        self._light = light
        
        # Store this cell in our tracking systems
        Cell._grid[(row, column)] = self
        Cell._value_to_position[self._value] = (row, column)
        
        # Set up neighbors
        self._setup_neighbors()
    
    def _setup_neighbors(self):
        """
        Sets up all neighbor relationships for this cell.
        Creates new cells for neighbors that don't exist yet and
        establishes bidirectional relationships.
        """
        # Initialize all neighbors
        self._up = None
        self._down = None
        self._left = None
        self._right = None
        
        # Check and create up neighbor
        if self._row > 0:
            up_pos = (self._row - 1, self._column)
            if up_pos in Cell._grid:
                self._up = Cell._grid[up_pos]
            else:
                self._up = Cell(self._row - 1, self._column)
            self._up._down = self
            
        # Check and create down neighbor
        if self._row < 4:
            down_pos = (self._row + 1, self._column)
            if down_pos in Cell._grid:
                self._down = Cell._grid[down_pos]
            else:
                self._down = Cell(self._row + 1, self._column)
            self._down._up = self
            
        # Check and create left neighbor
        if self._column > 0:
            left_pos = (self._row, self._column - 1)
            if left_pos in Cell._grid:
                self._left = Cell._grid[left_pos]
            else:
                self._left = Cell(self._row, self._column - 1)
            self._left._right = self
            
        # Check and create right neighbor
        if self._column < 4:
            right_pos = (self._row, self._column + 1)
            if right_pos in Cell._grid:
                self._right = Cell._grid[right_pos]
            else:
                self._right = Cell(self._row, self._column + 1)
            self._right._left = self
    
    # Essential property definitions
    @property
    def row(self):
        """Get the row position of the cell."""
        return self._row
    
    @property
    def column(self):
        """Get the column position of the cell."""
        return self._column
    
    @property
    def value(self):
        """Get the cell's value (1-25)."""
        return self._value
    
    @property
    def light(self):
        """Get the cell's light status."""
        return self._light
    
    @property
    def up(self):
        """Get the cell's up neighbor."""
        return self._up
    
    @property
    def down(self):
        """Get the cell's down neighbor."""
        return self._down
    
    @property
    def left(self):
        """Get the cell's left neighbor."""
        return self._left
    
    @property
    def right(self):
        """Get the cell's right neighbor."""
        return self._right
    
    def switch_light(self):
        """
        Switches the light status of the cell between True and False.
        
        Returns:
            bool: The new light status
        """
        self._light = not self._light
        return self._light
    
    def click(self):
        """
        Performs a click action on this cell, which:
        1. Switches this cell's light
        2. Switches the lights of all existing neighbors (up, down, left, right)
        """
        # Switch this cell's light
        self.switch_light()
        
        # Switch lights of all existing neighbors
        if self._up:
            self._up.switch_light()
        if self._down:
            self._down.switch_light()
        if self._left:
            self._left.switch_light()
        if self._right:
            self._right.switch_light()
    
    @classmethod
    def get_cell_by_value(cls, value):
        """
        Finds and returns a cell by its value. Creates the cell if it doesn't exist.
        
        Args:
            value (int): The value to look for (1-25)
            
        Returns:
            Cell: The cell with the specified value
            
        Raises:
            ValueError: If value is not between 1 and 25
        """
        if not (1 <= value <= 25):
            raise ValueError("Value must be between 1 and 25")
            
        # If we know this value, return its cell
        if value in cls._value_to_position:
            row, col = cls._value_to_position[value]
            return cls._grid[(row, col)]
            
        # If we don't have this cell yet, create it
        row = (value - 1) // 5
        col = (value - 1) % 5
        return Cell(row, col)
    
    @classmethod
    def click_cells(cls, values):
        """
        Clicks multiple cells specified by their values.
        
        Args:
            values (list): List of values (1-25) indicating which cells to click
            
        Example:
            Cell.click_cells([5, 7, 13, 14, 18])
        """
        for value in values:
            cell = cls.get_cell_by_value(value)
            cell.click()
    
    @classmethod
    def reset_grid(cls):
        """
        Resets the grid by clearing all stored cells and value mappings.
        """
        cls._grid.clear()
        cls._value_to_position.clear()
    
    def __str__(self):
        """
        Returns a string representation of the cell.
        """
        return f"Cell({self.row}, {self.column}): value={self.value}, light={'ON' if self.light else 'OFF'}"

# set all cells in [5, 7, 13, 14, 18] to ON
for val in [5, 7, 13, 14, 18]:
    cell = Cell.get_cell_by_value(val)
    cell.switch_light()
    print(f'The light for {cell.value} is {cell.light}')
    
print(Cell._grid)