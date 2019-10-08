class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """

        result = []
        nums = [lower - 1] + nums + [upper + 1] # lower-1 and upper +1 should be included in the list

        i = 1
        while i < len(nums):
            if nums[i] - nums[i - 1] <= 1:
                i += 1
            elif nums[i] - nums[i - 1] == 2:
                result.append(''.join(str(nums[i] - 1)))
                i += 1
            else:
                result.append(''.join([str(nums[i - 1] + 1), '->', str(nums[i] - 1)]))
                i += 1

        return result
