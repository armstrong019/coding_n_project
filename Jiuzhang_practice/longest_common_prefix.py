class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # loop through all the letter in first word one by one from left to right, then loop it through all the words
        # if you can't find the the letter in all words, the common prefix should be the string from beginning to that letter ()
        # not including that letter

        if len(strs) == 0:
            return ""
        res = ""

        for j in range(len(strs[0])):
            temp = strs[0][j]
            for i in range(1, len(strs)):
                if j >= len(strs[i]) or strs[i][j] != strs[0][j]:
                    return res
            res += strs[0][j]
        return res
