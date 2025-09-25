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

    rec_width = screen.get_width() / len(arr)
    rec_height = screen.get_height() / len(arr)

    for i, item in enumerate(arr):
        #rec = pygame.Rect(0, i * rec_height, rec_width * item, rec_height) # verical
        rec = pygame.Rect(i * rec_width, screen.get_height() - rec_height * item, rec_width, rec_height * item)

        if i + 1 == item:
            pygame.draw.rect(screen, pygame.Color('green'), rec)
        else:
            pygame.draw.rect(screen, pygame.Color('white'), rec)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit

    pygame.event.pump()


    player.note_on(60, 100)
    time.sleep(delay)