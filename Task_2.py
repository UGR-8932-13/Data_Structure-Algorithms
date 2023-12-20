
class Searching:
    def linear_search(self, arr, target):
        for i in range(len(arr)):
            if arr[i] == target:
                return i
        return -1

    def binary_search(self, arr, target):
        low, high = 0, len(arr) - 1

        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        return -1

    def optimized_binary_search(self, arr, target):
        low, high = 0, len(arr) - 1

        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        return -1

    def test_searching_algorithms(self):
        import time
        import random

        arr = sorted(random.sample(range(1, 10000001), 1000000))
        target = arr[-1]

        start_time = time.time()
        linear_index = self.linear_search(arr, target)
        linear_time = time.time() - start_time

        start_time = time.time()
        binary_index = self.binary_search(arr, target)
        binary_time = time.time() - start_time

        start_time = time.time()
        optimized_binary_index = self.optimized_binary_search(arr, target)
        optimized_binary_time = time.time() - start_time

        print("linear search: index:", linear_index, "time:", linear_time)
        print("binary search: index:", binary_index, "time:", binary_time)
        print("optimized binary search: index:", optimized_binary_index, "time:", optimized_binary_time)


searching = Searching()
searching.test_searching_algorithms()
