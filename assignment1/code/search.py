#search
# זהו הפתרון של תרגיל 1 והוא מימוש בפייתון לפסיאודוקוד שהוצג בכיתה


from state import Maze
from frontier import Frontier

def search(n):
    s = Maze(n,n)
    s.initial()
    s.print_maze()
    f = Frontier(s)
    while not f.is_empty():
        s = f.remove()
        if s == 0:
            return 0
        print()
        print("Current state: ")
        s.print_maze()
        if s.is_goal():
            print("Reached the goal!")
            return s
        ns = s.expand()
        print("next states: ")
        print([i.path for i in ns], end='')
        for i in ns:
            f.insert(i)
    print("no solution")
    return 0
