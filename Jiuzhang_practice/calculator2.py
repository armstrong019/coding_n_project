import re

# stack solution pretty straight forward
# this solution is good for coding
class Solution:
    def calculate(self, s: str) -> int:
        if not s:
            return 0
        s = s.replace(" ", "")  # remove all spaces
        L = re.findall('[0-9.]+|.', s)  # separate digits and operators 42/3 -- 【'42'，'/'，'3'】

        i = 0
        stack = []  # holds the values and + - operators (get rid of *,/)
        while i <= len(L) - 1:
            if L[i] != '*' and L[i] != '/':
                stack.append(L[i])
                i += 1
            else:
                val = stack.pop()
                if L[i] == '*':
                    stack.append(int(val) * int(L[i + 1]))
                else:
                    stack.append(int(val) / int(L[i + 1]))
                i += 2

        i = 0
        stack2 = []  # holds the values (get rid of +,-)
        while i <= len(stack) - 1:
            if stack[i] != '+' and stack[i] != '-':
                stack2.append(stack[i])
                i += 1
            else:

                val = stack2.pop()
                if stack[i] == '+':
                    stack2.append(int(val) + int(stack[i + 1]))
                else:
                    stack2.append(int(val) - int(stack[i + 1]))
                i += 2
        return int(stack2[0])

# 以下为标准答案， 写着容易但是理解难一点。
class Solution:
    def calculate(self, s: str) -> int:
        # 3-2*8+7/6
        # [3, -2, ]
        # [3,-16,]
        # [3, -16,7]
        # [3,-16,1]
        if not s:
            return 0
        temp = s.split(' ')
        s = ''.join(temp)
        s = '+' + s
        i = 0
        stack = []
        while i <= len(s) - 1:
            if s[i] == '+':
                digits = self.getInt(s, i)
                stack.append(int(digits))
                i += len(digits) + 1
            elif s[i] == '-':
                digits = self.getInt(s, i)
                stack.append(-int(digits))
                i += len(digits) + 1
            elif s[i] == "*":
                digits = self.getInt(s, i)
                val = stack.pop()
                stack.append(val * int(digits))
                i += len(digits) + 1
            elif s[i] == '/':
                digits = self.getInt(s, i)
                val = stack.pop()
                stack.append(int(val / int(digits)))
                i += len(digits) + 1
            else:
                print('error')

        return sum(stack)

    def getInt(self, s, i):
        ind = i + 1
        while ind <= len(s) - 1 and s[ind].isdigit():
            ind += 1
        return s[i + 1:ind]





