import pygame
from random import shuffle
import time
pygame.init()
from config import *
from algorithms import ALGORITHMS

# Wrapper function to analyze algorithm
# Counts operations, execution time, and returns result
def analyze_algorithm(func, arr: list, visualize: bool = True, delay: float = 0.02) -> dict:

    # Run algorithm once (with visualization, if enabled)
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
    arr_length %= SCREEN_WIDTH # Prevent more columns than pixels on screen
    unsorted_arr = random_array(arr_length)  # create random array

    # analyze heap_sort
    stats = analyze_algorithm(ALGORITHMS[algorithm_idx], unsorted_arr, visualize = visualize, delay=delay)
    print(stats["sorting algorithm"])
    print("time " + str(stats["time"]))
    print(stats["result"])

    # event loop (keeps window open until closed)
    running = True
    while running:
        # wait for event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    arr_length += 100
                    run_sort_visualizer(arr_length, algorithm_idx)
                elif event.key == pygame.K_DOWN:
                    arr_length -= 100
                    run_sort_visualizer(arr_length, algorithm_idx)
                elif event.key == pygame.K_RIGHT:
                    algorithm_idx += 1
                    algorithm_idx %= len(ALGORITHMS)
                    run_sort_visualizer(arr_length, algorithm_idx)
                elif event.key == pygame.K_LEFT:
                    algorithm_idx -= 1
                    algorithm_idx %= len(ALGORITHMS)
                    run_sort_visualizer(arr_length, algorithm_idx)


if __name__ == "__main__":

    arr_length = 100
    algorithm_idx = -1

    run_sort_visualizer(arr_length, algorithm_idx)

    pygame.quit()