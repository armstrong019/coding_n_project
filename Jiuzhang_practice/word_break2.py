class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        self.result = []
        self.dfs([], s, wordDict)
        return self.result

    def check(self, s, dict):
        dp = [False for i in range(len(s) + 1)]
        dp[0] = True
        for i in range(1, len(s) + 1):
            for k in range(0, i):
                if dp[k] and s[k:i] in dict:
                    dp[i] = True
        return dp[len(s)]

    def dfs(self, current_path, current_s, wordDict):
        if self.check(current_s, wordDict):
            if current_s == '':
                res = ' '.join(current_path)
                self.result.append(res)
                return
            for i in range(len(current_s) + 1):
                if current_s[:i] in wordDict:
                    self.dfs(current_path + [current_s[:i]], current_s[i:], wordDict)

