# Example file showing a basic pygame "game loop"
import pygame.midi
import pygame
import time
import config

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

def draw(arr: list, screen, delay: float) -> bool:
    # Return True if run should continue, False if it must restart
    if config.restart_run:
        return False  # stop current run immediately

    screen.fill("black")

    rec_width = screen.get_width() / len(arr)
    rec_height = screen.get_height() / len(arr)

    for i, item in enumerate(arr):
        #rec = pygame.Rect(0, i * rec_height, rec_width * item, rec_height) # verical
        rec = pygame.Rect(i * rec_width, screen.get_height() - rec_height * item, rec_width, rec_height * item)
        color = 'green' if i + 1 == item else 'white'
        pygame.draw.rect(screen, pygame.Color(color), rec)

    pygame.display.flip()

    event_handler()

    pygame.event.pump()

    player.note_on(60, 100)
    time.sleep(delay)

    return True