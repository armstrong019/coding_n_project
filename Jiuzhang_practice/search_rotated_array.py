"""
DescriptionConsoleNote
62. Search in Rotated Sorted Array
Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Example
For [4, 5, 1, 2, 3] and target=1, return 2.

For [4, 5, 1, 2, 3] and target=0, return -1.

Challenge
O(logN) time
"""



class Solution(object):
    def search(self, A, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if A == []:
            return -1
        if len(A) == 1:
            if A[0] == target:
                return 0
            else:
                return -1
        start = 0
        end = len(A) - 1
        while start + 1 < end:
            mid = (start + end) / 2
            if A[mid] > A[start]:
                start = mid
            else:
                end = mid
        pivot = start

        if A[0] <= target and target <= A[pivot]:
            # note need to consider equal case here
            idx = self.binarySearch(A, 0, pivot, target)
        else:
            idx = self.binarySearch(A, pivot + 1, len(A) - 1, target)

        return idx

    def binarySearch(self, A, lo, hi, target):
        while lo + 1 < hi:
            mid = (lo + hi) / 2
            if A[mid] < target:
                lo = mid
            else:
                hi = mid
        if A[lo] == target:
            return lo
        if A[hi] == target:
            return hi
        return -1