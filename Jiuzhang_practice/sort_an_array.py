# selection sort 的写法
class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        for i in range(len(nums) - 1):
            min_ind = i # min_ind 代表从i点到最后一点的最小值。
            for j in range(i + 1, len(nums)):
                if nums[j] < nums[min_ind]:
                    min_ind = j
            nums[i], nums[min_ind] = nums[min_ind], nums[i]
        return nums

# O（n**2）最差 average O（nlgn）
#quicksort 找一个pivot 将比他小的都放在他的左边 大于等于他的放在右边
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

    def partition(self, nums, left, right): # similar to move zeros
        pivot = nums[right] #最后一位是pivot
        pind = left # 指向需要swap的位置
        for i in range(left, right):
            if nums[i] < pivot: # 如果当前值比pivot 小，那么就swap
                nums[pind], nums[i] = nums[i], nums[pind]
                pind += 1
        nums[pind], nums[right] = nums[right], nums[pind]# 最后将pivot放进来
        return pind


