class Solution:
    """
    @param: nums: A list of integers.
    @return: A list of permutations.
    """

    def permute(self, nums):
        # write your code here
        if nums == None:
            return None
        self.result = []
        self.dfs([], nums)
        return self.result

    def dfs(self, curr_list, nums):
        if nums == []:
            self.result.append(curr_list[:])
            return
        for i in range(len(nums)):
            curr_list.append(nums[i])
            self.dfs(curr_list, nums[:i]+nums[i + 1:])
            curr_list.pop()

# dfs。 state 包含两个部分， 一个是当前的permutation， 另一个是还未被用到的list of numbers
# 每次从未被用到的list of numbers选择一个number， 加到当前的permutation里面


