import pygame
import config
from .UIComponent import UIComponent
from ..elements.DisplayText import DisplayText


class Button(UIComponent):
    def __init__(self, position: tuple[int | float, int | float], value: str, action = None, width: int = 80, height: int = 50):
        super().__init__(position, value, action, width, height)

    def draw(self):
        mouse_pos = pygame.mouse.get_pos()
        if self._rect.collidepoint(mouse_pos):
            self.highlight()
        else:
            self.unhighlight()

        pygame.draw.rect(config.SCREEN, self.color, self._rect)

        DisplayText(self._rect.center,
                    str(self.value),
                    font_size=int(self._height * 0.5)
                    ).draw()

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and self._rect.collidepoint(event.pos):
            if self.action:
                self.action()
