def selection_sort(nums):
    for i in range(len(nums)):
        least = i
        for j in range(i, len(nums)):
            if nums[least] > nums[j]:
                least = j
        nums[i], nums[least] = nums[least], nums[i]
    print(nums)


selection_sort([12, 3, 1, 6, 5, 2, 3, 22, 46, 11, 32])
