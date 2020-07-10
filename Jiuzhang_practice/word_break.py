# 下面写了三种方法 面试的时候写第二种。
# 第一二种 是dp思路基本一致 定义略有不同。
# 第三种是dfs， dfs 本质是遍历， 所以效率低


# 第一种方法好写但是不好记
class Solution:
    """
    @param: s: A string
    @param: dict: A dictionary of words dict
    @return: A boolean
    """

    # let dp[i] be whether the word is seperatable from 0-i exclude i

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

# dp[i] 表示 string 从0-i 包含i 是否可分,
# dp【0】 表示第一个字符是否存在于 字典里
# dp【j】= 1 if 以下两种情况成立：
#   1。 dp【i】 ==1 for i<j and s【i+1：j+1】in wordDict（也就是从i+1到j这些字符组成的词在字典里）
#   2。 s【：j+1】自己本身就是一个词
#   如果以上两种都不成立 dp【j】=0

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        # let dp[i] be whether the word is seperatable from 0-i includes i
        if not s:
            return False
        dp = [0 for _ in range(len(s))]
        dp[0] = s[0] in wordDict
        for j in range(1, len(s)):
            for i in range(0, j):
                if dp[i] == 1 and s[i + 1:j + 1] in wordDict:
                    dp[j] = 1
            if s[:j + 1] in wordDict:
                dp[j] = 1
        return dp[-1] == 1

# 遍历的dfs 写法 复杂度高
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """

        is_true = self.dfs(0, s, wordDict)
        return is_true

    def dfs(self, ind, s, wordDict):
        if ind == len(s):
            return True
        for i in range(ind, len(s)):
            if s[ind:i + 1] in wordDict:
                is_true = self.dfs(i + 1, s, wordDict)
                if is_true:
                    return True
        return False


