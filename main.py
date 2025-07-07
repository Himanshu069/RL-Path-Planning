from maze import create_maze
from config import WIDTH, HEIGHT, START, GOAL
from search_based_algorithms.dijkstra import dijkstra, reconstruct_path as dijkstra_path
from animate import animate
import time

if __name__ == "__main__":
    maze = create_maze(WIDTH, HEIGHT)

    # Choose algorithm here
    print("Running Dijkstra...")
    start_time = time.time()
    snapshots, prev = dijkstra(maze, START, GOAL)
    path = dijkstra_path(prev, GOAL)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Dijkstra Computation Time: {elapsed_time:.4f} seconds")
    animate(maze, snapshots, path, elapsed_time, "dijkstra")


    # To use A*, comment above and uncomment below:
    # print("Running A*...")
    # snapshots, prev = astar(maze, START, GOAL)
    # path = astar_path(prev, GOAL)

