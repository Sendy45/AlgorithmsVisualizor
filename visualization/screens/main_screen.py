import config
from visualization import Button, render_frame
from .sorting_screen import run_sort_screen
from .bst_screen import run_bst_screen
from .maze_screen import run_maze_screen

def run_main_screen(visualize: bool = True):
    config.item_to_render = []

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

    maze_screen_btn = Button(
        (160, 0),
        "MAZE",
        action=lambda: run_maze_screen(visualize=visualize)
    )

    config.item_to_render.extend(
        [bst_screen_btn, sort_screen_btn, maze_screen_btn])

    while True:  # loop until the user closes the window

        render_frame([], 0)