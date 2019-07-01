from collections import deque


class Solution:
    """
    @param s: A string
    @return: whether the string is a valid parentheses
    """

    def isValidParentheses(self, s):
        # write your code here
        paren_dict = {'(': ')', '{': '}', '[': ']'}
        stack = deque()
        for i in s:
            if i in paren_dict.keys():
                stack.append(i)
            if i in paren_dict.values():
                if len(stack) == 0:
                    return False
                else:
                    p = stack.pop()
                    if paren_dict[p] != i:
                        return False
        if len(stack) > 0:
            return False
        return True

# using stack is good
# 有几个termination condition：
        # #1。有一个右括号，但是stack为空，如果有有括号 stack 不空，但是对应不上、
        # 2。 遍历完成还有多余的括号。