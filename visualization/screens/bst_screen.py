import config
from algorithms.bst_algorithms import *
from visualization import Button, InputBox
from utils import analyze_algorithm

def run_bst_screen(visualize: bool = True):

    root_container = [None]  # a list to store root
    config.item_to_render = []

    # TODO organize buttons outside of function

    n = 0

    input_number = InputBox(
        (0, 80),
        ""
    )

    bst_create_btn = Button(
        (0, 0),
        "create",
        action=lambda: (root_container.__setitem__(0, analyze_algorithm(
            bst_create,
            list(range(1, 30, 3)),
            visualize=visualize,
            delay=0.5
        )["result"]), setattr(config, "restart_run", True))
    )

    bst_insert_btn = Button(
        (80, 0),
        "insert",
        action=lambda: (root_container.__setitem__(0, analyze_algorithm(
            bst_insert,
            root_container[0],
            n,
            visualize=visualize,
            delay=0.5
        )["result"]), setattr(config, "restart_run", True))
    )

    bst_remove_btn = Button(
        (160, 0),
        "remove",
        action=lambda: (root_container.__setitem__(0, analyze_algorithm(
            bst_remove,
            root_container[0],
            n,
            visualize=visualize,
            delay=0.5
        )["result"]), setattr(config, "restart_run", True))
    )

    bst_traverse_postorder_btn = Button(
        (240, 0),
        "postorder",
        action=lambda: (analyze_algorithm(
            bst_traverse_postorder,
            root_container[0],
            visualize=visualize,
            delay=0.5
        ), setattr(config, "restart_run", True))
    )

    bst_traverse_preorder_btn = Button(
        (320, 0),
        "preorder",
        action=lambda: (analyze_algorithm(
            bst_traverse_preorder,
            root_container[0],
            visualize=visualize,
            delay=0.5
        ), setattr(config, "restart_run", True))
    )

    bst_traverse_inorder_btn = Button(
        (400, 0),
        "inorder",
        action=lambda: (analyze_algorithm(
            bst_traverse_inorder,
            root_container[0],
            visualize=visualize,
            delay=0.5
        ), setattr(config, "restart_run", True))
    )



    config.item_to_render.extend([bst_create_btn, bst_insert_btn, bst_remove_btn, bst_traverse_postorder_btn, bst_traverse_inorder_btn, bst_traverse_preorder_btn, input_number])

    while True:  # loop until the user closes the window
        config.restart_run = False  # reset the restart flag

        n = int(input_number.value) if input_number.value.isnumeric() else n

        objects_to_draw = [root_container[0]] if root_container[0] else []
        render_frame(objects_to_draw, 0)