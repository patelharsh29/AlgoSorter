import time

def bubble_sort(arr, update_callback):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                update_callback(arr)
                time.sleep(0.1)  # Simulate visualization delay

def merge_sort(arr, update_callback):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left, update_callback)
        merge_sort(right, update_callback)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
            update_callback(arr)
            time.sleep(0.1)

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
            update_callback(arr)
            time.sleep(0.1)

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
            update_callback(arr)
            time.sleep(0.1)

def quick_sort(arr, low, high, update_callback):
    if low < high:
        pi = partition(arr, low, high, update_callback)
        quick_sort(arr, low, pi - 1, update_callback)
        quick_sort(arr, pi + 1, high, update_callback)

def partition(arr, low, high, update_callback):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            update_callback(arr)
            time.sleep(0.1)
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    update_callback(arr)
    time.sleep(0.1)
    return i + 1

def selection_sort(arr, update_callback):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        update_callback(arr)
        time.sleep(0.1)

def insertion_sort(arr, update_callback):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        update_callback(arr)
        time.sleep(0.1)
