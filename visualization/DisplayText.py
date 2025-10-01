import pygame
import config

class DisplayText:
    def __init__(self, value: str, position: tuple[int, int], font_size: int = 20):
        self.value = value
        self.position = position
        self.font_size = font_size

    def draw(self) -> None:
        # Display collision count
        font = pygame.font.Font('freesansbold.ttf', self.font_size)
        txt = font.render(self.value, True, "green")
        config.SCREEN.blit(txt, self.position)