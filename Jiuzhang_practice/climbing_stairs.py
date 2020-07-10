class Solution:
    """
    @param n: An integer
    @return: An integer
    """
    def climbStairs(self, n):
        # write your code here
        if n == 0 or n==1:
            return n
        dp = [0 for _ in range(n+1)]
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n+1):
            dp[i] = dp[i-1]+dp[i-2]
        return dp[n]
#DP, no brainer
# 这道题是利用dp， dp[i] 要不就是从i-1走一步过来：dp[i-1], 要不就是i-2 走一步（2阶过来）： dp[i-2]
# 所以dp[i] = dp[i-1]+dp[i-2]
