"""
letter combination of phone number
一层一层的加， 每一次加一个letter。 见手机图片。
"""
keywords = {
    '2': ['a', 'b', 'c'],
    '3': ['d', 'e', 'f'],
    '4': ['g', 'h', 'i'],
    '5': ['j', 'k', 'l'],
    '6': ['m', 'n', 'o'],
    '7': ['p', 'q', 'r', 's'],
    '8': ['t', 'u', 'v'],
    '9': ['w', 'x', 'y', 'z'], }


class Solution:
    """
    @param digits: A digital string
    @return: all posible letter combinations
    """

    def letterCombinations(self, digits):
        # write your code here
        result = []
        if not digits:
            return []
        self.dfs(digits, 0, '', result)
        return result

    def dfs(self, digits, index, string, result):
        if index == len(digits):
            result.append(string)
            return
        for i in keywords[digits[index]]:
            self.dfs(digits, index + 1, string + i, result)
