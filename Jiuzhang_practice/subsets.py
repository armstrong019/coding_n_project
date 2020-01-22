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


# 另一种更为精简的写法。
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return False
        self.result = []
        self.dfs(nums, [], 0)
        return self.result

    def dfs(self, nums, current_set, ind):
        self.result.append(current_set[:])
        for i in range(ind, len(nums)):
            self.dfs(nums, current_set + [nums[i]], i + 1)
