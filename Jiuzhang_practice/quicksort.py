def bubblesort(nums):
    is_sorted = False
    while not is_sorted:
        is_sorted = True
        for i in range(len(nums)-1):
            if nums[i]>nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
                is_sorted = False
    return nums

nums = [3,2,5,-1,9,0]
print(bubblesort(nums))

# O（n**2）最差 average O（nlgn）
# quicksort and bubble sort 都是inplace sorting algorithm
class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        start = 0
        end = len(nums) - 1
        self.quicksort(nums, start, end)
        return nums

    def quicksort(self, nums, start, end):
        if start >= end:
            return
        pind = self.partition(nums, start, end)
        self.quicksort(nums, pind + 1, end)
        self.quicksort(nums, start, pind - 1)

    def partition(self, nums, left, right):
        pivot = nums[right] #最后一位是pivot
        pind = left # 指向需要swap的位置
        for i in range(left, right):
            if nums[i] < pivot: # 如果当前值比pivot 小，那么就swap
                nums[pind], nums[i] = nums[i], nums[pind]
                pind += 1
        nums[pind], nums[right] = nums[right], nums[pind]# 最后将pivot放进来
        return pind

sortedInsert(Stack S, element)
    if stack is empty OR element > top element
        push(S, elem)
    else
        temp = pop(S)
        sortedInsert(S, element)
        push(S, temp)
