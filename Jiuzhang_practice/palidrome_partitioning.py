class Solution:
    """
    @param: s: A string
    @return: A list of lists of string
    """

    def partition(self, s):
        # write your code here
        if not s:
            return []
        self.res = []
        self.dfs([], s)
        return self.res

    def dfs(self, combination, s):
        if len(s) == 0:
            if combination not in self.res:
                self.res.append(combination[:])
                return
        for i in range(len(s)):
            string = s[:i + 1]
            if string == string[::-1]:  # 如果当前的字符串是palindrome， 才可以加入到combination里面， 然后继续深搜
                combination.append(string)
                self.dfs(combination, s[i + 1:])
                combination.pop()

# dfs 用一个string s来记录。状态变量是combination（已经考虑的，是palindrome的部分， 和s： 还未处理的s的部分