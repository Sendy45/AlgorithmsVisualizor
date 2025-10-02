import pygame
import config
from visualization import Drawable


class DisplayText:
    def __init__(self, position: tuple[int | float, int | float], value: str, color: str | tuple[int, int, int] = (255, 255, 255), font_size: int = 20):
        self.position = position
        self.value = value
        self.highlighted = False
        self.font_size = font_size
        self.font = pygame.font.SysFont('freesansbold', self.font_size)
        self.color = color

    def draw(self) -> None:
        # Display collision count
        txt = self.font.render(self.value, True, self.color)

        # get the rectangle for the text surface, centered at the given position
        text_rect = txt.get_rect(center=self.position)

        config.SCREEN.blit(txt, text_rect)