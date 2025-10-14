import pygame

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800

arr_length = 100
algorithm_idx = 0
delay = 0.003
algorithm_name = None
restart_run = False # flag to interrupt current run and restart

SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # visualization window

COLUMN_WIDTH = SCREEN.get_width() / arr_length
COLUMN_HEIGHT = SCREEN.get_height() / arr_length
