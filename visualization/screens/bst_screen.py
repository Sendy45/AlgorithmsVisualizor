import config
from algorithms.bst_algorithms import *
from visualization import Button, InputBox
from utils import analyze_algorithm

def run_bst_screen(visualize: bool = True):

    root: BinaryTreeNode | None = None  # a list to store root
    config.item_to_render = []

    # TODO organize buttons outside of function

    n = 0

    input_number = InputBox(
        (0, 0),
        ""
    )

    # Runs an algorithm on the maze and updates maze_container
    def run_algorithm_button(algorithm_func, data, *args, visualize: bool = True):

        nonlocal root

        # Run the algorithm
        results = analyze_algorithm(
            algorithm_func,
            data,
            *args,
            visualize=visualize,
            delay=0.5
        )

        # Update the root only if the algorithm finished properly and returned root
        if results["result"] is not None and isinstance(results["result"], BinaryTreeNode):
            root = results["result"]
            print(results)

        # Trigger re-render
        config.restart_run = True

    bst_create_btn = Button(
        (0, 0),
        "create",
        action=lambda: run_algorithm_button(bst_create, list(range(1, 30, 3)))
    )

    bst_insert_btn = Button(
        (0, 0),
        "insert",
        action=lambda: run_algorithm_button(bst_insert, root, n, visualize=visualize)
    )

    bst_remove_btn = Button(
        (0, 0),
        "remove",
        action=lambda: run_algorithm_button(bst_remove, root,n, visualize=visualize)
    )

    bst_traverse_postorder_btn = Button(
        (0, 0),
        "postorder",
        action=lambda: run_algorithm_button(bst_traverse_postorder, root, visualize=visualize)
    )

    bst_traverse_preorder_btn = Button(
        (0, 0),
        "preorder",
        action=lambda: run_algorithm_button(bst_traverse_preorder, root, visualize=visualize)
    )

    bst_traverse_inorder_btn = Button(
        (0, 0),
        "inorder",
        action=lambda: run_algorithm_button(bst_traverse_inorder, root, visualize=visualize)
    )

    back_btn = Button(
        (0, 0),
        "back",
        action=lambda: __import__(
            "visualization.screens.main_screen",
            fromlist=["run_main_screen"]
        ).run_main_screen()
    )

    config.item_to_render.extend([back_btn, bst_create_btn, bst_insert_btn, bst_remove_btn, bst_traverse_postorder_btn, bst_traverse_inorder_btn, bst_traverse_preorder_btn, input_number])

    start_y = 0
    h, w = 50, 90
    for item in config.item_to_render:
        item.set_height(h)
        item.set_width(w)
        item.set_position((0, start_y))
        item.clip_to("right")
        start_y += h

    while True:  # loop until the user closes the window
        config.restart_run = False  # reset the restart flag

        n = int(input_number.value) if input_number.value.isnumeric() else n

        objects_to_draw = [root] if root else []
        render_frame(objects_to_draw, 0)