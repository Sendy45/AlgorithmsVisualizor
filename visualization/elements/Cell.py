from __future__ import annotations
import pygame
import config
from ..Drawable import Drawable

class Cell(Drawable):
    def __init__(self, position: tuple[int, int]):
        super().__init__(position)
        self.row = position[0]
        self.col = position[1]
        self.walls = [True] * 4
        self.visited = False

    def draw(self) -> None:
        x = self.col * 20  # horizontal
        y = self.row * 20  # vertical

        if self.visited:
            pygame.draw.rect(config.SCREEN, (150, 255, 150), pygame.Rect(x, y, 20, 20))

        if self.walls[0]:  # TOP
            pygame.draw.line(config.SCREEN, self.color, (x, y), (x + 20, y), 4)
        if self.walls[1]:  # RIGHT
            pygame.draw.line(config.SCREEN, self.color, (x + 20, y), (x + 20, y + 20), 4)
        if self.walls[2]:  # BOTTOM
            pygame.draw.line(config.SCREEN, self.color, (x + 20, y + 20), (x, y + 20), 4)
        if self.walls[3]:  # LEFT
            pygame.draw.line(config.SCREEN, self.color, (x, y + 20), (x, y), 4)

    def del_walls(self, next_cell: Cell) -> None:
        dr = next_cell.row - self.row
        dc = next_cell.col - self.col

        if dr == -1:  # next cell is above
            self.walls[0] = False  # TOP
            next_cell.walls[2] = False  # BOTTOM
        elif dr == 1:  # next cell is below
            self.walls[2] = False  # BOTTOM
            next_cell.walls[0] = False  # TOP

        if dc == -1:  # next cell is to the left
            self.walls[3] = False  # LEFT
            next_cell.walls[1] = False  # RIGHT
        elif dc == 1:  # next cell is to the right
            self.walls[1] = False  # RIGHT
            next_cell.walls[3] = False  # LEFT



