class Solution:
    """
    @param s: input string
    @return: the longest palindromic substring
    """
    def longestPalindrome(self, s):
        # write your code here
        max_len = 1
        res = None
        for i in range(len(s)):
            temp = []
            for j in range(i, len(s)):
                substring = s[i:j+1]
                if substring==substring[::-1]:
                    if len(substring)>= max_len:
                        res = substring[:]
                        max_len =max(max_len, len(substring))
        return res
# 两种方法略有不同

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ''
        max_len = 1
        res = s[0]
        # brutal force
        for i in range(len(s) - 1):
            for j in range(i + 1, len(s)):
                substring = s[i:j + 1]
                # print(i,j,substring)
                if substring == substring[::-1]:
                    if len(substring) > max_len:
                        max_len = len(substring)
                        res = substring
        return res
