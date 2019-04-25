# beat 100% of the submissions!

class Solution:
    """
    @param nums: an integer array
    @return: nothing
    """

    def moveZeroes(self, nums):
        # write your code here
        p0 = 0  # point to 0 elements
        p = 0  # point to nonezero elements
        # make sure p>=p0 all the time
        while p0 <= len(nums) - 1 and p <= len(nums) - 1:
            if nums[p0] == 0 and nums[p] != 0:
                nums[p0], nums[p] = nums[p], nums[p0]
                p0 += 1
                p += 1
            elif nums[p0] != 0:
                p0 += 1
                if p < p0: p = p0 # make sure you move p along with p0
            else:
                p += 1

# to pointer, one search for 0 another search for nonzero,
# the swap these two when applies
# make sure p>= p0 for always