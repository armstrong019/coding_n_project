def quicksort(nums):
    is_sorted = False
    while not is_sorted:
        is_sorted = True
        for i in range(len(nums)-1):
            if nums[i]>nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
                is_sorted = False
    return nums

nums = [3,2,5,-1,9,0]
print(quicksort(nums))
