import pygame
import config
from visualization.Drawable import Drawable


class DisplayText(Drawable):
    def __init__(self, position: tuple[int | float, int | float], value: str, font_size: int = 20):
        super().__init__(position, value, color="Black")
        self.font_size = font_size
        self.font = pygame.font.SysFont('freesansbold', self.font_size)

    def draw(self) -> None:
        # Display collision count
        txt = self.font.render(self.value, True, self.color)

        # get the rectangle for the text surface, centered at the given position
        text_rect = txt.get_rect(center=self.position)

        config.SCREEN.blit(txt, text_rect)