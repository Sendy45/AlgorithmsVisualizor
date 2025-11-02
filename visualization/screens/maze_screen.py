from visualization.elements.Cell import Cell
import pygame
import config
from visualization import event_handler, render_frame, Maze, Button
from algorithms import depth_first_search_generation, prims_simple_generation, prims_cell_based_generation, kruskal_generation, right_wall_follower, dijkstra, a_star, dead_end_filling
from utils import analyze_algorithm

def run_maze_screen(visualize: bool = True):

    maze_container = [None] # a list to store maze
    n = 40
    delay = 0.001

    config.item_to_render = []

    # TODO organize buttons outside of function

    x = config.SCREEN_WIDTH - 80

    dfs_create_btn = Button(
        (x, 0),
        "dfs",
        action=lambda: (maze_container.__setitem__(0, Maze(n, n)),
            maze_container.__setitem__(0, analyze_algorithm(
            depth_first_search_generation,
            maze_container[0],
            visualize=visualize,
            delay=delay
        )["result"]), setattr(config, "restart_run", True))
    )

    prims_simple_create_btn = Button(
        (x, 50),
        "prims_simple",
        action=lambda: (maze_container.__setitem__(0, Maze(n, n)),
                        maze_container.__setitem__(0, analyze_algorithm(
                            prims_simple_generation,
                            maze_container[0],
                            visualize=visualize,
                            delay=delay
                        )["result"]), setattr(config, "restart_run", True))
    )

    prims_cell_create_btn = Button(
        (x, 100),
        "prims_cell",
        action=lambda: (maze_container.__setitem__(0, Maze(n, n)),
                        maze_container.__setitem__(0, analyze_algorithm(
                            prims_cell_based_generation,
                            maze_container[0],
                            visualize=visualize,
                            delay=delay
                        )["result"]), setattr(config, "restart_run", True))
    )

    kruskal_create_btn = Button(
        (x, 150),
        "kruskal",
        action=lambda: (maze_container.__setitem__(0, Maze(n, n)),
                        maze_container.__setitem__(0, analyze_algorithm(
                            kruskal_generation,
                            maze_container[0],
                            visualize=visualize,
                            delay=delay
                        )["result"]), setattr(config, "restart_run", True))
    )

    a_star_solve_btn = Button(
        (x, 200),
        "A*",
        action=lambda: (maze_container.__setitem__(0, analyze_algorithm(
                            a_star,
                            maze_container[0],
                            visualize=visualize,
                            delay=delay
                        )["result"]), setattr(config, "restart_run", True))
    )

    dijkstra_solve_btn = Button(
        (x, 250),
        "dijkstra",
        action=lambda: (maze_container.__setitem__(0, analyze_algorithm(
            dijkstra,
            maze_container[0],
            visualize=visualize,
            delay=delay
        )["result"]), setattr(config, "restart_run", True))
    )

    dead_end_filling_solve_btn = Button(
        (x, 300),
        "dead_end",
        action=lambda: (maze_container.__setitem__(0, analyze_algorithm(
            dead_end_filling,
            maze_container[0],
            visualize=visualize,
            delay=delay
        )["result"]), setattr(config, "restart_run", True))
    )

    wall_follower_solve_btn = Button(
        (x, 350),
        "follower",
        action=lambda: (maze_container.__setitem__(0, analyze_algorithm(
            right_wall_follower,
            maze_container[0],
            visualize=visualize,
            delay=delay
        )["result"]), setattr(config, "restart_run", True))
    )

    config.item_to_render.extend([dfs_create_btn, prims_simple_create_btn, prims_cell_create_btn, kruskal_create_btn, a_star_solve_btn, dijkstra_solve_btn, dead_end_filling_solve_btn, wall_follower_solve_btn])

    while True:  # loop until the user closes the window

        config.restart_run = False  # reset the restart flag

        objects_to_draw = [maze_container[0]] if maze_container[0] else []
        render_frame(objects_to_draw, 0)

        waiting = True
        while waiting:
            event_handler()
            if config.restart_run:
                config.restart_run = False
                waiting = False
                if isinstance(maze_container[0], Maze):
                    maze_container[0].clean_all()
