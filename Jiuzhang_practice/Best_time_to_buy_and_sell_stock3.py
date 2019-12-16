

# this solution the time limit exceed.
class Solution:
    def maxProfit(self, prices):
        T = len(prices)
        dp = [[0 for _ in range(T)] for _ in range(3)]  # 3 row, T col
        for k in range(1, 3):
            for t in range(1, T):
                no_sell = dp[k][t-1]
                max_sell = 0
                for j in range(t):
                    profit = prices[t] - prices[j] + dp[k - 1][j]
                    max_sell = max(max_sell, profit)
                dp[k][t] = max(no_sell, max_sell)
        print(dp)
        return dp[-1][-1]

x = Solution()
print(x.maxProfit([3,3,5,0,0,3,1,4]))

#在以上基础上进行优化， 参见https://www.youtube.com/watch?v=oDhu5uGq_ic&t=935s
# 主要是fix k， 让后列出t=2， t=3 的公式 找关系。
class Solution:
    def maxProfit(self, prices):
        T = len(prices)
        dp = [[0 for _ in range(T)] for _ in range(3)]  # 3 row, T col
        for k in range(1, 3):
            maxdiff = -prices[0]
            for t in range(1, T):
                no_sell = dp[k][t-1]
                dp[k][t] = max(no_sell, maxdiff+prices[t])
                maxdiff = max(maxdiff, dp[k-1][t]-prices[t])
        return dp[-1][-1]

x = Solution()
print(x.maxProfit([3,3,5,0,0,3,1,4]))

