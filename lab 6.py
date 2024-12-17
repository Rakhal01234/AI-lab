hill climb for 8 puzzles

import random

def evaluate(state):
    conflicts = 0
    n = len(state)

    # Check for conflicts between queens
    for i in range(n):
        for j in range(i + 1, n):
            if state[i] == state[j]:  # Same row
                conflicts += 1
            elif abs(state[i] - state[j]) == abs(i - j):  # Same diagonal
                conflicts += 1
    return conflicts

def hill_climbing(state):
    n = len(state)
    current_state = state
    current_conflicts = evaluate(current_state)

    while True:
        neighbors = []
        for col in range(n):
            for row in range(n):
                if row != current_state[col]:
                    neighbor = current_state[:]
                    neighbor[col] = row
                    neighbors.append(neighbor)

        best_neighbor = None
        best_conflicts = float('inf')
        for neighbor in neighbors:
            neighbor_conflicts = evaluate(neighbor)
            if neighbor_conflicts < best_conflicts:
                best_conflicts = neighbor_conflicts
                best_neighbor = neighbor

        # If no improvement is found, return the current state
        if best_conflicts >= current_conflicts:
            return current_state, current_conflicts

        current_state = best_neighbor
        current_conflicts = best_conflicts

def random_state(n=8):
    return [random.randint(0, n - 1) for _ in range(n)]

def solve_8_queens():
    initial_state = random_state()
    solution, conflicts = hill_climbing(initial_state)
    
    if conflicts == 0:
        print("Solution found!")
    else:
        print("Reached local optimum with conflicts:", conflicts)
    print("Final state:", solution)

# Solve the 8-queens problem
solve_8_queens()



2)a* algorithm for 8 queens

import heapq

N = 8  # Size of the chessboard

def heuristic(board):
    """Heuristic function to count attacking pairs of queens."""
    attacking_pairs = 0
    for i in range(N):
        for j in range(i + 1, N):
            if board[i] == board[j]:  # Same row
                attacking_pairs += 1
            if abs(board[i] - board[j]) == abs(i - j):  # Same diagonal
                attacking_pairs += 1
    return attacking_pairs

def is_safe(board, row, col):
    """Check if it's safe to place a queen at (row, col)."""
    for i in range(col):
        if board[i] == row or abs(board[i] - row) == abs(i - col):
            return False
    return True

def a_star_8_queens():
    """Solve the 8-Queens problem using A* search algorithm."""
    # Initial state: an empty board
    start_state = [-1] * N
    open_list = []
    heapq.heappush(open_list, (0, 0, start_state))  # (f(n), g(n), state)
    visited = set()

    while open_list:
        f, g, board = heapq.heappop(open_list)

        # If all queens are placed, the solution is found
        if g == N:
            print("Solution found:")
            print_board(board)
            return

        # Try placing a queen in the next column
        col = g
        for row in range(N):
            if is_safe(board, row, col):
                new_board = board[:]
                new_board[col] = row
                if tuple(new_board) not in visited:
                    visited.add(tuple(new_board))
                    h = heuristic(new_board)
                    heapq.heappush(open_list, (g + h, g + 1, new_board))

    print("No solution found.")

def print_board(board):
    """Print the chessboard."""
    for row in range(N):
        line = ['Q' if board[col] == row else '.' for col in range(N)]
        print(" ".join(line))

# Run the A* search to solve the 8-Queens problem
a_star_8_queens()
