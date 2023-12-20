
import random
import time

class Sorting:
    def bubble_sort(self, arr):
        """
        Bubble sort algorithm to sort the given list in increasing order.
        """
        n = len(arr)
        for i in range(n):
            for j in range(0, n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]

    def test_sorting_algorithms(self):
        # Randomly generate 1,000,000 integers
        random_integers = [random.randint(0, 1000000) for _ in range(1000000)]

        # Generate 1,000,000 sorted integers (in increasing order)
        sorted_integers = [i for i in range(1000000)]

        # Generate 1,000,000 sorted integers (in decreasing order)
        reversed_integers = [i for i in range(1000000, 0, -1)]

        # Measure the running time for each sorting algorithm
        start_time = time.time()
        self.bubble_sort(random_integers)
        random_time = time.time() - start_time

        start_time = time.time()
        self.bubble_sort(sorted_integers)
        sorted_time = time.time() - start_time

        start_time = time.time()
        self.bubble_sort(reversed_integers)
        reversed_time = time.time() - start_time

        # Print the running times
        print("Running time for sorting random integers:", random_time)
        print("Running time for sorting sorted integers:", sorted_time)
        print("Running time for sorting reversed integers:", reversed_time)

# Create an instance of the Sorting class and test the sorting algorithms
sorting_obj = Sorting()
sorting_obj.test_sorting_algorithms()

