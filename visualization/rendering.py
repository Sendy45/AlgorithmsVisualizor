import pygame.midi
import pygame
import config
from visualization.DisplayText import DisplayText
from visualization.Drawable import Drawable
from visualization.Button import Button

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

        for btn in config.item_to_render:
            if isinstance(btn, Button):
                btn.handle_event(event)

def render_frame(objects: list[Drawable], delay: float, hud: dict[str, str] = None, play_sound: bool = False) -> bool:
    """
    Render one frame of the visualization.
    :param objects: list of Drawable objects (Columns, Nodes, etc.)
    :param delay: frame delay in seconds
    :param hud: dict of text labels { "label": "value" } to display
    :param play_sound: flag to play sound
    :return: False if restart was requested, True otherwise
    """

    event_handler()

    if config.restart_run:
        return False  # stop current run immediately

    config.SCREEN.fill("black")

    # Update object positions if they have 'position'
    for i, obj in enumerate(objects):
        if hasattr(obj, "position") and isinstance(obj.position, int):
            obj.position = i
        obj.draw()

    for obj in config.item_to_render:
        obj.draw()

    # Draw HUD (if any)
    if hud:
        for idx, (key, value) in enumerate(hud.items()):
            DisplayText((0, idx * 30), f"{key} = {value}").draw()

    pygame.display.flip()

    pygame.event.pump()

    player.note_on(60, 100) if play_sound else None
    pygame.time.delay(int(delay * 1000))

    return True
