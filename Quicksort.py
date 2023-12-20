import random
import time
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def test_function():
    random_numbers = [random.randint(1, 1000000) for _ in range(1000000)]
    start_time = time.time()
    quick_sort(random_numbers)
    end_time = time.time()
    random_sort_time = end_time - start_time

    increasing = sorted(random_numbers)
    start_time = time.time()
    quick_sort(increasing)
    end_time = time.time()
    sorted_numbers_time = end_time - start_time

    decreasing_order = sorted(random_numbers, reverse=True)
    start_time = time.time()
    quick_sort(decreasing_order)
    end_time = time.time()
    decreasing_order_time = end_time - start_time
    print("quick sorting random numbers finished in" + " " + str(random_sort_time))
    print("quick sorting sorted integers(increasing order) finished in" + " " + str(sorted_numbers_time))
    print("quick sorting sorted integers (decreasing order) finished in" + " " + str(decreasing_order_time))
    return

if __name__ == "__main__":
    test_function()


