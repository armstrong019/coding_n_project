class Solution:
    """
    @param nums: an integer array
    @return: nothing
    this version is from JY
    """

    def moveZeroes(self, nums):
        # write your code here
        idx_0, idx_num = 0, 1
        while idx_num < len(nums):
            while idx_0 < len(nums) and nums[idx_0] != 0:
                idx_0 += 1

            while idx_num < len(nums) and nums[idx_num] == 0:
                idx_num += 1

            if idx_0 == len(nums) or idx_num == len(nums):
                break

            if idx_num > idx_0:
                nums[idx_0], nums[idx_num] = nums[idx_num], nums[idx_0]

            else:
                idx_num = idx_0 + 1

