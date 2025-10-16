import math
from visualization import render_frame, Column
from random import shuffle

# Bubble sort - O(n^2)
def bubble_sort(columns: list[Column], visualize: bool, delay: float) -> list:
    n = len(columns)

    for i in range(n):

        swapped = False  # track if any swaps occur
        for j in range(0, n - i - 1):

            if columns[j] > columns[j + 1]:  # swap if out of order
                columns[j], columns[j + 1] = columns[j + 1], columns[j]
                render_frame(columns, delay) if visualize else None # hud - {"n":str(n), "d":str(delay)}

                swapped = True

        if not swapped:  # stop if array already sorted
            break

    return columns


# Selection sort - O(n^2)
def selection_sort(columns: list[Column], visualize: bool, delay: float) -> list:
    n = len(columns)

    for i in range(n):
        min_idx = i
        for j in range(i, n):

            if columns[j] < columns[min_idx]:  # find smallest element
                min_idx = j

        # place the smallest element at position i
        columns[i], columns[min_idx] = columns[min_idx], columns[i]
        render_frame(columns, delay) if visualize else None

    return columns


# Insertion sort - O(n^2)
def insertion_sort(columns: list[Column], visualize: bool, delay: float) -> list:
    n = len(columns)

    for i in range(1, n):
        key = columns[i]  # current element to insert
        current_idx = i
        while current_idx != 0 and key < columns[current_idx - 1]:

            # shift element right
            columns[current_idx] = columns[current_idx - 1]
            render_frame(columns, delay) if visualize else None
            current_idx -= 1

        # place key in correct position
        columns[current_idx] = key
        render_frame(columns, delay) if visualize else None

    return columns


# Merge sort - O(n log n)
def merge_sort(columns: list[Column], l: int = 0, r: int | None = None, visualize: bool = True, delay: float = 0.02) -> list[Column]:

    if r is None:
        r = len(columns) - 1

    if l >= r:  # base case: single element
        return columns

    mid = (l + r) // 2

    # sort left and right halves
    merge_sort(columns, l, mid, visualize, delay)
    merge_sort(columns, mid + 1, r, visualize, delay)

    # merge step
    L = columns[l:mid + 1]
    R = columns[mid + 1:r + 1]

    i = j = 0
    k = l

    # merge while both lists have elements
    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            columns[k] = L[i]
            i += 1
        else:
            columns[k] = R[j]
            j += 1
        render_frame(columns, delay) if visualize else None
        k += 1

    # copy remaining L
    while i < len(L):
        columns[k] = L[i]
        i += 1
        k += 1
        render_frame(columns, delay) if visualize else None

    # copy remaining R
    while j < len(R):
        columns[k] = R[j]
        j += 1
        k += 1
        render_frame(columns, delay) if visualize else None

    return columns


# Quick sort - O(n log n) average, O(n^2) worst
def quick_sort(columns: list[Column], l: int = 0, r: int = None, visualize: bool = True, delay: float = 0.02) -> list:

    if r is None:
        r = len(columns) - 1

    if l >= r:  # base case
        return columns

    pivot = columns[r].value  # choose pivot
    L = []  # left side
    R = []  # right side

    # partition step
    for item in columns[l:r]:
        if item.value <= pivot:
            L.append(item)
        else:
            R.append(item)

    # put partitioned elements back
    columns[l:r + 1] = L + [Column(len(L), pivot)] + R

    render_frame(columns, delay) if visualize else None

    # recursively sort left and right partitions
    quick_sort(columns, l, l + len(L) - 1, visualize, delay)  # left side
    quick_sort(columns, l + len(L) + 1, r, visualize, delay)  # right side

    return columns


