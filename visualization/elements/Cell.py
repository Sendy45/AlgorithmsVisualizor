from __future__ import annotations
import pygame
import config
from ..Drawable import Drawable

class Cell(Drawable):
    def __init__(self, position: tuple[int, int]):
        super().__init__(position)
        self.row = position[0]
        self.col = position[1]
        self.walls = [True, True, True, True]
        self.visited = False

    def draw(self) -> None:
        if self.visited:
            pygame.draw.rect(config.SCREEN, (150, 255, 150), pygame.Rect(self.row * 20, self.col * 20, 20, 20))
        if self.walls[0]: # UP WALL
            pygame.draw.line(config.SCREEN, self.color, (self.row* 20, self.col* 20), (self.row* 20+20, self.col* 20), 4)
        if self.walls[1]: # RIGHT WALL
            pygame.draw.line(config.SCREEN, self.color, (self.row* 20 + 20, self.col* 20), (self.row* 20 + 20, self.col* 20+20), 4)
        if self.walls[2]: # DOWN WALL
            pygame.draw.line(config.SCREEN, self.color, (self.row* 20 + 20, self.col* 20 + 20), (self.row* 20, self.col* 20 + 20), 4)
        if self.walls[3]: # LEFT WALL
            pygame.draw.line(config.SCREEN, self.color, (self.row* 20, self.col* 20 + 20), (self.row* 20, self.col* 20), 4)

    def del_walls(self, next_cell: Cell) -> None:
        x = self.row - next_cell.row
        y = self.col - next_cell.col

        if x == 1:
            self.walls[3] = False
            next_cell.walls[1] = False
        elif x == -1:
            self.walls[1] = False
            next_cell.walls[3] = False
        if y == 1:
            self.walls[0] = False
            next_cell.walls[2] = False
        elif y == -1:
            self.walls[2] = False
            next_cell.walls[0] = False



