import pygame
from typing import Union, Tuple
from config import default_color, highlight_color

ColorType = Union[str, Tuple[int,int,int], Tuple[int,int,int,int], pygame.Color]

class Drawable:
    def __init__(self, position: int | tuple[int | float, int | float] = 0, value: str | float | int = 0, highlighted: bool = False, color: ColorType = default_color) -> None:
        self.position = position
        self.value = value
        self.highlighted = highlighted
        self.color = pygame.Color(color)

    def highlight(self) -> None:
        self.highlighted = True
        self.color = highlight_color

    def unhighlight(self) -> None:
        self.highlighted = False
        self.color = default_color

    def draw(self):
        raise NotImplementedError("Drawable subclasses must implement draw()")