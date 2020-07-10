"""
letter combination of phone number
一层一层的加， 每一次加一个letter。 见手机图片。
"""

# revisited May 14th

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []

        dic = {'2': ['a', 'b', 'c'],
               '3': ['d', 'e', 'f'],
               '4': ['g', 'h', 'i'],
               '5': ['j', 'k', 'l'],
               '6': ['m', 'n', 'o'],
               '7': ['p', 'q', 'r', 's'],
               '8': ['t', 'u', 'v'],
               '9': ['w', 'x', 'y', 'z']}

        result = []
        self.dfs('', 0, result, digits, dic)
        return result

    def dfs(self, current_str, ind, result, digits, dic):
        # ind: 表示下一个digit 在digits 里的index
        if ind == len(digits):
            result.append(current_str)
            return
        for letter in dic[digits[ind]]:
            self.dfs(current_str + letter, ind + 1, result, digits, dic)
