import config
from visualization.Drawable import Drawable
import pygame

class UIComponent(Drawable):
    def __init__(self, position: tuple[int | float, int | float], value: str, action = None, width: int = 80, height: int = 50):
        center_pos = (position[0] + width // 2, position[1] + height// 2)
        self._position = position
        self.action = action
        self._rect = pygame.Rect(0, 0, width, height)
        self._rect.center = center_pos
        self._width = width
        self._height = height

        super().__init__(self._position, value)

    def get_position(self) -> tuple[int | float, int | float]:
        return self._position

    def get_width(self) -> int:
        return self._width

    def get_height(self) -> int:
        return self._height

    def set_position(self, position: tuple[int | float, int | float]):
        center_pos = (position[0] + self._width // 2, position[1] + self._height // 2)
        self._position = position
        self._rect.center = center_pos

    def set_height(self, height: int):
        self._height = height
        self._rect.h = height
        self.set_position(self._position)

    def set_width(self, width: int):
        self._width = width
        self._rect.w = width
        self.set_position(self._position)

    def clip_to(self, anchor: str, margin: int = 0):
        """
        Aligns the button to a screen edge or corner.
        anchor options:
            "top-left", "top-right", "bottom-left", "bottom-right",
            "center", "top", "bottom", "left", "right"
        margin: distance from screen edges
        """
        screen_w = config.SCREEN_WIDTH
        screen_h = config.SCREEN_HEIGHT

        match anchor:
            case "top-left":
                self.set_position((margin, margin))
            case "top-right":
                self.set_position((screen_w - self._width - margin, margin))
            case "bottom-left":
                self.set_position((margin, screen_h - self._height - margin))
            case "bottom-right":
                self.set_position((screen_w - self._width - margin, screen_h - self._height - margin))
            case "top":
                self.set_position((self._position[0], margin))
            case "bottom":
                self.set_position((self._position[0], screen_h - self._height - margin))
            case "left":
                self.set_position((margin, self._position[1]))
            case "right":
                self.set_position((screen_w - self._width - margin, self._position[1]))
            case "center":
                self.set_position(((screen_w - self._width) // 2, (screen_h - self._height) // 2))

            case _:
                raise ValueError(f"Invalid anchor '{anchor}'")

        return self