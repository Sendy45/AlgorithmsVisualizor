import pygame
import config
from ..Drawable import Drawable
from ..elements.Cell import Cell

class Maze(Drawable):
    def __init__(self,rows: int, cols: int) -> None:
        super().__init__()
        self.rows = rows
        self.cols = cols
        self.grid = [[Cell((r, c)) for c in range(cols)] for r in range(rows)]


    def get_cell(self, r: int, c: int) -> Cell | None:
        if 0 <= r < self.rows and 0 <= c < self.cols:
            return self.grid[r][c]
        return None


    def draw(self) -> None:
        for row in self.grid:
            for cell in row:
                cell.draw()


    def get_neighbors(self, cell: Cell | tuple[int, int]) -> list[Cell]:

        if isinstance(cell, Cell):
            r, c = cell.row, cell.col
        else:
            r, c = cell

        dirs = [(-1,0),(0,1),(1,0),(0,-1)]  # directions (TOP, RIGHT, BOTTOM, LEFT)
        neighbors = []
        for dx, dy in dirs:
            neighbor = self.get_cell(r + dx, c + dy)
            if neighbor:
                neighbors.append(neighbor)

        return neighbors

    def get_next_cell(self, cell: Cell, direction: int) -> Cell | None:
        """
        Get the neighboring cell in a specific direction (TOP, RIGHT, BOTTOM, LEFT).
        Returns None if that neighbor doesn't exist (out of bounds).
        """
        TOP, RIGHT, BOTTOM, LEFT = range(4)
        row, col = cell.row, cell.col

        if direction == TOP:
            row -= 1
        elif direction == RIGHT:
            col += 1
        elif direction == BOTTOM:
            row += 1
        elif direction == LEFT:
            col -= 1

        # return None if out of bounds
        if 0 <= row < self.rows and 0 <= col < self.cols:
            return self.get_cell(row, col)
        return None

    def clean_all(self):
        for row in self.grid:
            for cell in row:
                cell.visited = False