
# 按照答案照猫画虎写的， 大概意思是记录分割符的位置， 然后计算每两个分割符直接的元素个数 取得最大的
# 大概的意思就是用stack loop through s： 如果当前为"（"： 将index押入栈，
# 如果为"）"： 一种情况是栈为空，那么押入栈（这个就是分割符），
#             如果不为空， 那么检查栈顶元素是否为"（"， 如果是将栈钉元素出栈
#             如果为空， 那么将当前index押入栈 （这个就是分割符）。

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s:
            return 0
        max_len = 0
        stack = [-1]
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                if stack == [-1]:
                    stack.append(i)
                else:
                    if s[stack[-1]] == '(':
                        stack.pop()
                    else:
                        stack.append(i)
        stack.append(len(s))
        max_len = 0
        for j in range(1, len(stack)):
            current_len = stack[j] - stack[j - 1] - 1
            max_len = max(max_len, current_len)
        return max_len
