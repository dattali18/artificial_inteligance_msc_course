from state import Maze
from frontier_stack import FrontierStack
from frontier_queue import FrontierQueue

def _state_key(state):
    # Try to use the state directly if hashable; otherwise fall back to repr
    try:
        hash(state)
        return state
    except TypeError:
        return repr(state)

def search_id(n):
    """
    :param n: the nXn size of the maze
    :return: tuple
        [0]: True/ False arrived at the goal
        [1]: total items pushed into the frontier
        [2]: maximum frontier size observed (space complexity proxy)
    """
    # Keeping your original logic as-is because Frontier is not shown here.
    # Consider returning f.get_max_item_pushed() for the third value if Frontier supports it.
    from frontier import Frontier  # local import to avoid unused if Frontier not needed elsewhere

    s = Maze(n, n)
    f = Frontier(s)

    while not f.is_empty():
        s = f.remove()
        if s is None:
            return False, f.get_items_pushed(), f.get_items_pushed()

        if s.is_goal():
            return True, f.get_items_pushed(), f.get_items_pushed()

        ns = s.expand()
        for i in ns:
            f.insert(i)

    return False, f.get_items_pushed(), f.get_items_pushed()

def search_bfs(n):
    """
    Breadth-First Search using FrontierQueue.
    Returns (found: bool, items_pushed: int, max_frontier_size: int)
    """
    start = Maze(n, n)
    frontier = FrontierQueue()
    visited = set()

    frontier.enqueue(start)
    visited.add(_state_key(start))

    while not frontier.is_empty():
        current = frontier.dequeue()
        if current is None:
            break

        if current.is_goal():
            return True, frontier.get_items_pushed(), frontier.get_max_item_pushed()

        for neighbor in current.expand():
            k = _state_key(neighbor)
            if k in visited:
                continue
            visited.add(k)
            frontier.enqueue(neighbor)

    return False, frontier.get_items_pushed(), frontier.get_max_item_pushed()

def search_dfs(n):
    """
    Depth-First Search using FrontierStack.
    Returns (found: bool, items_pushed: int, max_frontier_size: int)
    """
    start = Maze(n, n)
    frontier = FrontierStack()
    visited = set()

    frontier.push(start)
    visited.add(_state_key(start))

    while not frontier.is_empty():
        current = frontier.pop()
        if current is None:
            break

        if current.is_goal():
            return True, frontier.get_items_pushed(), frontier.get_max_item_pushed()

        # Optionally reverse expand() for deterministic order if expand() is ordered
        for neighbor in current.expand():
            k = _state_key(neighbor)
            if k in visited:
                continue
            visited.add(k)
            frontier.push(neighbor)

    return False, frontier.get_items_pushed(), frontier.get_max_item_pushed()