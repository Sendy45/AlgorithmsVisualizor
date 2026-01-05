import config
from visualization import Button, event_handler
from algorithms import ALGORITHMS
from utils import random_columns_array, analyze_algorithm


def run_sort_screen(visualize: bool = True):

    config.item_to_render = []

    increase_delay_btn = Button(
        (0, 0),
        "delay",
        action=lambda: (setattr(config, "delay", config.delay + 0.001), setattr(config, "restart_run", True))
    )

    next_algorithm_btn = Button(
        (0, 0),
        "next",
        action=lambda: (setattr(config, "algorithm_idx", config.algorithm_idx + 1), setattr(config, "restart_run", True))
    )

    arr_len_btn = Button(
        (0, 0),
        "length",
        action=lambda: (setattr(config, "arr_length", config.arr_length + 50),
                        setattr(config, "restart_run", True))
    )

    back_btn = Button(
        (0, 0),
        "back",
        action=lambda: __import__(
            "visualization.screens.main_screen",
            fromlist=["run_main_screen"]
        ).run_main_screen()
    )

    config.item_to_render.extend([back_btn, increase_delay_btn, next_algorithm_btn, arr_len_btn])

    start_x = 0
    h, w = 50, 80
    for item in config.item_to_render:
        item.set_height(h)
        item.set_width(w)
        item.set_position((start_x, 0))
        item.clip_to("top")
        start_x += w

    while True:  # loop until the user closes the window

        config.restart_run = False  # reset the restart flag

        #TODO make adjustments in config
        config.arr_length %= config.SCREEN_WIDTH
        config.algorithm_idx %= len(ALGORITHMS)
        config.delay %= 0.01
        config.delay = round(config.delay, 5)

        unsorted_arr = random_columns_array(config.arr_length)

        # run algorithm (can be stopped mid-way with restart_run)
        stats = analyze_algorithm(
            ALGORITHMS[config.algorithm_idx],
            unsorted_arr,
            visualize=visualize,
            delay=config.delay
        )

        print(stats["algorithm"])
        print("time " + str(stats["time"]))

        waiting = True
        while waiting:
            event_handler()
            if config.restart_run:
                config.restart_run = False
                waiting = False