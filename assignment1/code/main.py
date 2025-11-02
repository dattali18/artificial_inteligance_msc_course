from search import *

NUM_ITERATIONS = 100
MAZE_SIZE = 5


def analyze_results(results):
    """
    Analyzes the results list and computes the required metrics.
    """
    success_runs = [r for r in results if r[0]]
    failure_runs = [r for r in results if not r[0]]

    total_runs = len(results)
    success_count = len(success_runs)
    failure_count = len(failure_runs)

    # 1. Percentage of successful search
    success_percent = (success_count / total_runs) * 100

    # 2. Average number of iteration (successful)
    avg_success_iters = sum(r[1] for r in success_runs) / success_count if success_count > 0 else 0.0

    # 3. Average maximum path (successful)
    avg_success_path = sum(r[2] for r in success_runs) / success_count if success_count > 0 else 0.0

    # 4. Average iteration for unsuccessful
    avg_fail_iters = sum(r[1] for r in failure_runs) / failure_count if failure_count > 0 else 0.0

    return {
        "success_percent": success_percent,
        "avg_success_iters": avg_success_iters,
        "avg_success_path_length": avg_success_path,
        "avg_fail_iters": avg_fail_iters
    }


def main():
    """
    Runs 100 iterations for each search algorithm and prints the aggregated statistics.
    """

    import random
    import time

    random.seed(time.time())

    print(f"--- Running {NUM_ITERATIONS} Trials on Maze Size {MAZE_SIZE}x{MAZE_SIZE} ---")

    bfs_results = []
    dfs_results = []
    id_results = []

    for i in range(1, NUM_ITERATIONS + 1):
        # Run all searches on the same configuration (Maze(n,n).initial()
        # creates a NEW maze internally, so they are independent trials)

        # Using try-except to handle potential errors from Maze/Frontier imports/logic
        try:
            bfs_results.append(search_bfs(MAZE_SIZE))
            dfs_results.append(search_dfs(MAZE_SIZE))
            id_results.append(search_id(MAZE_SIZE))

            if i % 10 == 0:
                print(f"Trial {i} completed...")

        except Exception as e:
            # Handle cases where the external Maze or Frontier classes might fail
            # to prevent the entire loop from crashing.
            print(f"Warning: Trial {i} failed with error: {e}. Skipping this trial.")
            continue

    # Analyze and print results for each algorithm
    algorithms = {
        "BFS (Breadth-First Search)": bfs_results,
        "DFS (Depth-First Search)": dfs_results,
        "ID (Iterative Deepening Search)": id_results,
    }

    print("\n" + "=" * 50)
    print("      STATISTICAL ANALYSIS RESULTS")
    print("=" * 50)

    for name, results in algorithms.items():
        if not results:
            continue

        metrics = analyze_results(results)

        print(f"\n--- {name} ---")
        print(f"Success Rate: {metrics['success_percent']:.2f}%")
        print(f"Avg Successful Iterations: {metrics['avg_success_iters']:.2f}")
        print(f"Avg Solution Path Length (Successful): {metrics['avg_success_path_length']:.2f}")
        print(f"Avg Unsuccessful Iterations: {metrics['avg_fail_iters']:.2f}%")

    print("\n" + "=" * 50)


if __name__ == "__main__":
    main()