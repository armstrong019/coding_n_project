class Solution:
    """
    @param nums: A set of numbers
    @return: A list of lists
    """

    def subsets(self, nums):
        nums.sort()
        self.nums = nums
        self.res = []
        self.dfs(0, [])
        return self.res

    def dfs(self, index, combination):
        self.res.append(list(combination))
        # if index==len(nums):  # there is no difference adding this sentence
        #     return

        for i in range(index, len(self.nums)):
            combination.append(self.nums[i])
            self.dfs(i + 1, combination)
            combination.pop()

# two state variables, one track the current subsets, the other track the index for the start of search algorithm.
# for index i, the search start from index i+1 to the end index len(nums)-1, when ever we add a number we add the current state to the result