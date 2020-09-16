class Solution:
    """
    @param s: input string
    @return: the longest palindromic substring
    """
    def longestPalindrome(self, s):
        # write your code here
        max_len = 0
        res = None
        for i in range(len(s)):
            for j in range(i, len(s)):
                substring = s[i:j+1] # 最主要就是注意indexing
                if substring==substring[::-1]:
                    if len(substring)>= max_len:
                        res = substring[:]
                        max_len =max(max_len, len(substring))
        return res

# 此题还可以用动态规划
# Dynamic
# Programming
# 来解，根
# Palindrome
# Partitioning
# II
# 的解法很类似，我们维护一个二维数组
# dp，其中
# dp[i][j]
# 表示字符串区间[i, j]
# 是否为回文串，当
# i = j
# 时，只有一个字符，肯定是回文串，如果
# i = j + 1，说明是相邻字符，此时需要判断
# s[i]
# 是否等于
# s[j]，如果i和j不相邻，即
# i - j >= 2
# 时，除了判断
# s[i]
# 和
# s[j]
# 相等之外，dp[i + 1][j - 1]
# 若为真，就是回文串，通过以上分析，可以写出递推式如下：
#
# dp[i, j] = 1 if i == j
#
# = s[i] == s[j] if j = i + 1
#
# = s[i] == s[j] & & dp[i + 1][j - 1] if j > i + 1
#
# 这里有个有趣的现象就是如果我把下面的代码中的二维数组由
# int
# 改为
# vector < vector < int >> 后，就会超时，这说明
# int
# 型的二维数组访问执行速度完爆
# std
# 的
# vector
# 啊，所以以后尽可能的还是用最原始的数据类型吧。
#  len（s）= 4 的情况 （i，j）vistied 的顺序：
# （0，0）（1，1）（2，2）（3，3）-- i=0-3, j=i
# （0，1）（1，2）（2，3)-- i=0-2, j=i+1
# （0，2）（1，3）-- i=0-1, j = i+2
# （0，3）--i=0, j=i+3
# 由以上， 做4次， 每一次 i 行数都减少一位
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        dp = [[-1 for _ in range(len(s))] for _ in range(len(s))]
        count = len(s)
        max_len = 1
        res = s[0]
        while count > 0:
            for i in range(count):
                j = i + len(s) - count
                if i == j:
                    dp[i][j] = 1
                elif j == i + 1:
                    if s[i] == s[j]:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = 0
                else:
                    if s[i] == s[j] and dp[i + 1][j - 1] == 1:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = 0

                if dp[i][j] == 1:
                    if j - i + 1 > max_len:
                        max_len = j - i + 1
                        res = s[i:j + 1]
            count -= 1
        return res

