import pygame
from random import shuffle, randint
import time

from config import SCREEN_WIDTH
from visualization.TreeNode import TreeNode

import config
from algorithms import ALGORITHMS
from visualization.Visualization import event_handler, Column, DisplayText

# Wrapper function to analyze algorithm
# Counts operations, execution time, and returns result
def analyze_algorithm(func, arr: list, visualize: bool = True, delay: float = 0.02) -> dict:

    config.algorithm_name = func.__name__
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
def random_columns_array(length: int) -> list[Column]:
    columns = []
    for i in range(length):
        columns.append(Column(i, i + 1))
    shuffle(columns)
    return columns

def generate_random_tree(
    max_depth: int = 4,
    max_children: int = 3,
    value_range: tuple[int, int] = (1, 100)
) -> TreeNode:
    """
    Generates a random tree and returns the root TreeNode.
    """
    def create_node(depth: int) -> TreeNode:
        value = randint(*value_range)
        node = TreeNode(value=value)

        if depth < max_depth:
            num_children = randint(0, max_children)
            for _ in range(num_children):
                child = create_node(depth + 1)
                node.add_child(child)

        return node

    return create_node(0)

def run_sort_visualizer(visualize: bool = True):

    while True:  # loop until the user closes the window
        config.restart_run = False  # reset the restart flag
        config.arr_length %= config.SCREEN_WIDTH
        config.algorithm_idx %= len(ALGORITHMS)
        config.delay %= 0.01
        config.delay = round(config.delay, 5)

        unsorted_arr = random_columns_array(config.arr_length)

        # Run algorithm
        stats = analyze_algorithm(ALGORITHMS[config.algorithm_idx], unsorted_arr, visualize=visualize, delay=config.delay)
        print(stats["sorting algorithm"])
        print("time " + str(stats["time"]))

        nums_arr = []
        for col in stats["result"]:
            nums_arr.append(col.value)
        print(nums_arr)

        # Wait for user input
        waiting = True
        while waiting:
            event_handler()
            if config.restart_run:
                waiting = False  # user pressed a key → exit wait and rerun


if __name__ == "__main__":
    pygame.init()

    #run_sort_visualizer()

    while True:

        config.restart_run = False

        config.SCREEN.fill("black")

        root = generate_random_tree()

        root.print_tree()

        root.draw()

        pygame.display.flip()

        # Wait for user input
        waiting = True
        while waiting:
            event_handler()
            if config.restart_run:
                waiting = False  # user pressed a key → exit wait and rerun

    pygame.quit()
