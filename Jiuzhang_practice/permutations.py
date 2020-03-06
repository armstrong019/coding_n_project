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

# compelxity O(n!): 第一层node有n个节点， 第二层每个node有n-1个节点， 第三层每个node有n-2 个节点，
# 那么一共有n*n-1*n-2*...*1 = n!个节点
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        self.result = []
        self.dfs([], nums)
        return self.result

    def dfs(self, current_perm, rest):
        if rest == []:
            self.result.append(current_perm[:])
        for i in range(len(rest)):
            self.dfs(current_perm + [rest[i]], rest[:i] + rest[i + 1:])

# checked on March 1st
