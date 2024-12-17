
LAB4
1)ITERATIVE DEEP SEARCH
2)A* 
BOTH FOR 8 PUZZLE

1)import time

# Target configuration (goal state)
GOAL = (1, 2, 3, 4, 5, 6, 7, 8, 0)

# Moves for sliding tiles: up, down, left, right
MOVES = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # (row, col) directions

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

def dfs_with_limit(state, blank_pos, depth_limit, visited, path):
    """Perform DFS with a depth limit."""
    # If depth limit is reached, return None
    if len(path) > depth_limit:
        return None

    # If we reach the goal, return the path
    if state == GOAL:
        return path

    visited.add(state)

    # Generate all possible moves
    for move in MOVES:
        if is_valid_move(blank_pos, move):
            new_state, new_blank_pos = get_new_state(state, blank_pos, move)

            if new_state not in visited:
                new_path = path + [new_state]
                result = dfs_with_limit(new_state, new_blank_pos, depth_limit, visited, new_path)
                if result:
                    return result

    return None  # No solution found at this depth limit

def iterative_deepening_search(start_state):
    """Iterative Deepening Search (IDS) for solving the 8-puzzle."""
    blank_pos = start_state.index(0)  # Find the position of the blank tile
    depth_limit = 0  # Start from depth limit 0

    # Try increasing depth limits until a solution is found
    while True:
        visited = set()  # Reset visited set for each depth limit
        result = dfs_with_limit(start_state, blank_pos, depth_limit, visited, [start_state])

        if result:
            return result  # Solution found

        depth_limit += 1  # Increase depth limit if no solution found at the current limit

def solve_puzzle(start_state):
    """Solve the 8-puzzle using Iterative Deepening Search (IDS)."""
    start_time = time.time()
    solution = iterative_deepening_search(start_state)
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



2)A*

import heapq
import time

# Goal state (solved puzzle)
GOAL = (1, 2, 3, 4, 5, 6, 7, 8, 0)

# Possible moves for the blank tile (0): up, down, left, right
MOVES = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # (row, col) directions

def manhattan_distance(state):
    """Calculate the Manhattan distance of the state from the goal."""
    distance = 0
    for i, val in enumerate(state):
        if val != 0:  # Don't calculate distance for the blank tile
            goal_row, goal_col = divmod(val - 1, 3)
            current_row, current_col = divmod(i, 3)
            distance += abs(current_row - goal_row) + abs(current_col - goal_col)
    return distance

def is_valid_move(blank_pos, move):
    """Check if the move is valid based on the position of the blank tile."""
    r, c = divmod(blank_pos, 3)
    new_r, new_c = r + move[0], c + move[1]
    return 0 <= new_r < 3 and 0 <= new_c < 3

def get_new_state(state, blank_pos, move):
    """Return a new state after applying the move to the current state."""
    r, c = divmod(blank_pos, 3)
    new_r, new_c = r + move[0], c + move[1]
    
    # Convert the tuple to a list to make it mutable
    new_state = list(state)
    # Swap the blank tile (0) with the target tile
    new_state[blank_pos], new_state[new_r * 3 + new_c] = new_state[new_r * 3 + new_c], new_state[blank_pos]
    
    return tuple(new_state), new_r * 3 + new_c

def a_star(start_state):
    """A* search algorithm for solving the 8-puzzle."""
    # Find the initial position of the blank tile (0)
    blank_pos = start_state.index(0)
    
    # Priority queue to store the states to explore
    open_list = []
    # Set to store visited states
    visited = set()
    
    # Start node's cost: g(n) = 0, h(n) = Manhattan distance
    g_start = 0
    h_start = manhattan_distance(start_state)
    f_start = g_start + h_start
    
    # Push the start state into the open list (priority queue)
    heapq.heappush(open_list, (f_start, g_start, start_state, blank_pos, []))
    
    while open_list:
        # Pop the state with the lowest f(n) value
        f, g, state, blank_pos, path = heapq.heappop(open_list)
        
        # If we reach the goal state, return the solution path
        if state == GOAL:
            return path + [state]
        
        # Add the current state to the visited set
        visited.add(state)
        
        # Generate all possible moves for the blank tile (0)
        for move in MOVES:
            if is_valid_move(blank_pos, move):
                new_state, new_blank_pos = get_new_state(state, blank_pos, move)
                
                # If the new state hasn't been visited, add it to the open list
                if new_state not in visited:
                    g_new = g + 1  # The cost to reach this new state is one more than the current state
                    h_new = manhattan_distance(new_state)  # Heuristic: Manhattan distance
                    f_new = g_new + h_new  # f(n) = g(n) + h(n)
                    new_path = path + [state]  # Add the current state to the path
                    
                    # Push the new state into the open list with its f(n), g(n), and h(n)
                    heapq.heappush(open_list, (f_new, g_new, new_state, new_blank_pos, new_path))
    
    return None  # No solution found

def solve_puzzle(start_state):
    """Solve the 8-puzzle using the A* search algorithm."""
    start_time = time.time()
    solution = a_star(start_state)
    end_time = time.time()

    if solution:
        print(f"Solution found in {len(solution) - 1} steps!")
        for step in solution:
            print(step)
    else:
        print("No solution found.")
    
    print(f"Time taken: {end_time - start_time:.4f} seconds")
