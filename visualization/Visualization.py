# Example file showing a basic pygame "game loop"
import pygame.midi
import pygame
import time
import config
from visualization.Column import Column
from visualization.DisplayText import DisplayText
from visualization.Drawable import Drawable

# pygame setup
pygame.init()
pygame.midi.init()
player = pygame.midi.Output(1)
player.set_instrument(12)

def event_handler():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit

        elif event.type == pygame.KEYDOWN:
            config.restart_run = True  # signal the sort to restart

            if event.key == pygame.K_UP:
                config.arr_length += 50
            elif event.key == pygame.K_DOWN:
                config.arr_length = max(10, config.arr_length - 50)
            elif event.key == pygame.K_RIGHT:
                config.algorithm_idx += 1
            elif event.key == pygame.K_LEFT:
                config.algorithm_idx -= 1
            elif event.key == pygame.K_d:
                config.delay += 0.001

def render_frame(objects: list[Drawable], delay: float, hud: dict[str, str] = None) -> bool:
    """
    Render one frame of the visualization.
    :param objects: list of Drawable objects (Columns, Nodes, etc.)
    :param delay: frame delay in seconds
    :param hud: dict of text labels { "label": "value" } to display
    :return: False if restart was requested, True otherwise
    """
    if config.restart_run:
        return False  # stop current run immediately

    config.SCREEN.fill("black")

    # Update object positions if they have 'position'
    for i, obj in enumerate(objects):
        if hasattr(obj, "position") and isinstance(obj.position, int):
            obj.position = i
        obj.draw()

    # Draw HUD (if any)
    if hud:
        for idx, (key, value) in enumerate(hud.items()):
            DisplayText((0, idx * 30), f"{key} = {value}","Green").draw()

    pygame.display.flip()

    event_handler()
    pygame.event.pump()

    player.note_on(60, 100)
    pygame.time.delay(int(delay * 1000))

    return True
