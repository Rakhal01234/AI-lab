8 puzzel using dfs

import time

# Target configuration (goal state)
GOAL = (1, 2, 3, 4, 5, 6, 7, 8, 0)

# Moves for sliding tiles: up, down, left, right
MOVES = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # (row, col) directions

def manhattan_distance(state):
    """Calculate the Manhattan distance of the state from the goal."""
    distance = 0
    for i, val in enumerate(state):
        if val != 0:  # Don't calculate distance for the empty tile
            goal_row, goal_col = divmod(val - 1, 3)
            current_row, current_col = divmod(i, 3)
            distance += abs(current_row - goal_row) + abs(current_col - goal_col)
    return distance

def is_valid_move(blank_pos, move):
    """Check if the move is valid based on the blank tile's position."""
    r, c = divmod(blank_pos, 3)
    new_r, new_c = r + move[0], c + move[1]
    return 0 <= new_r < 3 and 0 <= new_c < 3

def get_new_state(state, blank_pos, move):
    """Return a new state after applying the move."""
    r, c = divmod(blank_pos, 3)
    new_r, new_c = r + move[0], c + move[1]
    
    # Convert the tuple to a list to make it mutable
    new_state = list(state)
    # Swap the blank tile (0) with the target tile
    new_state[blank_pos], new_state[new_r * 3 + new_c] = new_state[new_r * 3 + new_c], new_state[blank_pos]
    
    return tuple(new_state), new_r * 3 + new_c

def dfs(start_state):
    """Depth-First Search algorithm for solving the 8-puzzle."""
    # Find the initial position of the blank (0)
    blank_pos = start_state.index(0)
    
    # Set up visited set to avoid revisiting states
    visited = set()
    
    # Stack to manage the DFS (explicit stack-based DFS)
    stack = [(start_state, blank_pos, [start_state])]
    
    while stack:
        state, blank_pos, path = stack.pop()
        
        # If the current state is the goal state, return the solution path
        if state == GOAL:
            return path
        
        # Add state to visited
        visited.add(state)
        
        # Generate all possible moves
        for move in MOVES:
            if is_valid_move(blank_pos, move):
                new_state, new_blank_pos = get_new_state(state, blank_pos, move)
                
                # If the new state hasn't been visited yet, add to stack
                if new_state not in visited:
                    new_path = path + [new_state]
                    stack.append((new_state, new_blank_pos, new_path))
    
    return None  # No solution found

def solve_puzzle(start_state):
    """Solve the 8-puzzle using DFS."""
    start_time = time.time()
    solution = dfs(start_state)
    end_time = time.time()

    if solution:
        print(f"Solution found in {len(solution) - 1} steps!")
        for step in solution:
            print(step)
    else:
        print("No solution found.")
    
    print(f"Time taken: {end_time - start_time:.4f} seconds")

# Example usage:
start_state = (1, 2, 3, 4, 5, 6, 7, 0, 8)  # A random start state
solve_puzzle(start_state)
