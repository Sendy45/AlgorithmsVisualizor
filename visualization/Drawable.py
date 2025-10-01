class Drawable:
    def __init__(self, position: int | tuple[int, int], value: int = 0):
        self.position = position
        self.value = value

    def draw(self):
        raise NotImplementedError("Drawable subclasses must implement draw()")