import time
import sys
from sorting_algorithms import bubble_sort, merge_sort, quick_sort, selection_sort, insertion_sort

# Increase the recursion limit to avoid RecursionError for large arrays in quick_sort
sys.setrecursionlimit(2000)  # Set it to 2000 or higher if needed

# Function to count the visual updates during sorting
def count_updates(_):
    global updates
    updates += 1  # Increment on each callback

# Function to test each sorting algorithm's visual updates per second
def test_visual_updates(algorithm, max_size, algorithm_name):
    global updates  # Use global variable updates
    updates = 0

    print(f"Testing {algorithm_name} for visual updates...")
    for size in range(25, max_size + 1, 25):  # Test with increments of 25
        arr = list(range(size, 0, -1))  # Generate a reverse-sorted array
        start_time = time.time()

        # Check the algorithm and call it with appropriate parameters
        if algorithm_name == "Quick Sort":
            algorithm(arr, 0, len(arr) - 1, count_updates)  # Pass arr, 0, len(arr)-1, callback for quick_sort
        elif algorithm_name == "Merge Sort":
            algorithm(arr, count_updates)  # Pass only arr and callback for merge_sort
        else:
            algorithm(arr, count_updates)  # Pass only arr and callback for bubble_sort, insertion_sort, selection_sort

        elapsed_time = time.time() - start_time
        updates_per_second = updates / elapsed_time
        print(f"Array size {size}: {updates} updates in {elapsed_time:.2f} seconds ({updates_per_second:.2f} updates/sec)")

        if elapsed_time > 3:  # If sorting takes longer than 3 seconds, stop
            print(f"Max {algorithm_name} size for updates/sec: {size}")
            return updates_per_second
    return updates_per_second

# Run tests for each sorting algorithm
max_size = 50  # Max size is set to 50 now
max_bubble_sort_updates = test_visual_updates(bubble_sort, 25, "Bubble Sort")  # Set max size of bubble sort to 25 for speed
max_merge_sort_updates = test_visual_updates(merge_sort, max_size, "Merge Sort")
max_quick_sort_updates = test_visual_updates(quick_sort, max_size, "Quick Sort")
max_selection_sort_updates = test_visual_updates(selection_sort, max_size, "Selection Sort")
max_insertion_sort_updates = test_visual_updates(insertion_sort, max_size, "Insertion Sort")

# Print results
print(f"\nMax visual updates per second for each algorithm:")
print(f"Max Bubble Sort updates/sec: {max_bubble_sort_updates}")
print(f"Max Merge Sort updates/sec: {max_merge_sort_updates}")
print(f"Max Quick Sort updates/sec: {max_quick_sort_updates}")
print(f"Max Selection Sort updates/sec: {max_selection_sort_updates}")
print(f"Max Insertion Sort updates/sec: {max_insertion_sort_updates}")
