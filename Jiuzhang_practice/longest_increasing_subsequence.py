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

# use DP. let dp[i] 以i这个位置为结尾的最长subsequence值。
# dp[i] = max(dp[j] + 1 for j<i and nums[j]<nums[i], 1) 1 means no j with nums[j]<nums[i]， the longest is itself
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        dp = [1 for _ in range(len(nums))]
        for i in range(1,len(nums)):
            max_length_i = 1
            for j in range(i):
                if nums[j]<nums[i]:
                    value = dp[j]+1
                else:
                    value = 1
                max_length_i = max(max_length_i, value)
            dp[i] = max_length_i
        return max(dp)
