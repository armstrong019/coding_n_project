class Solution:
    """
    @param nums: a rotated sorted array
    @return: the minimum number in the array
    """
    def findMin(self, nums):
        # write your code here
        start = 0
        end = len(nums)-1
        while start+1 <end:
            mid = (start+end)//2
            if nums[mid]<=nums[end]:
                end = mid
            elif nums[mid]>= nums[start]:
                start = mid
            else:
                break
        return min(nums[start], nums[end])

class Solution:
    def find_minimum_index(self, A):
        start,end=0,len(A)-1
        while start+1<end:
            mid=(start+end)//2
            if A[mid]>= A[start]:
                start = mid
            else:
                end = mid
        if A[start]<= A[end]:
            return start
        else:
            return end

class Solution:
    # @param nums: a rotated sorted array
    # @return: the minimum number in the array
    def findMin(self, nums):
        if not nums:
            return -1
        start, end = 0, len(nums) - 1
        target = nums[-1]
        while start + 1 < end:  # 用来控制区间大小
            mid = (start + end) // 2
            if nums[mid] <= target:  # 如果mid位置上的数字小于等于最右端的数字时，区间向左移动
                end = mid
            else:
                start = mid
        return min(nums[start], nums[end])

# there are two solutions to this problem
# the first one is to set the last value to be the target(a reference value), see comments
# the second one is to make comparsion between mid and end or start value(see method 1 and 2).