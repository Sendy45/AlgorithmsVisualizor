from visualization.elements.Cell import Cell
import pygame
import config
from visualization import event_handler, render_frame, Maze, Button, InputBox
from algorithms import depth_first_search_generation, prims_simple_generation, prims_cell_based_generation, kruskal_generation, right_wall_follower, dijkstra, a_star, dead_end_filling
from utils import analyze_algorithm

def run_maze_screen(visualize: bool = True):

    maze_container: list[Maze | None] = [None] # a list to store maze
    n = 20
    delay = 0.0001

    maze_container[0] = Maze(n, n)

    config.item_to_render = []

    # TODO organize buttons outside of function

    x = config.SCREEN_WIDTH - 80

    input_number = InputBox(
        (x, 400),
        ""
    )

    def run_algorithm_button(algorithm_func, maze_container: list[Maze | None], visualize: bool = True,
                             delay: float = 0.02, update: bool = False):
        """
        Runs an algorithm on the maze and updates maze_container.

        algorithm_func: the algorithm function to run
        maze_container: a list containing the current maze or None
        n: size of the maze
        visualize: whether to show the visualization
        delay: delay between frames for visualization
        clean: whether to call clean_all() before running
        """
        # Stop any previous run
        setattr(config, "restart_run", True)
        setattr(config, "restart_run", False)

        # Update maze with a new one
        if update:
            new_n = int(input_number.value) if input_number.value.isnumeric() else n
            maze_container[0] = Maze(new_n, new_n)

        if isinstance(maze_container[0], Maze):
            maze_container[0].clean_all()

        # Run the algorithm
        result = analyze_algorithm(
            algorithm_func,
            maze_container[0],
            visualize=visualize,
            delay=delay
        )["result"]

        # Update the maze_container only if the algorithm finished properly
        if result is not None:
            maze_container[0] = result

        # Trigger re-render
        setattr(config, "restart_run", True)

    dfs_create_btn = Button(
        (x, 0),
        "dfs",
        action=lambda: run_algorithm_button(depth_first_search_generation, maze_container, visualize=False, delay=delay, update=True)
    )

    prims_simple_create_btn = Button(
        (x, 50),
        "prims_simple",
        action=lambda: run_algorithm_button(prims_simple_generation, maze_container, visualize=False, delay=delay, update=True)
    )

    prims_cell_create_btn = Button(
        (x, 100),
        "prims_cell",
        action=lambda: run_algorithm_button(prims_cell_based_generation, maze_container, visualize=False, delay=delay, update=True)
    )

    kruskal_create_btn = Button(
        (x, 150),
        "kruskal",
        action=lambda: run_algorithm_button(kruskal_generation, maze_container, visualize=False, delay=delay, update=True)
    )

    a_star_solve_btn = Button(
        (x, 200),
        "A*",
        action=lambda: run_algorithm_button(a_star, maze_container, visualize=visualize, delay=delay)
    )

    dijkstra_solve_btn = Button(
        (x, 250),
        "dijkstra",
        action=lambda: run_algorithm_button(dijkstra, maze_container, visualize=visualize, delay=delay)

    )

    dead_end_filling_solve_btn = Button(
        (x, 300),
        "dead_end",
        action=lambda: run_algorithm_button(dead_end_filling, maze_container, visualize=visualize, delay=delay)

    )

    wall_follower_solve_btn = Button(
        (x, 350),
        "follower",
        action=lambda: run_algorithm_button(right_wall_follower, maze_container, visualize=visualize, delay=delay)

    )

    config.item_to_render.extend([dfs_create_btn, prims_simple_create_btn, prims_cell_create_btn, kruskal_create_btn, a_star_solve_btn, dijkstra_solve_btn, dead_end_filling_solve_btn, wall_follower_solve_btn, input_number])

    while True:  # loop until the user closes the window

        config.restart_run = False  # reset the restart flag

        waiting = True
        while waiting:
            event_handler()

            objects_to_draw = [maze_container[0]] if maze_container[0] else []
            render_frame(objects_to_draw, 0)
            if config.restart_run:
                config.restart_run = False
                waiting = False