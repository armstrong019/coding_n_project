class Solution:
    """
    @param: nums: a set of distinct positive integers
    @return: the largest subset
    """

    def largestDivisibleSubset(self, nums):
        # write your code here
        nums.sort()
        f = [1 for i in range(len(nums))]
        v = [[] for i in range(len(nums))]
        v[0] = [nums[0]]
        for i in range(1, len(nums)):
            flag = 0
            for j in range(i - 1, -1, -1):
                if nums[i] % nums[j] == 0:
                    f[i] = f[j] + 1
                    v[i] = v[j] + [nums[i]]
                    flag = 1
                    break
            if flag == 0:
                f[i] = 1
                v[i] = [nums[i]]
        ind = f.index(max(f))
        return v[ind]

# sort numbers first
# f[i] represents the divisble subset which the largest element is nums[i]
# v[i] represents the set itself
# for each i, from i-1 to 0, if we have nums[i]%nums[j] == 0, then we have find a larger subset with element i in it.