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

