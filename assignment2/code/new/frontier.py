# frontier.py

"""
implements a priority queue using a minimum heap
"""
import math


def create(s, f):
    # 'opened': The min-heap (priority queue)
    # 'closed': Dictionary to track expanded locations: { (x, y): min_path_len }
    # 'path_len_map': Tracks minimum known path length for states currently in 'opened'
    return {"opened": [s], "function": f, "closed": {}, "total": 1, "max": 1,
            "path_len_map": {s.user_location(): s.path_len()}}


def is_empty(f):
    return f["opened"] == []


def parent(i):
    return (i + 1) // 2 - 1


def leftSon(i):
    return (i + 1) * 2 - 1


def rightSon(i):
    return (i + 1) * 2


def swap(l, x, y):
    t = l[x]
    l[x] = l[y]
    l[y] = t


# Utility function to fix the heap upwards after insertion/update
def update_heap_up(pq, i):
    f = pq["opened"]
    val = pq["function"]
    while i > 0 and val(f[i]) < val(f[parent(i)]):
        swap(f, i, parent(i))
        i = parent(i)


def insert(pq, s):
    val = pq["function"]
    f = pq["opened"]
    current_loc = s.user_location()

    # 1. Check against CLOSED list
    if current_loc in pq["closed"]:
        old_path_len = pq["closed"][current_loc]
        if s.path_len() >= old_path_len:
            return  # Path is not better, ignore
        else:
            # Found a better path to a closed state: Re-open it
            del pq["closed"][current_loc]

    # 2. Check against OPENED list
    old_path_len = pq["path_len_map"].get(current_loc)

    if old_path_len is not None:
        if s.path_len() < old_path_len:
            # Found a better path to an opened state: Insert the new state and update the map.
            # The old, suboptimal state will be discarded in remove()
            pq["path_len_map"][current_loc] = s.path_len()

            f.append(s)
            i = len(f) - 1
            pq["total"] = pq["total"] + 1
            update_heap_up(pq, i)

        return  # Path is not better (or just inserted)

    # 3. New state (not in opened or closed)

    f.append(s)
    i = len(f) - 1
    pq["path_len_map"][current_loc] = s.path_len()
    pq["total"] = pq["total"] + 1

    update_heap_up(pq, i)


def remove(pq):
    f = pq["opened"]
    m = pq["max"]
    if is_empty(pq):
        return None

    if len(f) > m:
        pq["max"] = len(f)

    s = f[0]
    f[0] = f[len(f) - 1]
    del f[-1]
    heapify(pq, 0)

    # Handle suboptimal duplicates in the heap (only for A* and UCS)
    # If the retrieved state has a longer path than recorded in path_len_map, it's a duplicate.
    while s.path_len() > pq["path_len_map"].get(s.user_location(), math.inf):
        if is_empty(pq): return None

        s = f[0]
        f[0] = f[len(f) - 1]
        del f[-1]
        heapify(pq, 0)

        # Add to CLOSED list only after ensuring it's the optimal state
    pq["closed"][s.user_location()] = s.path_len()

    return s


def heapify(pq, i):
    minSon = i
    val = pq["function"]
    f = pq["opened"]
    if leftSon(i) < len(f) and val(f[leftSon(i)]) < val(f[minSon]):
        minSon = leftSon(i)
    if rightSon(i) < len(f) and val(f[rightSon(i)]) < val(f[minSon]):
        minSon = rightSon(i)
    if minSon != i:
        swap(f, i, minSon)
        heapify(pq, minSon)
