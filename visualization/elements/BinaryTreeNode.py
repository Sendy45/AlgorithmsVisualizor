from __future__ import annotations
from ..elements.TreeNode import TreeNode

class BinaryTreeNode(TreeNode):
    def __init__(self, value: int, highlighted: bool = False):
        super().__init__(value, highlighted)
        self._left: BinaryTreeNode | None = None
        self._right: BinaryTreeNode | None = None
        self.children: list[BinaryTreeNode] = []

    @property
    def left(self) -> BinaryTreeNode | None:
        return self._left

    @left.setter
    def left(self, node: BinaryTreeNode | None):
        self._left = node
        if node: node.parent = self
        self._update_children()

    @property
    def right(self) -> BinaryTreeNode | None:
        return self._right

    @right.setter
    def right(self, node: BinaryTreeNode | None):
        self._right = node
        if node: node.parent = self
        self._update_children()

    def _update_children(self) -> None:
        """Keep the children list consistent with left and right."""
        self.children = []
        if self._left is not None:
            self.children.append(self._left)
        if self._right is not None:
            self.children.append(self._right)
        self.update_layout()


    def find_min(self) -> BinaryTreeNode:
        if self.left:
            return self.left.find_min()
        return self