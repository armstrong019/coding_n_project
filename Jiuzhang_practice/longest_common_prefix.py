# 九章的做法
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
                if j >= len(strs[i]) or strs[i][j] != temp: # 如果index 超过了当前word 的长度 或者对不上。
                    return res
            res += strs[0][j]
        return res

# 优化的做法
class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        if len(strs) == 0:
            return ""
        res = ""

        # 第一步是选出来最短的string 和他在list里面的index
        min_len = 1000000
        min_ind = -1
        for i in range(len(strs)):
            if len(strs[i]) < min_len:
                min_len = len(strs[i])
                min_ind = i

        # 第二部进行比较
        for j in range(min_len):
            letter = strs[min_ind][j] # 当前要比较的字符
            for i in range(strs):
                if strs[i][j]!= letter:
                    return res
            res += letter
        return res

