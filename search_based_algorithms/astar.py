import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from maze import create_maze
from config import WIDTH, HEIGHT, START, GOAL
from algorithms.dijkstra import dijkstra, reconstruct_path

