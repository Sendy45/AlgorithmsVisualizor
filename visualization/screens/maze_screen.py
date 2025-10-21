from visualization.elements.Cell import Cell
import pygame
import config
from visualization import event_handler, render_frame, Maze
from algorithms import depth_first_search, right_wall_follower

def run_maze_screen(visualize: bool = True):

    config.item_to_render = []

    maze = Maze(30, 30)

    depth_first_search(maze, visualize=False)
    maze.clean_all()
    right_wall_follower(maze, delay=0.001)

    waiting = True
    while waiting:
        event_handler()
        if config.restart_run:
            config.restart_run = False
            waiting = False
