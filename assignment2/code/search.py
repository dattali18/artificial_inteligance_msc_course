#search
#Pseudo code for exercise 2

import state
import frontier

def search(n):
    s=state.Maze(n,n)
    s.initial()
    s.print_maze()
    f=frontier.create(s, lambda stat: stat.hdistance()+stat.path_len())
    while not frontier.is_empty(f):
        s=frontier.remove(f)
        print()
        print("Current state: ")
        s.print_maze()

        if s.is_goal():
            print("Reached the goal!")
            return s
        ns=s.expand()
        print("next states: ")
        print([i.path for i in ns], end='')
        for i in ns:
            frontier.insert(f,i)
    print("no solution")
    return 0

search(5)