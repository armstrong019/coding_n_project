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