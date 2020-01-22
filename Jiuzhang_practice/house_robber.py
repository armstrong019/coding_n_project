# DP【i️】 定义成 从0 到i 抢劫的最大数目。那么有两种情况如果我选择抢劫i 那么我的总收益就是dp【i-2】+当前的钱
# 如果不抢当前的钱， 那么总收益就和dp【i-1】
# 选择两个更大的那一个
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        is_robbed = [0 for _ in range(len(nums))]
        is_robbed[0] = 1
        dp = [0 for _ in range(len(nums))]
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            choose_i = nums[i] + dp[i - 2]
            not_i = dp[i - 1]
            dp[i] = max(choose_i, not_i)
        return dp[-1]

