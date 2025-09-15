# Example file showing a basic pygame "game loop"
import pygame
import time
# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
FPS = 3
arr = [5, 2, 3, 1, 8, 4, 2]

def draw(arr: list, screen, delay: float) -> None:

    screen.fill("black")

    size = 1

    rec_width = screen.get_width() / (2 * len(arr))
    rec_height = screen.get_height() / (size * len(arr))

    for i, item in enumerate(arr):
        rec = pygame.Rect(0, i * rec_height, rec_width * item, rec_height)
        pygame.draw.rect(screen, pygame.Color('green'), rec)

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()
    time.sleep(delay)