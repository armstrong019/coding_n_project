# 可以买卖多次，很简单， 就是差价只要后面比前面的大， 就卖
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        total = 0
        for i in range(1, len(prices)):
            diff = prices[i]-prices[i-1]
            if diff>0:
                total+=diff
        return total

# 这个我自己想出来的DP解法超时了, 逻辑应该是对的。 但是复杂度是n^2
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        dp = [0 for _ in range(len(prices))]
        for i in range(1, len(prices)):
            max_val = dp[i-1] # do not sell
            for j in range(i):
                if prices[i]>prices[j]:
                    val = dp[j]+prices[i]-prices[j] # try sell
                    max_val = max(max_val,val)
            dp[i] = max_val
        return dp[-1]
