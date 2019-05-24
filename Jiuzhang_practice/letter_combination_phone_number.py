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
        if digits == '':
            return []
        self.res = []
        self.dfs('', digits, 0)
        return self.res

    def dfs(self, curr_comb, digits, index):
        if index == len(digits):
            print(curr_comb)
            self.res.append(curr_comb)
            return
        for letter in keywords[digits[index]]:
            curr_comb = curr_comb + letter
            self.dfs(curr_comb, digits, index + 1)
            curr_comb = curr_comb[:-1]