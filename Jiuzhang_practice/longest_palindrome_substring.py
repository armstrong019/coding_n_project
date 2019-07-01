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