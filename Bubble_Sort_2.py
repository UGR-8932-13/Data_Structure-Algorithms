import random
import time

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def test_sorting_algorithms():
    # Generate 1,000,000 random integers
    random_ints = [random.randint(0, 100) for _ in range(100)]

    # Test Bubble Sort on random integers
    start_time = time.time()
    sorted_ints = bubble_sort(random_ints)
    end_time = time.time()
    print(f"Time taken for Bubble Sort on random integers: {end_time - start_time:.5f} seconds")

    # Generate 1,000,000 sorted integers (in increasing order)
    sorted_ints_increasing = [i for i in range(100)]

    # Test Bubble Sort on sorted integers (in increasing order)
    start_time = time.time()
    sorted_ints = bubble_sort(sorted_ints_increasing)
    end_time = time.time()
    print(f"Time taken for Bubble Sort on sorted integers (in increasing order): {end_time - start_time:.5f} seconds")

    # Generate 1,000,000 sorted integers (in decreasing order)
    sorted_ints_decreasing = [i for i in range(100, 0, -1)]

    # Test Bubble Sort on sorted integers (in decreasing order)
    start_time = time.time()
    sorted_ints = bubble_sort(sorted_ints_decreasing)
    end_time = time.time()
    print(f"Time taken for Bubble Sort on sorted integers (in decreasing order): {end_time - start_time:.5f} seconds")

if __name__ == "__main__":
    test_sorting_algorithms()