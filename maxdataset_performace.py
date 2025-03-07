import time
import sys
from sorting_algorithms import bubble_sort, merge_sort, quick_sort, selection_sort, insertion_sort

# Set a higher recursion limit for deeper recursion (needed for larger arrays)
sys.setrecursionlimit(20000)

# Override time.sleep temporarily for performance testing
original_sleep = time.sleep

def fast_sleep(seconds):
    """Override time.sleep to skip the delay during performance testing."""
    pass  # Do nothing (skip the sleep)

def test_algorithm(algorithm, max_size, step_size=1000):  # Increased step size for better performance testing
    def dummy_callback(_):
        pass  # No-op callback for testing performance

    # Temporarily override time.sleep with fast_sleep to skip the delays
    time.sleep = fast_sleep

    if algorithm == quick_sort:
        for size in range(1000, max_size + 1, step_size):  # Start with increments of 1000
            arr = list(range(size, 0, -1))  # Generate a reverse-sorted array
            start_time = time.time()
            algorithm(arr, 0, len(arr) - 1, dummy_callback)  # Run the algorithm without visualization
            elapsed_time = time.time() - start_time
            print(f"Array size {size} sorted in {elapsed_time:.2f} seconds")
            if elapsed_time > 3:  # Threshold in seconds
                return size - step_size  # Previous size was the max acceptable
        return max_size
    
    for size in range(1000, max_size + 1, step_size):  # Start with increments of 1000
        arr = list(range(size, 0, -1))  # Generate a reverse-sorted array
        start_time = time.time()
        algorithm(arr, dummy_callback)  # Run the algorithm without visualization
        elapsed_time = time.time() - start_time
        print(f"Array size {size} sorted in {elapsed_time:.2f} seconds")
        if elapsed_time > 3:  # Threshold in seconds
            return size - step_size  # Previous size was the max acceptable
    return max_size

# Example usage for testing all algorithms:
print("Testing Bubble Sort...")
max_bubble_sort_size = test_algorithm(bubble_sort, 10000)
print(f"Max Bubble Sort size: {max_bubble_sort_size}")

print("\nTesting Merge Sort...")
max_merge_sort_size = test_algorithm(merge_sort, 10000)
print(f"Max Merge Sort size: {max_merge_sort_size}")

print("\nTesting Quick Sort...")
max_quick_sort_size = test_algorithm(quick_sort, 10000)
print(f"Max Quick Sort size: {max_quick_sort_size}")

print("\nTesting Selection Sort...")
max_selection_sort_size = test_algorithm(selection_sort, 10000)
print(f"Max Selection Sort size: {max_selection_sort_size}")

print("\nTesting Insertion Sort...")
max_insertion_sort_size = test_algorithm(insertion_sort, 10000)
print(f"Max Insertion Sort size: {max_insertion_sort_size}")
