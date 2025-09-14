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

def run():
    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # fill the screen with a color to wipe away anything from last frame
        screen.fill("white")

        rec_width = screen.get_width() / (2 * len(arr))
        rec_height = screen.get_height() / (2 * len(arr))

        for i, item in enumerate(arr):
            rec = pygame.Rect(0, i * rec_height, rec_width * item, rec_height)
            pygame.draw.rect(screen, pygame.Color('blue'), rec)


        # RENDER YOUR GAME HERE

        # flip() the display to put your work on screen
        pygame.display.flip()

        clock.tick(FPS)  # limits FPS

    pygame.quit()

def draw(arr: list) -> None:
    # pygame setup
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    screen.fill("white")
    rec_width = screen.get_width() / (2 * len(arr))
    rec_height = screen.get_height() / (2 * len(arr))

    for i, item in enumerate(arr):
        rec = pygame.Rect(0, i * rec_height, rec_width * item, rec_height)
        pygame.draw.rect(screen, pygame.Color('blue'), rec)

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()
    time.sleep(0.01)