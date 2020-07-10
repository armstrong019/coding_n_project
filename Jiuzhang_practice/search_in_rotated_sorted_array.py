
# May 18th 2020 revisited,
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if nums == []:
            return -1
        # no rotating case
        if nums[0] <= nums[-1]: # is not rotated
            return self.binary_search(0, len(nums ) -1, target, nums)

        # find pivot here:
        start = 0
        end = len(nums ) -1
        while start + 1 <end:
            mid = (start +end )//2
            if nums[mid ]>= nums[start]:
                start = mid
            else:
                end = mid
        pivot = end # using this method, the pivot is the end point
        # 判断到底是在哪一个分支
        if target== nums[pivot]:
            return pivot
        elif target >nums[pivot] and target <= nums[-1]: # if the target is in between pivot and last position
            return self.binary_search(pivot, len(nums )-1, target, nums)
        elif target>= nums[0] and target <= nums[pivot-1]: # if the target is in between start and mid point
            return self.binary_search(0, pivot-1, target, nums)
        return -1

    def binary_search(self, start, end, target, nums):
        while start + 1 <end:
            mid = (start +end )//2
            if nums[mid]<= target:
                start = mid
            else:
                end = mid
        if target == nums[start]:
            return start
        elif target == nums[end]:
            return end
        return -1


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
#2020/01/22
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        start = 0
        end = len(nums)-1
        while start+1 < end:
            mid = (start+end)//2
            if nums[mid] == target:
                return mid
            if nums[start] <= nums[mid]: # left hand is sorted
                if target >= nums[start] and target<=nums[mid]:
                    end = mid
                else:
                    start = mid
            else: # right hand side is sorted
                if target <= nums[end] and target>=nums[mid]:
                    start = mid
                else:
                    end = mid
        if target == nums[start]:
            return start
        if target == nums[end]:
            return end
        return -1