# Build max heap
def build_max_heap(columns: list[Column]) -> list:
    n = len(columns)

    # start from last non-leaf node
    for i in range(n // 2, -1, -1):
        columns = max_heapify(columns, n, i)

    return columns


# Maintain max-heap property
def max_heapify(columns: list[Column], n: int, i: int) -> list:
    l = 2 * i
    r = 2 * i + 1

    # assume current node is largest
    largest = i

    # check for larger child
    if l < n and columns[l] > columns[i]:
        largest = l

    if r < n and columns[r] > columns[largest]:
        largest = r

    # if largest is not parent, swap and continue heapifying
    if largest != i:
        columns[i], columns[largest] = columns[largest], columns[i] # swap
        columns = max_heapify(columns, n, largest) # recursive call

    return columns


# Heap sort - O(n log n)
def heap_sort(columns: list[Column], visualize: bool, delay: float) -> list:

    columns = build_max_heap(columns)  # build heap
    n = len(columns)
    for i in range(n - 1, 0, -1):
        columns[i], columns[0] = columns[0], columns[i]  # swap root with last
        render_frame(columns, delay) if visualize else None
        max_heapify(columns, i, 0)  # restore heap property

    return columns


# Counting sort - O(n + k)
def counting_sort(columns: list[Column], visualize: bool, delay: float) -> list:
    n = len(columns)

    if n == 0: return columns

    # Find the maximum value to define the counting array size
    max_val = max(columns).value
    counting = [0] * (max_val + 1) # initialize counting array

    # Count occurrences of each value
    for item in columns:
        counting[item.value] += 1

    # Reconstruct the sorted array
    j, i = 0, 0
    while i < n:
        if counting[j] > 0:
            columns[i].value = j
            counting[j] -= 1
            i += 1
            render_frame(columns, delay) if visualize else None
        else:
            j += 1 # move to the next number

    return columns

# Bucket sort - O(n + k)
def bucket_sort(columns: list[Column], visualize: bool, delay: float) -> list[Column]:
    n = len(columns)
    k = int(math.sqrt(n))

    buckets = [[] for _ in range(k + 1)]

    for item in columns:
        i = min(item.value//k, k)
        buckets[i].append(item)

    if not buckets[-1]: del buckets[-1]

    for bucket in buckets:
        bucket_len = len(bucket)

        for i in range(1, bucket_len):
            key = bucket[i]  # current element to insert
            current_idx = i
            while current_idx != 0 and key < bucket[current_idx - 1]:
                # shift element right
                bucket[current_idx] = bucket[current_idx - 1]
                current_idx -= 1

            # place key in correct position
            bucket[current_idx] = key
            columns = [item for bucket in buckets for item in bucket]
            render_frame(columns, delay) if visualize else None

        render_frame(columns, delay) if visualize else None

    return columns

# Shell sort - O(n log n)
def shell_sort(columns: list[Column], visualize: bool, delay: float) -> list[Column]:
    n = len(columns)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            current = i
            while current - gap >= 0 and columns[current] < columns[current - gap]:
                columns[current], columns[current - gap] = columns[current - gap], columns[current]
                current -= gap
                render_frame(columns, delay) if visualize else None
        gap = gap // 2

    return columns

def tim_sort(columns: list[Column], visualize: bool, delay: float) -> list[Column]:
    # TODO: implement tim sort here

    return columns

# Radix sort - O(d * (n + k))
def radix_sort(columns: list[Column], visualize: bool, delay: float) -> list[Column]:

    def get_digit(num: int, place: int) -> int:
        return num // (10 ** place) % 10

    n = len(columns)
    max_val = max(columns).value
    d = len(str(max_val))

    output_arr = [Column() for _ in range(n)]

    for d_idx in range(d):
        # Counting sort for this digit
        counting = [0] * 10

        # Count occurrences of each digit
        for col in columns:
            digit = get_digit(col.value, d_idx)
            counting[digit] += 1

        # Prefix sum → convert to positions
        for i in range(1, 10):
            counting[i] += counting[i - 1]

        # Build output array (right to left to keep positions)
        for i in range(n - 1, -1, -1):
            digit = get_digit(columns[i].value, d_idx)
            counting[digit] -= 1
            output_arr[counting[digit]] = columns[i]

            render_frame(output_arr, delay) if visualize else None

        columns = output_arr.copy()

    return columns

# Comb sort - Best: O(n log n), Average: O(n^2)
def comb_sort(columns: list[Column], visualize: bool, delay: float) -> list[Column]:
    n = len(columns)
    shrink = 1.3
    gap = n
    swapped = True

    while gap > 1 or swapped:

        gap = max(1, int(gap / shrink))

        swapped = False  # track if any swaps occur
        for i in range(gap, n):

            if columns[i] < columns[i - gap]:  # swap if out of order
                columns[i], columns[i - gap] = columns[i - gap], columns[i]
                render_frame(columns, delay) if visualize else None

                swapped = True

    return columns

# Cocktail Shaker sort - O(n^2)
def cocktail_shaker_sort(columns: list[Column], visualize: bool, delay: float) -> list[Column]:
    n = len(columns)

    left = 0
    right = n - 1
    while left < right:
        swapped = False
        for j in range(left, right):
            if columns[j] > columns[j + 1]:
                columns[j], columns[j + 1] = columns[j + 1], columns[j]
                swapped = True
                render_frame(columns, delay) if visualize else None
        right -= 1

        for j in range(right, left, -1):
            if columns[j] < columns[j - 1]:
                columns[j], columns[j - 1] = columns[j - 1], columns[j]
                swapped = True
                render_frame(columns, delay) if visualize else None
        left += 1

        if not swapped:
            break

    return columns

# Bogo sort - O(n X n!)
def bogo_sort(columns: list[Column], visualize: bool, delay: float) -> list[Column]:

    is_sorted = False

    while not is_sorted:
        is_sorted = True
        for i in range(1, len(columns)):
            if columns[i] < columns[i - 1]:
                is_sorted = False
                shuffle(columns)
                render_frame(columns, delay) if visualize else None
                break

    return columns