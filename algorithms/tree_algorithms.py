from visualization import render_frame, BinaryTreeNode

def binary_search_tree(arr: list[int]) -> BinaryTreeNode | None:
    if not arr:
        return None
    mid = len(arr) // 2
    node = BinaryTreeNode(arr[mid])
    node.left = binary_search_tree(arr[:mid])
    node.right = binary_search_tree(arr[mid + 1:])
    return node


def add_to_binary_tree(root: BinaryTreeNode | None, num: int) -> BinaryTreeNode:
    if root is None:
        return BinaryTreeNode(num)

    if num < root.value:
        root.left = add_to_binary_tree(root.left, num)
    elif num > root.value:
        root.right = add_to_binary_tree(root.right, num)

    return root






