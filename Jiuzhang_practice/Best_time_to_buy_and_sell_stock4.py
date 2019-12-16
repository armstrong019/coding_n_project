# 两道题的结合
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices:
            return 0
        if k >= len(prices) - 1:
            return self.max_profit(prices)
        else:
            T = len(prices)
            dp = [[0 for _ in range(T)] for _ in range(k + 1)]
            print(dp)
            for i in range(1, k + 1):
                maxdiff = -prices[0]
                for t in range(1, T):
                    no_sell = dp[i][t - 1]
                    dp[i][t] = max(no_sell, maxdiff + prices[t])
                    maxdiff = max(maxdiff, dp[i - 1][t] - prices[t])
            return dp[-1][-1]

    def max_profit(self, prices):
        total = 0
        for i in range(1, len(prices)):
            diff = prices[i] - prices[i - 1]
            if diff > 0:
                total += diff
        return total
