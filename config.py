import pygame

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

arr_length = 100
algorithm_idx = 0
delay = 0.003
restart_run = False # flag to interrupt current run and restart

SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # visualization window
