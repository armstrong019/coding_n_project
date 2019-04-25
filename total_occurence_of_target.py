class Solution:
    """
    @param A: A an integer array sorted in ascending order
    @param target: An integer
    @return: An integer
    """

    def totalOccurrence(self, A, target):
        # write your code here
        if A == []:
            return 0
        x = self.first_position(A, target)
        y = self.last_position(A, target)
        if x == -1 and y == -1:
            return 0
        return y - x + 1

    def last_position(self, nums, target):
        start = 0
        end = len(nums) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] <= target:
                start = mid
            else:
                end = mid
        if target == nums[end]:
            return end
        elif target == nums[start]:
            return start
        else:
            return -1

    def first_position(self, nums, target):
        start = 0
        end = len(nums) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] >= target:
                end = mid
            else:
                start = mid
        if target == nums[start]:
            return start
        if target == nums[end]:
            return end
        return -1

# using binary search twice. find the first and last position of the target