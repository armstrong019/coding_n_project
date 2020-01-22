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

# dfs 用一个string s来记录。状态变量是combination（已经考虑的，是palindrome的部分， 和s：还未处理的s的部分

# 类似版本
class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        if not s:
            return []
        self.result = []
        self.dfs([], s)
        return self.result

    def dfs(self, current_palindrome, rest_string):
        if rest_string == '':
            self.result.append(current_palindrome[:])
            return
        for i in range(len(rest_string)):
            words = rest_string[:i + 1] #最主要的是把index弄清楚，不要出错。一定要取道第i 位， 因为必须保证不能有空字符'' 出现
            if words == words[::-1]:
                self.dfs(current_palindrome + [words], rest_string[i + 1:])
