import pygame
import config
from visualization.Drawable import Drawable
from visualization.DisplayText import DisplayText


class Button(Drawable):
    def __init__(self, position: tuple[int | float, int | float], value: str, action = None, width: int = 80, height: int = 50):
        position = (position[0] + width // 2, position[1] + height// 2)
        super().__init__(position, value)
        self.action = action
        self.rect = pygame.Rect(0, 0, width, height)
        self.rect.center = position
        self.width = width
        self.height = height

    def draw(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            self.highlight()
        else:
            self.unhighlight()

        pygame.draw.rect(config.SCREEN, self.color, self.rect)

        DisplayText(self.position,
                    str(self.value),
                    font_size=int(self.height * 0.5)
                    ).draw()

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos):
            if self.action:
                self.action()
