# 题目前提是list里面没有重复， 如果有重复需要问清楚情况
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if target <= nums[i]:
                return i
            if target > nums[i]:
                i += 1
        return i

# binary search using bisect method
from bisect import bisect
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        ind = bisect(nums, target)
        if ind != 0 and nums[ind - 1] == target:
            return ind - 1
        return ind

# 手写方法， 注意这里面assume list 没有重复。
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target > nums[-1]:
            return len(nums)
        if target < nums[0]:
            return 0
        start = 0
        end = len(nums) - 1

        while start + 1 < end:
            mid = (start + end) // 2
            if target == nums[mid]:
                return mid
            elif target > nums[mid] and target < nums[mid + 1]:
                return mid + 1
            elif target < nums[mid]:
                end = mid
            else:
                start = mid
        if target == nums[start]:
            return start
        else:
            return start + 1

