# Given nums = [0,0,1,1,1,2,2,3,3,4],
#
# Your function should return length = 5, with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively.
# action needs to be inplace with O(1) extra memory
# 确实是比较绕的题目 多写几遍

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return None
        i = 0
        p0 = 1
        max_val = nums[0]
        while i <= len(nums)-1:
            if nums[i]<=max_val:
                i+=1
            else:
                nums[p0]=nums[i]
                p0+=1
                max_val = nums[i]
                i+=1
        return p0
