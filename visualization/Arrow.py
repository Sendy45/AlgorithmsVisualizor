import pygame
import math
import config
from visualization import Drawable, DisplayText


class Arrow(Drawable):
    def __init__(self, start_position: tuple[int | float, int | float], end_position: tuple[int | float, int | float], value: str | float | int = None, padding: int = 0, highlighted: bool = False) -> None:
        super().__init__(value=value, highlighted=highlighted)
        self.start_position = start_position
        self.end_position = end_position
        self.padding = padding

    def draw(self) -> None:
        start_point = self.start_position
        end_point = self.end_position

        if self.padding > 0:
            dx = end_point[0] - start_point[0]
            dy = end_point[1] - start_point[1]
            distance = math.hypot(dx, dy)

            if distance != 0:
                # Normalize direction vector and scale by padding
                pad_x = (dx / distance) * self.padding
                pad_y = (dy / distance) * self.padding

                start_point = (start_point[0] + pad_x, start_point[1] + pad_y)
                end_point = (end_point[0] - pad_x, end_point[1] - pad_y)

        if self.value:
            midpoint = ((start_point[0] + end_point[0]) / 2 , (start_point[1] + end_point[1]) / 2)
            DisplayText(midpoint, self.value).draw()

        pygame.draw.line(config.SCREEN, self.color, start_point, end_point)


