# FB 高频题目，
# 这道题有两种解法， 一种是用stack space complexity 是 O(n)
# another method is O(1), 首先从左往右扫 去除多余的右括号 比如"）（）"， 然后再从右往左扫 去除不合理的左括号 比如 "（）（"

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # from left to right, remove extra ")"
        s = list(s) # 这里面必须用list（s）， 因为string 不支持assignment 比如s[i]='a'会报错。
        p = 0
        for i in range(len(s)):
            if s[i] == '(':
                p += 1
            elif s[i] == ')': # 如果右括号多于左括号，则不行
                if p == 0:
                    s[i] = ''
                else:
                    p -= 1
            else:
                pass

        # from right to left, remove extra "("
        q = 0
        for j in range(len(s) - 1, -1, -1):
            if s[j] == ')':
                q += 1
            elif s[j] == '(':
                if q == 0:
                    s[j] = ''
                else:
                    q -= 1
            else:
                pass

        return ''.join(s)

# stack 的做法。
# 这个借用valid parenthesis 的方法
# 这个stack 里面记录的是不合理的括号和他们的位置的信息， 然后再根据位置把他们remove掉
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        if not s:
            return ''
        stack = []  # this stack records the elements that will be removed
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(['(', i])
            elif s[i] == ')':
                if not stack:
                    stack.append([')', i]) # 记录不合理位置
                else:
                    if stack[-1][0] == '(':
                        stack.pop()
                    else:
                        stack.append([')', i])
            else:
                pass

        res = ''
        pos = 0 # 开始的位置
        while stack:
            _, delete_pos = stack.pop(0)
            res += s[pos:delete_pos]
            pos = delete_pos+1
        if pos <= len(s)-1: # 不要忘记把后面的string 也加进去
            res += s[pos:]

        return res

