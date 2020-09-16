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


# dp[i] 表示以i为结尾的包含i的 subarray sum
# if dp[i-1]<=0 dp[i] = nums[i], if dp[i-1]>0 dp[i] = dp[i]+nums[i]
# 难点就是这个判断的condition是跟dp[i-1]相关的，跟nums[i]不相关。
# [-2, 1, -3, 4, 2, -1, 2, -3]
# [-2, 1, -2, 4, 6, 5, 7, 4]
# 这个方法是最好写也最方便的 在实际操作过程中应该采用这种方法
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [nums[0]]
        for i in range(1, len(nums)):
            if dp[-1] > 0:
                dp.append(dp[-1]+nums[i])
            else:
                dp.append(nums[i])
        return max(dp)

#在此基础上进行空间优化
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        prev = nums[0]
        maxval = prev
        for i in range(1, len(nums)):
            if prev>0:
                prev= prev+nums[i]
            else:
                prev = nums[i]
            maxval = max(maxval, prev)
        return maxval



# Brute force 这种方法 超时了 O（N^2）
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums)<=1:
            return sum(nums)
        max_value = -sys.maxsize
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                sum_value = sum(nums[i:j+1])
                if sum_value > max_value:
                    max_value = sum_value
        return max_value
