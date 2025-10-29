from .sorting_algorithms import (
    bubble_sort,
    selection_sort,
    insertion_sort,
    merge_sort,
    heap_sort,
    quick_sort,
    counting_sort,
    radix_sort,
    cocktail_shaker_sort,
    shell_sort,
    bucket_sort,
    comb_sort
)

from .bst_algorithms import (
    bst_create,
    bst_search,
    bst_insert,
    bst_remove,
    bst_traverse_inorder,
    bst_traverse_preorder,
    bst_traverse_postorder
)

from .maze_algorithms import (
    depth_first_search_generation,
    prims_cell_based_generation,
    prims_simple_generation,
    right_wall_follower,
    dijkstra
)

ALGORITHMS = [
    bubble_sort,
    selection_sort,
    insertion_sort,
    merge_sort,
    quick_sort,
    heap_sort,
    counting_sort,
    radix_sort,
    cocktail_shaker_sort,
    shell_sort,
    bucket_sort,
    comb_sort
]

__all__ = [
    "bubble_sort",
    "selection_sort",
    "insertion_sort",
    "merge_sort",
    "heap_sort",
    "quick_sort",
    "counting_sort",
    "radix_sort",
    "cocktail_shaker_sort",
    "shell_sort",
    "bucket_sort",
    "comb_sort",
    "ALGORITHMS",
    "bst_create",
    "bst_search",
    "bst_insert",
    "bst_remove",
    "bst_traverse_inorder",
    "bst_traverse_preorder",
    "bst_traverse_postorder",
    "depth_first_search_generation",
    "prims_cell_based_generation",
    "prims_simple_generation",
    "dijkstra",
    "right_wall_follower"
]
