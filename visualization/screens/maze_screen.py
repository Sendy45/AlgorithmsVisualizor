from visualization.elements.Cell import Cell
import pygame
import config
from visualization import event_handler, render_frame, Maze
from algorithms import depth_first_search

def run_maze_screen(visualize: bool = True):

    config.item_to_render = []

    maze = Maze(20, 20)

    maze = depth_first_search(maze, delay=0.01)

    waiting = True
    while waiting:
        event_handler()
        if config.restart_run:
            config.restart_run = False
            waiting = False
