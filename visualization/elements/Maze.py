import pygame
import config
from ..Drawable import Drawable
from ..elements.Cell import Cell

class Maze(Drawable):
    def __init__(self,rows: int, cols: int) -> None:
        super().__init__()
        self.rows = rows
        self.cols = cols
        self.cell_size = self.calc_cell_size()
        self.grid = [[Cell((r, c), self.cell_size) for c in range(cols)] for r in range(rows)]

    def calc_cell_size(self) -> int:
        side_x = config.SCREEN_WIDTH / self.cols
        side_y = config.SCREEN_HEIGHT / self.rows
        return int(min(side_x, side_y))

    def get_cell(self, r: int, c: int) -> Cell | None:
        if 0 <= r < self.rows and 0 <= c < self.cols:
            return self.grid[r][c]
        return None

    def draw(self) -> None:
        for row in self.grid:
            for cell in row:
                cell.draw()

    def get_neighbors(self, cell: Cell | tuple[int, int]) -> list[Cell]:

        if not isinstance(cell, Cell):
            cell = Cell(cell) # Turn tuple position into cell type

        neighbors = []
        for direction in range(4): # TOP, RIGHT, BOTTOM, LEFT = range(4)
            neighbor = self.get_next_cell(cell, direction)
            if neighbor:
                neighbors.append(neighbor)

        return neighbors

    def navigable_neighbors(self, cell: Cell | tuple[int, int]) -> list[Cell]:
        if not isinstance(cell, Cell):
            cell = Cell(cell) # Turn tuple position into cell type

        neighbors = []
        for direction in range(4):  # TOP, RIGHT, BOTTOM, LEFT = range(4)
            neighbor = self.get_next_cell(cell, direction)
            if neighbor and not cell.walls[direction]: # Check if exists and navigable
                neighbors.append(neighbor)

        return neighbors


    def get_next_cell(self, cell: Cell, direction: int) -> Cell | None:
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

    def all_cells(self) -> list[Cell]:
        cells = []
        for row in self.grid:
            cells.extend(row)
        return cells