class Solution:
    """
    @param nums: An integer array
    @return: The length of LIS (longest increasing subsequence)
    """
    def longestIncreasingSubsequence(self, nums):
        # write your code here
        if not nums:
            return 0
        dp = [1]
        for i in range(1, len(nums)):
            temp = 1
            for j in range(i):
                if nums[i] > nums[j]:
                    temp = max(temp, dp[j]+1)
            dp.append(temp)
        return  max(dp)