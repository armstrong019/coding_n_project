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
    def subsets(self, nums):
        if not nums:
            return False
        self.result = []
        self.dfs(nums, [], 0)
        return self.result

    def dfs(self, nums, current_set, ind):
        self.result.append(current_set[:]) # 注意这里面没有return， termination 是自主完成的
        for i in range(ind, len(nums)):
            self.dfs(nums, current_set + [nums[i]], i + 1)

# 解法2， 逐次加入元素
def subsets(nums):
    result = [[]]
    for n in nums:
        for List in result[:]: #注意这里面的情况，result在loop里面是变化的，如果不copy的话会死循环
            result.append(List+[n])
    return result

# 解法2， 逐次加入元素
def subsets2(nums):
    result = [[]]
    for n in nums:
        for i in range(len(result)): # 在这里面没有这个问题。 这个range里面的值在第一次访问的时候就已经记住了 并且在loop里面不会变化。
            result.append(result[i] + [n])
    return result

print(subsets2([1,2,3]))

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for i in range(len(nums)):
            for j in range(len(res)): # 为什么这样写就可以， 因为这样相当于创建了一个新的object， 不存在res 改变的情况
                res.append([nums[i]]+res[j])
        return res
