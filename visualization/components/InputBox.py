import pygame
import config
from .UIComponent import UIComponent
from ..elements.DisplayText import DisplayText

class InputBox(UIComponent):
    def __init__(self, position: tuple[int | float, int | float], value: str, width: int = 120, height: int = 40):
        position = (position[0] + width // 2, position[1] + height// 2)
        super().__init__(position, value, width = width, height = height)
        self.active = False

    def draw(self):
        mouse_pos = pygame.mouse.get_pos()
        if self._rect.collidepoint(mouse_pos):
            self.highlight()
        else:
            self.unhighlight()

        pygame.draw.rect(config.SCREEN, self.color, self._rect, 2)

        DisplayText(self._rect.center,
                    str(self.value),
                    font_size=int(self._height * 0.75),
                    color = self.color
                    ).draw()

    def handle_event(self, event):
        # Clicked on input box
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self._rect.collidepoint(event.pos):
                self.active = True
            else:
                self.active = False

        if event.type == pygame.KEYDOWN and self.active:
            if event.key == pygame.K_BACKSPACE:
                self.value = self.value[:-1]
            else:
                self.value += event.unicode