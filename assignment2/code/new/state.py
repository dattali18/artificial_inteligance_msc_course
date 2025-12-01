# state.py

"""
The state is a list of 2 items: the board, the path
"""

import math
import random


class Maze:

    # Updated to include heuristic_type
    def __init__(self, width, height, maze=None, path=None, heuristic_type='manhattan'):
        self.width = width
        self.height = height
        self.heuristic_type = heuristic_type  # Added for A* and Greedy

        if maze is None:
            self.maze = [[0 for _ in range(width)] for _ in range(height)]
        else:
            self.maze = maze

        if path is None:
            self.path = [(0, 0)]
        else:
            self.path = path

    # Updated to pass heuristic_type
    def copy(self):
        return Maze(self.width, self.height, self.maze, self.path, self.heuristic_type)

    def initial(self):
        # Randomly make paths (3/4 open, 1/4 wall)
        for y in range(self.height):
            for x in range(self.width):
                self.maze[y][x] = random.choice([0, 0, 0, 1])

        # Ensure start (0, 0) and end (width-1, height-1) are open
        self.maze[0][0] = 0
        self.maze[self.height - 1][self.width - 1] = 0
        self.path = [(0, 0)]

    def user_location(self):
        return self.path[-1]

    def hdistance(self):
        # Calculates the heuristic distance to the goal (width-1, height-1)
        x, y = self.user_location()
        goal_x, goal_y = self.width - 1, self.height - 1

        if self.heuristic_type == 'manhattan':
            # Manhattan distance: |x1 - x2| + |y1 - y2|
            return abs(x - goal_x) + abs(y - goal_y)

        elif self.heuristic_type == 'euclidean':
            # Euclidean distance: sqrt((x1 - x2)^2 + (y1 - y2)^2)
            return math.sqrt((x - goal_x) ** 2 + (y - goal_y) ** 2)

        else:
            # Used for UCS (where h(n) = 0)
            return 0

    def print_maze(self):
        for y in range(self.height):
            for x in range(self.width):
                if (x, y) == self.user_location():
                    print('U', end='')
                elif (x, y) == (self.width - 1, self.height - 1):
                    print('G', end='')
                elif (x, y) in self.path:
                    print('*', end='')
                else:
                    print('#' if self.maze[y][x] == 1 else '.', end='')
            print()

    def is_goal(self):
        return self.user_location() == (self.width - 1, self.height - 1)

    def expand(self):
        x, y = self.user_location()
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Down, Right, Up, Left
        possible_moves = []

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.width and \
                    0 <= ny < self.height and self.maze[ny][nx] == 0:
                currpath = self.path[:]
                currpath.append((nx, ny))
                # Passing heuristic_type to the new state
                m = Maze(self.width, self.height, self.maze, currpath, self.heuristic_type)
                possible_moves.append(m)

        return possible_moves

    def path_len(self):
        return len(self.path)
