

class Solution:
    """
    @param nums: A set of numbers
    @return: A list of lists. All valid subsets.
    """

    def subsetsWithDup(self, nums):
        nums.sort()
        self.nums = nums
        self.res = []
        self.dfs(0, [])
        return self.res

    def dfs(self, index, combination):
        if combination not in self.res:
            self.res.append(list(combination))
        # if index==len(nums):  # there is no difference adding this sentence
        #     return

        for i in range(index, len(self.nums)):
            combination.append(self.nums[i])
            self.dfs(i + 1, combination)
            combination.pop()
