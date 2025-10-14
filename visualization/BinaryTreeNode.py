from __future__ import annotations
from visualization import TreeNode

class BinaryTreeNode(TreeNode):
    def __init__(self, value: int):
        super().__init__(value)
        self._left: BinaryTreeNode | None = None
        self._right: BinaryTreeNode | None = None
        self.children: list[BinaryTreeNode] = []

    @property
    def left(self) -> BinaryTreeNode | None:
        return self._left

    @left.setter
    def left(self, node: BinaryTreeNode | None):
        self._left = node
        self._update_children()

    @property
    def right(self) -> BinaryTreeNode | None:
        return self._right

    @right.setter
    def right(self, node: BinaryTreeNode | None):
        self._right = node
        self._update_children()

    def _update_children(self) -> None:
        """Keep the children list consistent with left and right."""
        self.children = []
        if self._left is not None:
            self.children.append(self._left)
        if self._right is not None:
            self.children.append(self._right)
        self.update_layout()

    def copy(self) -> BinaryTreeNode:
        copy_node = BinaryTreeNode(self.value)
        copy_node.left = self.left.copy() if self.left is not None else None
        copy_node.right = self.right.copy() if self.right is not None else None
        copy_node.position = self.position
        copy_node.children = self.children
        copy_node.parent = self.parent
        copy_node.update_layout()
        return copy_node
