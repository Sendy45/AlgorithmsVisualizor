import pygame
from random import shuffle
import time

pygame.init()
import config
from algorithms import ALGORITHMS
from visualization.Visualization import event_handler

# Wrapper function to analyze algorithm
# Counts operations, execution time, and returns result
def analyze_algorithm(func, arr: list, visualize: bool = True, delay: float = 0.02) -> dict:

    func(arr.copy(), visualize=visualize, delay=delay)

    # Time counting (measure performance without visualization)
    start_time = time.perf_counter()
    result = func(arr.copy(), visualize=False, delay=delay)
    end_time = time.perf_counter()

    return {
        "sorting algorithm": func.__name__,
        "result": result,  # sorted result
        "time": end_time - start_time,  # elapsed time
    }


# Generate random shuffled array
def random_array(length: int) -> list:
    arr = list(range(1, length + 1))
    shuffle(arr)
    return arr


def run_sort_visualizer(arr_length: int, algorithm_idx: int, visualize: bool = True, delay: float = 0.01):

    while True:  # loop until the user closes the window
        config.restart_run = False  # reset the restart flag
        config.arr_length %= config.SCREEN_WIDTH
        config.algorithm_idx %= len(ALGORITHMS)

        unsorted_arr = random_array(config.arr_length)

        # Run algorithm
        stats = analyze_algorithm(ALGORITHMS[config.algorithm_idx], unsorted_arr, visualize=visualize, delay=delay)
        print(stats["sorting algorithm"])
        print("time " + str(stats["time"]))
        print(stats["result"])

        # Wait for user input
        waiting = True
        while waiting:
            event_handler()
            if config.restart_run:
                waiting = False  # user pressed a key → exit wait and rerun


if __name__ == "__main__":

    run_sort_visualizer(config.arr_length, config.algorithm_idx, delay=config.delay)

    pygame.quit()