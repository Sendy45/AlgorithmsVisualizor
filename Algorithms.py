import time
import random
from Visualization import draw

def bubble_sort(arr: list) -> list:
    n = len(arr)

    for i in range(n):

        swapped = False
        for j in range(0, n-i-1):

            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                draw(arr)
                swapped = True

        if not swapped:
            break

    return arr

def selection_sort(arr: list) -> list:
    n = len(arr)

    for i in range(n):
        min_idx = i
        for j in range(i, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        draw(arr)

    return arr

def insertion_sort(arr: list) -> list:
    n = len(arr)

def random_array(length: int) -> list:
    arr = list(range(length))
    random.shuffle(arr)
    return arr

if __name__ == "__main__":
    arr = random_array(100)
    start_time = time.time()
    selection_sort(arr)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print("Elapsed time: ", elapsed_time)
