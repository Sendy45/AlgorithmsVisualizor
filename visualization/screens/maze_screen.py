from visualization.elements.Cell import Cell
import pygame
import config
from visualization import event_handler, render_frame, Maze
from algorithms import depth_first_search_generation, prims_simple_generation, prims_cell_based_generation,right_wall_follower
from utils import analyze_algorithm

def run_maze_screen(visualize: bool = True):

    config.item_to_render = []

    maze = Maze(100, 100)

    prims_cell_based_generation(maze, visualize=False, delay=0)
    maze.clean_all()
    print(analyze_algorithm(right_wall_follower, maze, visualize=True, delay=0.01))

    waiting = True
    while waiting:
        event_handler()
        if config.restart_run:
            config.restart_run = False
            waiting = False
