# 把数字加起来 比较 0+1+2+。。。+n 的差值
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum_nums = sum(nums)
        actual_sum = sum([i for i in range(len(nums) + 1)])
        return actual_sum - sum_nums

