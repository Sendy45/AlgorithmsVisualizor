from Visualization import draw
import pygame
from random import shuffle
from config import SCREEN

# Bubble sort - O(n^2)
def bubble_sort(arr: list, visualize: bool, delay: float) -> list:
    n = len(arr)

    for i in range(n):

        swapped = False  # track if any swaps occur
        for j in range(0, n - i - 1):

            if arr[j] > arr[j + 1]:  # swap if out of order
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                draw(arr, SCREEN, delay) if visualize else None
                swapped = True

        if not swapped:  # stop if array already sorted
            break

    return arr


# Selection sort - O(n^2)
def selection_sort(arr: list, visualize: bool, delay: float) -> list:
    n = len(arr)

    for i in range(n):
        min_idx = i
        for j in range(i, n):

            if arr[j] < arr[min_idx]:  # find smallest element
                min_idx = j

        # place smallest element at position i
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        draw(arr, SCREEN, delay) if visualize else None

    return arr


# Insertion sort - O(n^2)
def insertion_sort(arr: list, visualize: bool, delay: float) -> list:
    n = len(arr)

    for i in range(1, n):
        key = arr[i]  # current element to insert
        current_idx = i
        while current_idx != 0 and key < arr[current_idx - 1]:

            # shift element right
            arr[current_idx] = arr[current_idx - 1]
            draw(arr, SCREEN, delay) if visualize else None
            current_idx -= 1

        # place key in correct position
        arr[current_idx] = key
        draw(arr, SCREEN, delay) if visualize else None

    return arr


# Merge sort - O(n log n)
def merge_sort(arr: list, l: int = 0, r: int | None = None, visualize: bool = True, delay: float = 0.02) -> list:

    if r is None:
        r = len(arr) - 1

    if l >= r:  # base case: single element
        return arr

    mid = (l + r) // 2

    # sort left and right halves
    merge_sort(arr, l, mid, visualize, delay)
    merge_sort(arr, mid + 1, r, visualize, delay)

    # merge step
    L = arr[l:mid + 1]
    R = arr[mid + 1:r + 1]

    i = j = 0
    k = l

    # merge while both lists have elements
    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        draw(arr, SCREEN, delay) if visualize else None
        k += 1

    # copy remaining L
    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1
        draw(arr, SCREEN, delay) if visualize else None

    # copy remaining R
    while j < len(R):
        arr[k] = R[j]
        j += 1
        k += 1
        draw(arr, SCREEN, delay) if visualize else None

    return arr


# Quick sort - O(n log n) average, O(n^2) worst
def quick_sort(arr: list, l: int = 0, r: int = None, visualize: bool = True, delay: float = 0.02) -> list:

    if r is None:
        r = len(arr) - 1

    if l >= r:  # base case
        return arr

    pivot = arr[r]  # choose pivot
    L = []  # left side
    R = []  # right side

    # partition step
    for item in arr[l:r]:
        if item <= pivot:
            L.append(item)
        else:
            R.append(item)

    # put partitioned elements back
    arr[l:r + 1] = L + [pivot] + R

    draw(arr, SCREEN, delay) if visualize else None

    # recursively sort left and right partitions
    quick_sort(arr, l, l + len(L) - 1, visualize, delay)  # left side
    quick_sort(arr, l + len(L) + 1, r, visualize, delay)  # right side

    return arr


# Build max heap
def build_max_heap(arr: list) -> list:
    n = len(arr)

    # start from last non-leaf node
    for i in range(n // 2, -1, -1):
        arr = max_heapify(arr, n, i)

    return arr


# Maintain max-heap property
def max_heapify(arr: list, n: int, i: int) -> list:
    l = 2 * i
    r = 2 * i + 1

    # assume current node is largest
    largest = i

    # check for larger child
    if l < n and arr[l] > arr[i]:
        largest = l

    if r < n and arr[r] > arr[largest]:
        largest = r

    # if largest is not parent, swap and continue heapifying
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i] # swap
        arr = max_heapify(arr, n, largest) # recursive call

    return arr


# Heap sort - O(n log n)
def heap_sort(arr: list, visualize: bool, delay: float) -> list:

    arr = build_max_heap(arr)  # build heap
    n = len(arr)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap root with last
        draw(arr, SCREEN, delay) if visualize else None
        max_heapify(arr, i, 0)  # restore heap property

    return arr


# Counting sort - O(n + k)
def counting_sort(arr: list, visualize: bool, delay: float) -> list:
    n = len(arr)

    if n == 0: return arr

    # Find the maximum value to define the counting array size
    max_value = max(arr)
    counting = [0] * (max_value + 1) # initialize counting array

    # Count occurrences of each value
    for item in arr:
        counting[item] += 1

    # Reconstruct the sorted array
    j, i = 0, 0
    while i < n:
        if counting[j] > 0:
            arr[i] = j
            counting[j] -= 1
            i += 1
            draw(arr, SCREEN, delay) if visualize else None
        else:
            j += 1 # move to the next number

    return arr

def cocktail_shaker_sort(arr: list, visualize: bool, delay: float) -> list:
    # TODO: implement cocktail sort here

    return arr

def shell_sort(arr: list, visualize: bool, delay: float) -> list:
    # TODO: implement shell sort here

    return arr

def tim_sort(arr: list, visualize: bool, delay: float) -> list:
    # TODO: implement tim sort here

    return arr

def radix_sort(arr: list, visualize: bool, delay: float) -> list:
    n = len(arr)

    #for i in range(n):


    return arr

def comb_sort(arr: list, visualize: bool, delay: float) -> list:
    # TODO: implement comb sort here

    return arr

def bucket_sort(arr: list, visualize: bool, delay: float) -> list:
    # TODO: implement bucket sort here

    return arr

def bogo_sort(arr: list, visualize: bool, delay: float) -> list:

    is_sorted = False

    while not is_sorted:
        is_sorted = True
        for i in range(1, len(arr)):
            if arr[i] < arr[i - 1]:
                is_sorted = False
                shuffle(arr)
                draw(arr, SCREEN, delay) if visualize else None
                break

    return arr