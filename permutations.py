class Solution:
    """
    see drew picture
    @param: nums: A list of integers.
    @return: A list of permutations.
    """

    def permute(self, nums):
        # write your code here
        if nums == []:
            return [[]]
        result = []
        self.helper(nums, [], result,3)
        return result

    def helper(self, nums, current_list, result,n):
        if len(current_list) ==n:
            result.append(current_list[:])
            return
        for i in range(len(nums)):
            self.helper(nums[i + 1:], current_list + [nums[i]], result,n)

nums = [1,2,3,9]
x = Solution()
print(x.permute(nums))

