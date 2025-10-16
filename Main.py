import sys

import pygame
from random import shuffle, randint
import time
from copy import deepcopy

from algorithms.bst_algorithms import *
from visualization import TreeNode, event_handler, Column, Button

import config
from algorithms import ALGORITHMS

# Wrapper function to analyze algorithm
# Counts operations, execution time, and returns result
def analyze_algorithm(func, data, *args, visualize: bool = True, delay: float = 0.02) -> dict:

    config.algorithm_name = func.__name__
    func(deepcopy(data), *args, visualize=visualize, delay=delay)

    # Time counting (measure performance without visualization)
    start_time = time.perf_counter()
    result = func(deepcopy(data), *args, visualize=False, delay=delay)
    end_time = time.perf_counter()

    return {
        "algorithm": func.__name__,
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
    max_depth: int = 5,
    max_children: int = 3,
    value_range: tuple[int, int] = (1, 100)
) -> TreeNode:

    def create_node(depth: int) -> TreeNode:
        value = randint(*value_range)
        node = TreeNode(value=value)

        if depth < max_depth:
            num_children = randint(1, max_children)
            for _ in range(num_children):
                child = create_node(depth + 1)
                node.add_child(child)

        return node

    return create_node(0)

def run_sort_visualizer(visualize: bool = True):

    config.item_to_render = []

    #TODO organize buttons outside of function

    increase_delay_btn = Button(
        (0, 0),
        "delay",
        action=lambda: (setattr(config, "delay", config.delay + 0.001), setattr(config, "restart_run", True))
    )

    next_algorithm_btn = Button(
        (80, 0),
        "next",
        action=lambda: (setattr(config, "algorithm_idx", config.algorithm_idx + 1), setattr(config, "restart_run", True))
    )

    arr_len_btn = Button(
        (160, 0),
        "length",
        action=lambda: (setattr(config, "arr_length", config.arr_length + 50),
                        setattr(config, "restart_run", True))
    )

    config.item_to_render.extend([increase_delay_btn, next_algorithm_btn, arr_len_btn])

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

def run_tree_visualizer(visualize: bool = True):

    root_container = [None]  # a list to store root
    config.item_to_render = []

    # TODO organize buttons outside of function

    bst_create_btn = Button(
        (0, 0),
        "create",
        action=lambda: root_container.__setitem__(0, analyze_algorithm(
            bst_create,
            list(range(1, 30, 3)),
            visualize=visualize,
            delay=0.5
        )["result"])
    )

    bst_insert_btn = Button(
        (80, 0),
        "insert",
        action=lambda: root_container.__setitem__(0, analyze_algorithm(
            bst_insert,
            root_container[0],
            5,
            visualize=visualize,
            delay=0.5
        )["result"])
    )

    bst_remove_btn = Button(
        (160, 0),
        "remove",
        action=lambda: root_container.__setitem__(0, analyze_algorithm(
            bst_remove,
            root_container[0],
            5,
            visualize=visualize,
            delay=0.5
        )["result"])
    )

    bst_traverse_postorder_btn = Button(
        (240, 0),
        "postorder",
        action=lambda: analyze_algorithm(
            bst_traverse_postorder,
            root_container[0],
            visualize=visualize,
            delay=0.5
        )
    )

    bst_traverse_preorder_btn = Button(
        (320, 0),
        "preorder",
        action=lambda: analyze_algorithm(
            bst_traverse_preorder,
            root_container[0],
            visualize=visualize,
            delay=0.5
        )
    )

    bst_traverse_inorder_btn = Button(
        (400, 0),
        "inorder",
        action=lambda: analyze_algorithm(
            bst_traverse_inorder,
            root_container[0],
            visualize=visualize,
            delay=0.5
        )
    )

    config.item_to_render.extend([bst_create_btn, bst_insert_btn, bst_remove_btn, bst_traverse_postorder_btn, bst_traverse_inorder_btn, bst_traverse_preorder_btn])

    while True:  # loop until the user closes the window
        config.restart_run = False  # reset the restart flag

        objects_to_draw = [root_container[0]] if root_container[0] else []
        render_frame(objects_to_draw, 0)

        event_handler()


if __name__ == "__main__":

    run_tree_visualizer()
    run_sort_visualizer()

    pygame.quit()