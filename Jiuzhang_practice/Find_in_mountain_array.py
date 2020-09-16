# 这道题的解法就是binary search， 注意题目里面相邻的两个点不可以是一样的值。
# 这道题就是作为三次binary search
# 参见 find peak element 那道题 (有可能有多个peak)
# 这道题只有一个 peak。
# Based on whether A[i-1] < A[i] < A[i+1], A[i-1] < A[i] > A[i+1], or A[i-1] > A[i] > A[i+1],
# we are either at the left side, peak, or right side of the mountain.
# We can binary search to find the peak.
# After finding the peak, we can binary search two more times to find whether the value occurs on either side of the peak.




# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
# class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

#
# You may recall that an array A is a mountain array if and only if:
#
# A.length >= 3
# There exists some i with 0 < i < A.length - 1 such that:
# A[0] < A[1] < ... A[i-1] < A[i]
# A[i] > A[i+1] > ... > A[A.length - 1]
# Given a mountain array mountainArr, return the minimum index such that mountainArr.get(index) == target.  If such an index doesn't exist, return -1.



class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        # find the peak index
        start = 0
        end = mountain_arr.length() - 1
        peak = -1
        while start + 1 < end:
            mid = (start + end) // 2
            lv = mountain_arr.get(mid - 1)
            mv = mountain_arr.get(mid)
            rv = mountain_arr.get(mid + 1)
            if lv < mv and mv < rv:
                start = mid
            elif lv > mv and mv > rv:
                end = mid
            else:
                peak = mid
                break
        if not peak:
            if mountain_arr.get(start) > mountain_arr.get(end):
                peak = start
            else:
                peak = end

        left_res, right_res = -1, -1
        if target >= mountain_arr.get(0) and target <= mountain_arr.get(peak):
            left_res = self.binary_search(0, peak, target, mountain_arr)
            print(left_res)
        if target <= mountain_arr.get(peak) and target >= mountain_arr.get(mountain_arr.length() - 1):
            right_res = self.binary_search_reverse(peak, mountain_arr.length() - 1, target, mountain_arr)

        if left_res == -1 and right_res == -1:
            return -1
        else:
            if left_res >= 0:
                return left_res
            else:
                return right_res

    def binary_search(self, start, end, target, mountain_arr):
        while start + 1 < end:
            mid = (start + end) // 2
            if mountain_arr.get(mid) == target:
                return mid
            elif mountain_arr.get(mid) > target:
                end = mid
            else:
                start = mid
        if mountain_arr.get(start) == target:
            return start
        if mountain_arr.get(end) == target:
            return end
        return -1

    def binary_search_reverse(self, start, end, target, mountain_arr):

        while start + 1 < end:
            mid = (start + end) // 2
            if mountain_arr.get(mid) == target:
                return mid
            elif mountain_arr.get(mid) > target:
                start = mid
            else:
                end = mid
        if mountain_arr.get(start) == target:
            return start
        if mountain_arr.get(end) == target:
            return end
        return -1













