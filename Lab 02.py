vacuum cleaner algorithm

import random

class VacuumCleaner:
    def __init__(self, grid_size, start_position):
        self.grid_size = grid_size  # Grid dimensions (rows, cols)
        self.grid = self.create_grid()  # Generate a grid with some dirt
        self.position = start_position  # Initial position (row, col)
        self.cleaned_count = 0  # Number of cleaned cells

    def create_grid(self):
        """Creates a grid of random dirt spots."""
        grid = []
        for i in range(self.grid_size[0]):
            row = [random.choice([0, 1]) for _ in range(self.grid_size[1])]
            grid.append(row)
        return grid

    def display_grid(self):
        """Displays the current grid."""
        for row in self.grid:
            print(' '.join(str(cell) for cell in row))
        print(f"Cleaned cells: {self.cleaned_count}")
        print(f"Current Position: {self.position}\n")
    
    def move(self, direction):
        """Move the vacuum cleaner in a given direction: 'up', 'down', 'left', 'right'."""
        row, col = self.position
        
        if direction == "up" and row > 0:
            row -= 1
        elif direction == "down" and row < self.grid_size[0] - 1:
            row += 1
        elif direction == "left" and col > 0:
            col -= 1
        elif direction == "right" and col < self.grid_size[1] - 1:
            col += 1
        
        self.position = (row, col)
    
    def clean(self):
        """Clean the current cell if it's dirty."""
        row, col = self.position
        if self.grid[row][col] == 1:  # If the cell is dirty
            self.grid[row][col] = 0  # Clean the cell
            self.cleaned_count += 1
            print(f"Cleaning position {self.position}...")
    
    def is_cleaned(self):
        """Check if all cells are cleaned."""
        return self.cleaned_count == sum(sum(row) for row in self.grid)
    
    def run(self):
        """Run the vacuum cleaner algorithm."""
        while not self.is_cleaned():
            self.clean()
            # Try to move in a random direction for simplicity
            direction = random.choice(["up", "down", "left", "right"])
            self.move(direction)
            self.display_grid()
        print("All cells are cleaned!")

# Example usage
vacuum = VacuumCleaner(grid_size=(5, 5), start_position=(0, 0))
vacuum.run()
