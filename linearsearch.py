
class Searching:
    @staticmethod
    def linear_search(array, target):
        
        for index, element in enumerate(array):
            if element == target:
                return index
        
        return -1
    def binary_search(self, arr, target):
        low = 0
        high = len(arr) - 1

        while low <= high:
            mid = (low + high) // 2

            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        return -1
my_list = [10, 20, 30, 40, 50, 60]
target_element = 80

search_obj = Searching()
result = search_obj.linear_search(my_list, target_element)

if result == -1:
    print("Element not found in the list.")
else:
    print(f"Element found at index {result}.")
my_list = [10, 20, 30, 40, 50, 60]
target_element = 20

search_obj = Searching()
result = search_obj.binary_search(my_list, target_element)

if result == -1:
    print("Element not found in the list.")
else:
    print(f"Element found at index {result}.")
