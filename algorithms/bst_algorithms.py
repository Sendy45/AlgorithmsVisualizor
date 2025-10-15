from visualization import render_frame, BinaryTreeNode

def bst_create(arr: list[int]) -> BinaryTreeNode | None:
    if not arr:
        return None
    mid = len(arr) // 2
    node = BinaryTreeNode(arr[mid])
    node.left = bst_create(arr[:mid])
    node.right = bst_create(arr[mid + 1:])

    return node


def bst_insert(node: BinaryTreeNode | None, num: int, visualize: bool, delay: float) -> BinaryTreeNode:
    if node is None:
        return BinaryTreeNode(num, highlighted=visualize)

    if visualize:
        node.highlight()
        render_frame([node.get_root()], delay)

    if num < node.value:
        node.left = bst_insert(node.left, num, visualize, delay)
    elif num > node.value:
        node.right = bst_insert(node.right, num, visualize, delay)

    # one last render only when insertion is completed
    if visualize and node.get_root() == node:
        render_frame([node], delay)

    return node


def bst_remove(node: BinaryTreeNode | None, num: int, visualize: bool, delay: float) -> BinaryTreeNode | None:
    if node is None:
        return None

    if visualize:
        node.highlight()
        render_frame([node.get_root()], delay)

    if num == node.value:
        if not node.children:
            return None
        elif len(node.children) == 1:
            return node.children[0]
        else:
            node.value = node.right.find_min().value
            node.right = bst_remove(node.right, node.value, visualize, delay)

    elif num < node.value:
        node.left = bst_remove(node.left, num, visualize, delay)
    elif num > node.value:
        node.right = bst_remove(node.right, num, visualize, delay)

    # one last render only when deletion is completed
    if visualize and node and node.get_root() == node:
        render_frame([node], delay)

    return node


def bst_search(node: BinaryTreeNode | None, num: int, visualize: bool, delay: float) -> BinaryTreeNode | None:
    if node is None:
        return None

    if visualize:
        node.highlight()
        render_frame([node.get_root()], delay)

    if num == node.value:
        return node
    if num < node.value:
        node = bst_search(node.left, num, visualize, delay)
    elif num > node.value:
        node = bst_search(node.right, num, visualize, delay)

    # one last render only when insertion is completed
    if visualize and node and node.get_root() == node:
        render_frame([node], delay)

    return node


def bst_traverse_inorder(node: BinaryTreeNode | None, visualize: bool, delay: float) -> list[int]:
    if node is None:
        return []

    left = bst_traverse_inorder(node.left, visualize, delay)

    if visualize:
        node.highlight()
        render_frame([node.get_root()], delay)

    right = bst_traverse_inorder(node.right, visualize, delay)

    return left + [node.value] + right


def bst_traverse_preorder(node: BinaryTreeNode | None, visualize: bool, delay: float) -> list[int]:
    if node is None:
        return []

    if visualize:
        node.highlight()
        render_frame([node.get_root()], delay)

    left = bst_traverse_preorder(node.left, visualize, delay)

    right = bst_traverse_preorder(node.right, visualize, delay)

    return [node.value] + left + right


def bst_traverse_postorder(node: BinaryTreeNode | None, visualize: bool, delay: float) -> list[int]:
    if node is None:
        return []

    left = bst_traverse_postorder(node.left, visualize, delay)

    right = bst_traverse_postorder(node.right, visualize, delay)

    if visualize:
        node.highlight()
        render_frame([node.get_root()], delay)

    return left + right + [node.value]


