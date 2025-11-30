"""
The state is a list of 2 items: the board, the path
"""

import random
import math

class Maze:
    def copy(self):
        return Maze(self.width, self.height, self.maze, self.path)

    def __init__(self, width, height, maze=None, path=None):
        self.width = width
        self.height = height
        
        if maze is None:
            self.maze = [[0 for _ in range(width)] for _ in range(height)]
        else:
            self.maze = maze
        
        if path is None:
            self.path = [(0,0)]
        else:
            self.path = path


        
    def initial(self):
        # Randomly make paths
        for y in range(self.height ):
            for x in range(self.width):
                self.maze[y][x] = random.choice([0, 0, 0, 1])

       
        # Ensure start (0, 0) and end (width-1, height-1) are open
        self.maze[0][0] = 0
        self.maze[self.height - 1][self.width - 1] = 0
        self.path = [(0,0)]
        
     
    def user_location(self):
        return self.path[-1]

    def hdistance(self):
        return 0

    def print_maze(self):
        for y in range(self.height):
            for x in range(self.width):
                if (x, y) == self.user_location():
                    print('U', end='')
                elif (x, y) == (self.width-1, self.height-1):
                    print('G', end='')
                elif (x, y) in self.path:
                    print('*', end='')
                else:
                    print('#' if self.maze[y][x] == 1 else '.', end='')
            print()  # New line after each row

    def is_goal(self):
        # Check if the user has reached the target location (width-1, height-1)
        return self.user_location() == (self.width - 1, self.height - 1)

    def expand(self):
        x, y = self.user_location()
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Down, Right, Up, Left
        possible_moves = []

        for dx, dy in directions: #look for possible actions
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.width and \
                0 <= ny < self.height and self.maze[ny][nx] == 0 and \
                (nx, ny) not in self.path:
                   
                    
                    currpath = self.path[:]
                    currpath.append((nx, ny))
                    m = Maze(self.width, self.height, self.maze, currpath)
                    possible_moves.append(m)

        return possible_moves
    
    
    def path_len(self):
        # Count the number of '*' in the maze
        return len(self.path)
    
 

