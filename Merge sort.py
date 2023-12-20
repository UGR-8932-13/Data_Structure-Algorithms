import random
import time

class Sorting:
    @staticmethod
    def mergeSort(arr):
        if len(arr) > 1:
            mid = len(arr)//2
            sub_array1 = arr[:mid]
            sub_array2 = arr[mid:]
 
            Sorting.mergeSort(sub_array1)
            Sorting.mergeSort(sub_array2)
        
            i = j = k = 0
 
            # Until we reach the end of either start or end, pick larger among
            # elements start and end and place them in the correct position in the sorted array
            while i < len(sub_array1) and j < len(sub_array2):
                if sub_array1[i] < sub_array2[j]:
                    arr[k] = sub_array1[i]
                    i += 1
                else:
                    arr[k] = sub_array2[j]
                    j += 1
                k += 1
 
            # When all elements are traversed in either arr1 or arr2,
            # pick up the remaining elements and put in sorted array
            while i < len(sub_array1):
                arr[k] = sub_array1[i]
                i += 1
                k += 1
 
            while j < len(sub_array2):
                arr[k] = sub_array2[j]
                j += 1
                k += 1
            
    @staticmethod
    def test():
        # Test with randomly generated integers
        arr = [random.randint(0, 1000000) for _ in range(1000000)]
        start_time = time.time()
        Sorting.mergeSort(arr)
        end_time = time.time()
        print("Time taken to sort 1,000,000 randomly generated integers:", end_time - start_time, "seconds")

        # Test with sorted integers in increasing order
        arr = [i for i in range(1000000)]
        start_time = time.time()
        Sorting.mergeSort(arr)
        end_time = time.time()
        print("Time taken to sort 1,000,000 sorted integers in increasing order:", end_time - start_time, "seconds")

        # Test with sorted integers in decreasing order
        arr = [i for i in range(1000000, 0, -1)]
        start_time = time.time()
        Sorting.mergeSort(arr)
        end_time = time.time()
        print ("Time taken to sort 1,000,000 sorted integers in decreasing order:", end_time - start_time, "seconds")