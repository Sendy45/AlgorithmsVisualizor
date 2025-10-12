import pygame

import config
from visualization import Drawable


class Arrow(Drawable):
    def __init__(self, start_position: tuple[int | float, int | float], end_position: tuple[int | float, int | float], value: str | float | int = None, padding: int = 0) -> None:
        super().__init__(value=value)
        self.start_position = start_position
        self.end_position = end_position
        self.padding = padding

    def draw(self) -> None:
        pygame.draw.line(config.SCREEN, "Green", self.start_position , self.end_position)

