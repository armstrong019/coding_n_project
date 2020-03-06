# adding two string together
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        n1 = len(num1) - 1
        n2 = len(num2) - 1
        residual = 0
        res = ''
        while n1 >= 0 or n2 >= 0: # 只要有一个值大于等于0 就继续。
            v = 0
            if n1 >= 0:  # 那么这里面就需要加判断。
                v += int(num1[n1])
            if n2 >= 0:
                v += int(num2[n2])
            v += residual

            res += str(v % 10)
            residual = v // 10
            n1 = n1 - 1
            n2 = n2 - 1

        if residual != 0: # 多出来的部分的处理
            res += str(residual)
        return res[::-1]

#解法一比较正规， 解法二仅供参考
class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        res = ''
        num1 = num1[::-1]
        num2 = num2[::-1]
        n1 = len(num1)
        n2 = len(num2)

        total_len = max(len(num1), len(num2))
        residual = 0
        for i in range(total_len):
            if i < n1 and i < n2:
                value = ord(num1[i]) - ord('0') + ord(num2[i]) - ord('0') + residual
            elif i < n1:
                value = ord(num1[i]) - ord('0') + residual
            elif i < n2:
                value = ord(num2[i]) - ord('0') + residual
            else:
                raise ValueError('value not exist')

            digit = value % 10
            residual = value // 10  # update residual
            res += str(digit)
        if residual != 0:
            res += str(residual)

        return res[::-1]


class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        number = ''
        carry = 0
        s1 = num1[::-1]
        s2 = num2[::-1]
        i = 0
        while i <= max(len(s1), len(s2)) - 1:
            val = carry
            if i <= len(s1) - 1:
                val += int(s1[i])
            if i <= len(s2) - 1:
                val += int(s2[i])
            number += str(val % 10)
            carry = val // 10
            i += 1
        if carry > 0:  # 多出来的部分的处理办法
            number += str(carry)
        return number[::-1]

