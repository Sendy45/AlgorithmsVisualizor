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


    def get_neighbors(self, cell: Cell | tuple[int, int]) -> list[Cell] | None:

        if isinstance(cell, Cell):
            r, c = cell.row, cell.col
        else:
            r, c = cell

        if not (0 <= r < self.rows and 0 <= c < self.cols):
            return None

        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # directions (right, left, down, up)
        neighbors = []
        for dx, dy in dirs:
            neighbor = self.get_cell(r + dx, c + dy)
            if neighbor:
                neighbors.append(neighbor)

        return neighbors