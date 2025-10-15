import pygame
import config
from visualization.Drawable import Drawable


class Column(Drawable):
    def __init__(self, position: int = 0, value: int = 0):
        super().__init__(position, value)

    def draw(self) -> None:
        col_w = config.SCREEN_WIDTH / config.arr_length
        col_h = config.SCREEN_HEIGHT / config.arr_length

        rec = pygame.Rect(
            self.position * col_w,
            config.SCREEN_HEIGHT - col_h * self.value,
            col_w,
            col_h * self.value
        )

        if self.value == self.position + 1:
            self.highlight()
        else:
            self.unhighlight()

        pygame.draw.rect(config.SCREEN, self.color, rec)


    def __lt__(self, other) -> bool:
        return self.value < other.value


