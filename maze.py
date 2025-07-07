import numpy as np

def create_maze(width, height):
    maze = np.zeros((height, width), dtype=int)
    maze[5:30, 10] = 1
    maze[10, 5:25] = 1
    maze[5:20, 30] = 1
    maze[25, 30:45] = 1
    return maze