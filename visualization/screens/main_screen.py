import config
from visualization import Button, render_frame
from visualization.screens.sorting_screen import run_sort_screen
from visualization.screens.bst_screen import run_bst_screen

def run_main_screen(visualize: bool = True):
    config.item_to_render = []

    # TODO organize buttons outside of function

    bst_screen_btn = Button(
        (0, 0),
        "BST",
        action=lambda: run_bst_screen(visualize=visualize)
    )

    sort_screen_btn = Button(
        (80, 0),
        "SORT",
        action=lambda: run_sort_screen(visualize=visualize)
    )

    config.item_to_render.extend(
        [bst_screen_btn, sort_screen_btn])

    while True:  # loop until the user closes the window

        render_frame([], 0)