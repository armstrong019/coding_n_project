# 前缀加"+" 比较方便。

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
            digits = self.getDigits(s, i)
            if s[i] == '+':
                stack.append(int(digits))
            elif s[i] == '-':
                stack.append(-int(digits))
            elif s[i] == "*":
                val = stack.pop()
                stack.append(val * int(digits))
            elif s[i] == '/':
                val = stack.pop()
                stack.append(int(val / int(digits)))
            else:
                print('error')
            i += len(digits) + 1

        return sum(stack)

    def getDigits(self, s, i):
        # get the digits from index i+1
        ind = i + 1
        while ind <= len(s) - 1 and s[ind].isdigit():
            ind += 1
        return s[i + 1:ind]
