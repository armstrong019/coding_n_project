# 用DP去解。 注意0的处理。如果当前的数字是0， 那么他只能和前面一位组成数字。 如果不是0， 那么即可以分类讨论。
# https://www.cnblogs.com/grandyang/p/4313384.html
class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0
        dp = [0 for _ in range(len(s) + 1)]
        dp[0] = 1
        dp[1] = 1
        for i in range(2, len(dp)):
            if s[i - 1] == '0':
                if int(s[i - 2:i]) <= 26 and int(s[i - 2:i]) >= 10:
                    dp[i] = dp[i - 2]
                else:
                    return 0
            else:
                if int(s[i - 2:i]) <= 26 and int(s[i - 2:i]) >= 10:
                    dp[i] = dp[i - 1] + dp[i - 2]
                else:
                    dp[i] = dp[i - 1]
        return dp[-1]
