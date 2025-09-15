import time
import random

from Visualization import draw
import pygame.midi
import pygame

def analyze_algorithm(func,  *args, visualize: bool = True, delay: float = 0.02) -> dict:
    global operation_count
    operation_count = 0

    start_time = time.perf_counter()
    result = func(*args, visualize, delay)
    end_time = time.perf_counter()

    return {
        "result": result,
        "time": end_time - start_time,
        "operations": operation_count
    }

def bubble_sort(arr: list, visualize: bool, delay: float) -> list:
    n = len(arr)
    global operation_count

    for i in range(n):

        swapped = False
        for j in range(0, n-i-1):

            operation_count += 1

            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                draw(arr, screen, delay) if visualize else None
                swapped = True

        if not swapped:
            break

    return arr

def selection_sort(arr: list, visualize: bool, delay: float) -> list:
    n = len(arr)
    global operation_count

    for i in range(n):
        min_idx = i
        for j in range(i, n):

            operation_count += 1
            player.note_on(note=60, velocity=100)

            if arr[j] < arr[min_idx]:
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        draw(arr, screen, delay) if visualize else None

    return arr

def insertion_sort(arr: list, visualize: bool, delay: float) -> list:
    n = len(arr)
    global operation_count

    for i in range(1, n):
        key = arr[i]
        current_idx = i
        while current_idx!=0 and key < arr[current_idx-1]:
            operation_count += 1
            player.note_on(note=60, velocity=100)

            arr[current_idx] = arr[current_idx-1]
            draw(arr, screen, delay) if visualize else None
            current_idx -= 1

        arr[current_idx] = key
        draw(arr, screen, delay) if visualize else None

    return arr


def random_array(length: int) -> list:
    arr = list(range(length))
    random.shuffle(arr)
    return arr

if __name__ == "__main__":
    # pygame setup
    pygame.midi.init()
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))

    unsorted_arr = random_array(100)

    player = pygame.midi.Output(1)
    player.set_instrument(11)
    #player.note_on(note=60, velocity=100)
    stats = analyze_algorithm(selection_sort, unsorted_arr, delay=0.03)
    print("time "+ str(stats["time"]))
    print("operations "+ str(stats["operations"]))

    running = True
    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        event = pygame.event.wait()
        if event.type == pygame.QUIT:
            running = False
    pygame.quit()

