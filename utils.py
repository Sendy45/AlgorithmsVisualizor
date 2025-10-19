from random import shuffle, randint
import time
from copy import deepcopy

from visualization import TreeNode, Column
import config

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
