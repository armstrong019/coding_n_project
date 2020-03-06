"""
41. Maximum Subarray
中文English
Given an array of integers, find a contiguous subarray which has the largest sum.

Example
Example1:

Input: [−2,2,−3,4,−1,2,1,−5,3]
Output: 6
Explanation: the contiguous subarray [4,−1,2,1] has the largest sum = 6.
Example2:

Input: [1,2,3,4]
Output: 10
Explanation: the contiguous subarray [1,2,3,4] has the largest sum = 10.
Challenge
Can you do it in time complexity O(n)?

Notice
The subarray should contain at least one number.
"""


class Solution:
    """
    @param nums: A list of integers
    @return: A integer indicate the sum of max subarray
    """
    def maxSubArray(self, nums):
        # write your code here
        max_sum = -sys.maxsize
        min_sum = 0  # minimum sum from 0 to position k (k<=current)， initially must be 0：只有一个数的例子
        prefix_sum = 0  # sum from position 0 to current
        for i in range(len(nums)):
            prefix_sum += nums[i]
            max_sum = max(max_sum, prefix_sum-min_sum)
            min_sum = min(prefix_sum, min_sum)
        return max_sum
# 注意要先更新maxsum 然后更新minsum： minsum 是前几个数的最小和


class Solution:
    """
    @param nums: A list of integers
    @return: A integer indicate the sum of max subarray
    """
    def maxSubArray(self, nums):
        # write your code here
        if nums == []:
            return None
        cumsum = [0 for i in range(len(nums))]
        cumsum[0] = nums[0]
        for i in range(1, len(nums)):
            cumsum[i] = cumsum[i-1]+nums[i]
        minsum = nums[0] # 初始值指向第一个
        maxsum = nums[0]
        for i in range(1,len(cumsum)):
            if minsum<=0:
                maxsum = max(maxsum, cumsum[i]-minsum)
            else:
                maxsum = max(maxsum, cumsum[i]) # 如果前面最小值大于0， 那么用cumsum[i]进行更新
            minsum = min(minsum, cumsum[i])
        return maxsum

# dp[i] 表示以i为结尾的包含i的 subarray sum
# if dp[i-1]<=0 dp[i] = nums[i], if dp[i-1]>0 dp[i] = dp[i]+nums[i]
# [-2, 1, -3, 4, 2, -1, 2, -3]
# [-2, 1, -2, 4, 6, 5, 7, 4]
# 这个方法是最好写也最方便的 在实际操作过程中应该采用这种方法
class Solution:
    """
    @param nums: A list of integers
    @return: A integer indicate the sum of max subarray
    """
    def maxSubArray(self, nums):
        max_sum = nums[0]
        prev_sum = nums[0]
        for i in range(1, len(nums)):
            if prev_sum <0:
                prev_sum = nums[i]
            else:
                prev_sum += nums[i]
            if max_sum < prev_sum:
                max_sum = prev_sum
        return max_sum





