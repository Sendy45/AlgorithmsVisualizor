import config
from visualization import event_handler, render_frame, Maze, Button, InputBox
from algorithms import depth_first_search_generation, prims_simple_generation, prims_cell_based_generation, kruskal_generation, right_wall_follower, dijkstra, a_star, dead_end_filling
from utils import analyze_algorithm


def run_maze_screen(visualize: bool = True):

    n = 20 # default maze size
    delay = 0.0001

    maze_container: list[Maze] = [Maze(n, n)]  # a list to store maze

    config.item_to_render = []

    x = config.SCREEN_WIDTH - 80

    input_number = InputBox(
        (x, 400),
        ""
    )

    # Runs an algorithm on the maze and updates maze_container
    def run_algorithm_button(algorithm_func, maze_container: list[Maze | None], visualize: bool = True,
                             delay: float = 0.02, update: bool = False):

        # Update maze with a new one
        if update:
            new_n = int(input_number.value) if input_number.value.isnumeric() else n
            maze_container[0] = Maze(new_n, new_n)

        if isinstance(maze_container[0], Maze):
            maze_container[0].clean_all()

        # Run the algorithm
        results = analyze_algorithm(
            algorithm_func,
            maze_container[0],
            visualize=visualize,
            delay=delay
        )

        # Update the maze_container only if the algorithm finished properly
        if results["result"] is not None:
            maze_container[0] = results["result"]
            print(results)

        # Trigger re-render
        config.restart_run = True

    dfs_create_btn = Button(
        (0, 0),
        "dfs",
        action=lambda: run_algorithm_button(depth_first_search_generation, maze_container, visualize=False, delay=delay, update=True)
    )

    prims_simple_create_btn = Button(
        (0, 0),
        "prims_simple",
        action=lambda: run_algorithm_button(prims_simple_generation, maze_container, visualize=False, delay=delay, update=True)
    )

    prims_cell_create_btn = Button(
        (0, 0),
        "prims_cell",
        action=lambda: run_algorithm_button(prims_cell_based_generation, maze_container, visualize=False, delay=delay, update=True)
    )

    kruskal_create_btn = Button(
        (0, 0),
        "kruskal",
        action=lambda: run_algorithm_button(kruskal_generation, maze_container, visualize=False, delay=delay, update=True)
    )

    a_star_solve_btn = Button(
        (0, 0),
        "A*",
        action=lambda: run_algorithm_button(a_star, maze_container, visualize=visualize, delay=delay)
    )

    dijkstra_solve_btn = Button(
        (0, 0),
        "dijkstra",
        action=lambda: run_algorithm_button(dijkstra, maze_container, visualize=visualize, delay=delay)

    )

    dead_end_filling_solve_btn = Button(
        (0, 0),
        "dead_end",
        action=lambda: run_algorithm_button(dead_end_filling, maze_container, visualize=visualize, delay=delay)

    )

    wall_follower_solve_btn = Button(
        (0, 0),
        "follower",
        action=lambda: run_algorithm_button(right_wall_follower, maze_container, visualize=visualize, delay=delay)
    )

    back_btn = Button(
        (0, 0),
        "back",
        action=lambda: __import__(
            "visualization.screens.main_screen",
            fromlist=["run_main_screen"]
        ).run_main_screen()
    )

    config.item_to_render.extend([back_btn, dfs_create_btn, prims_simple_create_btn, prims_cell_create_btn, kruskal_create_btn, a_star_solve_btn, dijkstra_solve_btn, dead_end_filling_solve_btn, wall_follower_solve_btn, input_number])

    start_y = 0
    h, w = 80, 120
    for item in config.item_to_render:
        item.set_height(h)
        item.set_width(w)
        item.set_position((0, start_y))
        item.clip_to("right")
        start_y += h

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