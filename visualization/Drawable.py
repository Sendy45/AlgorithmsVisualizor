class Drawable:
    def __init__(self, position: int | tuple[int | float, int | float] = 0, value: str | float | int = 0) -> None:
        self.position = position
        self.value = value
        self.highlighted = False

    def highlight(self) -> None:
        self.highlighted = True

    def draw(self):
        raise NotImplementedError("Drawable subclasses must implement draw()")