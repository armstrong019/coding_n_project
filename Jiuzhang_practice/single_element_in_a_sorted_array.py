# You are given a sorted array consisting of only integers where every element appears exactly twice,
# except for one element which appears exactly once. Find this single element that appears only once.

class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lo = 0
        hi = len(nums) - 1
        while lo < hi: # stop when lo == hi
            mid = (lo + hi) // 2
            if nums[mid] == nums[mid + 1]:
                if self.is_odd(lo, mid - 1):
                    hi = mid - 1
                else:
                    lo = mid + 2
            elif nums[mid] == nums[mid - 1]:
                if self.is_odd(lo, mid - 2):
                    hi = mid - 2
                else:
                    lo = mid + 1
            else:
                return nums[mid]
        return nums[lo]

    def is_odd(self, start, end):
        if (end - start + 1) % 2 == 1:
            return True
        else:
            return False

# 这道题逻辑不难， 实践的时候要考虑corner cases
# 此题目不应该用九章的模版去做
# 大致思想是二分法将左右分成两部分， 和当前值一样的要么没有--直接返回， 要么在左边 要么在右边， 分类讨论
# termination condition： 可以想象倒数第二步 有三个情况： 112， 122， 121，
#   如果是112， 那么lo=hi=2， 如果122， 那么lo=hi=0， 如果121 直接返回2。
# 复杂度 O（lgn）空间O（1）

