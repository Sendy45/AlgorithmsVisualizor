from collections import defaultdict
import pygame

from config import SCREEN_HEIGHT, SCREEN_WIDTH, default_color
from visualization import Drawable, DisplayText, Arrow
import config

class TreeNode(Drawable):
    r = 100
    def __init__(self, value: int = 0, highlighted: bool = False):
        super().__init__(0, value, highlighted)
        self.children = []
        self.parent = None
        self.update_layout()

    def add_child(self, child):
        child.parent = self
        self.children.append(child)
        self.get_root().update_layout()

    def update_layout(self):
        root = self.get_root()

        # depths and leaves of the whole tree
        depth = root.max_depth() + 1                # number of levels
        total_leaves = root.compute_leaves()

        # determine spacing: leave some margin on left/right/top/bottom
        margin_x = SCREEN_WIDTH // 16
        margin_y = SCREEN_HEIGHT // 12

        width_available = max(1, config.SCREEN_WIDTH - 2 * margin_x)
        height_available = max(1, config.SCREEN_HEIGHT - 2 * margin_y)

        # horizontal spacing per leaf; ensure at least some minimal spacing
        x_spacing = width_available / max(1, total_leaves)
        y_spacing = height_available / max(1, depth + 1)

        # choose radius proportionally (avoid overlap with spacing)
        TreeNode.r = int(min(x_spacing, y_spacing) * 0.25)

        # leftmost x baseline for first leaf
        left_baseline = margin_x

        # assign x positions by doing left-to-right order for leaves.
        # Use closure to keep next_x counter.
        next_x = [0]  # number of leaves placed so far

        def assign_positions(node: TreeNode, level: int):
            if not node.children:
                # leaf -> assign sequential x
                x = left_baseline + next_x[0] * x_spacing
                next_x[0] += 1
                node.position = (x, margin_y + level * y_spacing)
                return node.position
            else:
                child_xs = []
                for ch in node.children:
                    ch_pos = assign_positions(ch, level + 1)
                    child_xs.append(ch_pos[0])
                # center parent above its children
                x_center = sum(child_xs) / len(child_xs)
                node.position = (x_center, margin_y + level * y_spacing)
                return node.position

        # start assignment from root (level 0)
        assign_positions(root, 0)

    def compute_leaves(self) -> int:
        if not self.children:
            return 1
        return sum(child.compute_leaves() for child in self.children)

    def print_tree(self):
        prefix = "-"
        print(f"{prefix*self.get_level()}value = {self.value}")
        for child in self.children:
            child.print_tree()

    def get_level(self) -> int:
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def max_depth(self) -> int:
        if self is None:
            return 0
        max_depth = 0
        for child in self.children:
            if child.max_depth() > max_depth:
                max_depth = child.max_depth()

        return max_depth + 1

    def max_width(self) -> int:
        level_counts = defaultdict(int)

        def dfs(node: TreeNode, level: int):
            level_counts[level] += 1
            for child in node.children:
                dfs(child, level + 1)

        dfs(self, 0)  # start at root, level 0
        return max(level_counts.values()) if level_counts else 0

    def get_root(self):
        if self.parent:
            return self.parent.get_root()
        else:
            return self

    def draw(self) -> None:
        pygame.draw.circle(config.SCREEN, self.color, self.position, TreeNode.r)
        DisplayText(self.position,
                    str(self.value),
                    font_size=int(TreeNode.r * 1.5)
        ).draw()

        for child in self.children:
            Arrow(self.position, child.position, padding=TreeNode.r).draw()
            child.draw()


    def unhighlight_all(self) -> None:
        self.unhighlight()
        for child in self.children:
            child.unhighlight_all()