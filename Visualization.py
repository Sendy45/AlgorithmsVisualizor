# Example file showing a basic pygame "game loop"
import pygame.midi
import pygame
import time
# pygame setup
pygame.init()
pygame.midi.init()
player = pygame.midi.Output(1)
player.set_instrument(12)

def draw(arr: list, screen, delay: float) -> None:

    screen.fill("black")

    rec_width = screen.get_width() / (2 * len(arr))
    rec_height = screen.get_height() / (1 * len(arr))

    for i, item in enumerate(arr):
        rec = pygame.Rect(0, i * rec_height, rec_width * item, rec_height)
        pygame.draw.rect(screen, pygame.Color('green'), rec)

    # flip() the display to put your work on screen
    pygame.display.flip()

    player.note_on(60, 120)
    time.sleep(delay)