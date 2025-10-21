import pygame
import config
from ..Drawable import Drawable
from ..elements.DisplayText import DisplayText

class InputBox(Drawable):
    def __init__(self, position: tuple[int | float, int | float], value: str, width: int = 120, height: int = 40):
        position = (position[0] + width // 2, position[1] + height// 2)
        super().__init__(position, value)
        self.rect = pygame.Rect(0, 0, width, height)
        self.rect.center = position
        self.width = width
        self.height = height
        self.active = False

    def draw(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            self.highlight()
        else:
            self.unhighlight()

        pygame.draw.rect(config.SCREEN, self.color, self.rect, 2)

        DisplayText(self.position,
                    str(self.value),
                    font_size=int(self.height * 0.75),
                    color = self.color
                    ).draw()

    def handle_event(self, event):
        # Clicked on input box
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = True
            else:
                self.active = False

        if event.type == pygame.KEYDOWN and self.active:
            if event.key == pygame.K_BACKSPACE:
                self.value = self.value[:-1]
            else:
                self.value += event.unicode