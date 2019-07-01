class Solution:
    """
    @param: s: A string
    @param: dict: A dictionary of words dict
    @return: A boolean
    """

    def wordBreak(self, s, dict):
        if len(dict) == 0:
            return len(s) == 0

        dp = [False for i in range(len(s) + 1)]
        dp[0] = True
        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j] and s[j:i] in dict:
                    dp[i] = True

        return dp[-1]

# dp[i] 表示 string[:i] 是否可分,

