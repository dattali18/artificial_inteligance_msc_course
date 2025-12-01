# main.py

import frontier
import state

# --- Configuration ---
MAZE_SIZE = 5
NUM_RUNS = 100


def run_search_algorithm(initial_maze, heuristic_type, search_type):
    """
    Executes a single search run and collects performance metrics.
    :param initial_maze: An existing Maze object (board configuration)
    :param heuristic_type: 'manhattan', 'euclidean', or 'none'
    :param search_type: 'ucs', 'greedy', or 'a_star'
    :returns: (path_len/max_open_size, num_expanded_nodes, found_solution)
    """

    # 1. Define the Evaluation Function f(n)
    if search_type == 'ucs':
        # UCS: f(n) = g(n) = path_len()
        f_func = lambda stat: stat.path_len()
    elif search_type == 'greedy':
        # Greedy: f(n) = h(n) = hdistance()
        f_func = lambda stat: stat.hdistance()
    elif search_type == 'a_star':
        # A*: f(n) = g(n) + h(n)
        f_func = lambda stat: stat.path_len() + stat.hdistance()
    else:
        raise ValueError("Invalid search_type")

    # 2. Initialize State and Frontier
    # Create a new starting state with the existing board and correct heuristic type
    s = state.Maze(MAZE_SIZE, MAZE_SIZE, initial_maze.maze, [(0, 0)], heuristic_type)

    f = frontier.create(s, f_func)

    num_expanded = 0

    # 3. Main Search Loop
    while True:
        s = frontier.remove(f)

        if s is None:
            # Frontier is empty, no solution found
            return f["max"], num_expanded, False

            # Check if the path is better than the one stored in closed
        # This check is primarily handled inside frontier.remove() for duplicates.
        # If the state *was* in closed, we just re-opened it (handled in frontier.insert).

        # 4. Goal Test
        if s.is_goal():
            return s.path_len(), num_expanded, True

        # 5. Expand State (Increment Counter)
        num_expanded += 1

        ns = s.expand()
        for i in ns:
            frontier.insert(f, i)

    # Should not be reached
    return 0, 0, False
