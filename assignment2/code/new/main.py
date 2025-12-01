from search import NUM_RUNS, MAZE_SIZE, run_search_algorithm
from state import Maze


def main():
    # --- Simulation Setup ---
    results = {
        "Uniform Cost Search (UCS)": {"found_count": 0, "path_len_sum": 0, "expanded_sum": 0,
                                      "no_solution_expanded_sum": 0,
                                      "no_solution_count": 0},
        "Greedy Search (Manhattan)": {"found_count": 0, "path_len_sum": 0, "expanded_sum": 0,
                                      "no_solution_expanded_sum": 0,
                                      "no_solution_count": 0},
        "A* (Euclidean Heuristic)": {"found_count": 0, "path_len_sum": 0, "expanded_sum": 0,
                                     "no_solution_expanded_sum": 0,
                                     "no_solution_count": 0},
        "A* (Manhattan Heuristic)": {"found_count": 0, "path_len_sum": 0, "expanded_sum": 0,
                                     "no_solution_expanded_sum": 0,
                                     "no_solution_count": 0}
    }

    search_params = [
        ("Uniform Cost Search (UCS)", "none", "ucs"),
        ("Greedy Search (Manhattan)", "manhattan", "greedy"),
        ("A* (Euclidean Heuristic)", "euclidean", "a_star"),
        ("A* (Manhattan Heuristic)", "manhattan", "a_star")
    ]

    # --- Main Simulation Loop ---
    for run_idx in range(NUM_RUNS):
        # 1. Create a single random maze configuration
        current_maze = Maze(MAZE_SIZE, MAZE_SIZE)
        current_maze.initial()

        # 2. Run all search algorithms on the same maze
        for key, h_type, s_type in search_params:

            path_info = run_search_algorithm(current_maze, h_type, s_type)

            # path_info is (path_len/max_open_size, num_expanded, found_solution)

            if path_info[2]:  # found_solution
                results[key]["found_count"] += 1
                results[key]["path_len_sum"] += path_info[0]
                results[key]["expanded_sum"] += path_info[1]
            else:
                results[key]["no_solution_count"] += 1
                results[key]["no_solution_expanded_sum"] += path_info[1]

    # --- Calculate and Print Results ---

    print(f"--- Search Algorithm Performance Summary ({NUM_RUNS} runs of {MAZE_SIZE}x{MAZE_SIZE} Mazes) ---\n")

    header = "| Algorithm | % Mazes Solved | Avg Path Length (Solved) | Avg Expansions (Solved) | Avg Expansions (No Solution) |"
    separator = "|:---|:---:|:---:|:---:|:---:|"
    print(header)
    print(separator)

    for key, data in results.items():
        # Percent Mazes Solved
        percent_found = (data["found_count"] / NUM_RUNS) * 100

        # Average Path Length (Solved)
        avg_path_len = data["path_len_sum"] / data["found_count"] if data["found_count"] > 0 else "N/A"

        # Average Expansions (Solved)
        avg_expanded_found = data["expanded_sum"] / data["found_count"] if data["found_count"] > 0 else "N/A"

        # Average Expansions (No Solution)
        avg_expanded_no_solution = data["no_solution_expanded_sum"] / data["no_solution_count"] if data[
                                                                                                       "no_solution_count"] > 0 else "N/A"

        # Format N/A for clean output
        avg_path_len_str = f"{avg_path_len:.2f}" if isinstance(avg_path_len, float) else avg_path_len
        avg_expanded_found_str = f"{avg_expanded_found:.2f}" if isinstance(avg_expanded_found,
                                                                           float) else avg_expanded_found
        avg_expanded_no_solution_str = f"{avg_expanded_no_solution:.2f}" if isinstance(avg_expanded_no_solution,
                                                                                       float) else avg_expanded_no_solution

        row = f"| {key} | {percent_found:.2f}% | {avg_path_len_str} | {avg_expanded_found_str} | {avg_expanded_no_solution_str} |"
        print(row)

    print("\n*Expansions refer to the number of states removed from the OPEN list for processing.")


if __name__ == "__main__":
    main()
