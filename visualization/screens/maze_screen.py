from visualization.elements.Cell import Cell
import pygame
import config
from visualization import event_handler, render_frame, Maze
from algorithms import depth_first_search_generation, prims_simple_generation, prims_cell_based_generation, kruskal_generation, right_wall_follower, dijkstra, a_star
from utils import analyze_algorithm

def run_maze_screen(visualize: bool = True):

    config.item_to_render = []

    maze = Maze(50, 50)

    results = analyze_algorithm(kruskal_generation, maze, visualize=False, delay=0.0)
    print(results)
    maze = results["result"]

    maze.clean_all()
    print(analyze_algorithm(dijkstra, maze, visualize=True, delay=0.00001))

    waiting = True
    while waiting:
        event_handler()
        if config.restart_run:
            config.restart_run = False
            waiting = False
