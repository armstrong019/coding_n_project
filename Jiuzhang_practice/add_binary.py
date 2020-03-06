# 两种写法， 第二种比第一种少一个variable，但是个人喜欢第一种写法，比较直接

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        n1 = len(a)-1
        n2 = len(b)-1
        res = ''
        residual = 0
        while n1>=0 or n2>=0: # add 系列的一致写法， a or b，两者只要一个成立就好， 所以在运行过程中有可能一个不成立， 这就是为什么过程中要加上判断
            v=0
            if n1>=0:
                v+=int(a[n1])
            if n2>=0:
                v+=int(b[n2])
            v+= residual
            res+=str(v%2)
            residual = v//2
            n1=n1-1
            n2=n2-1
        if residual != 0:
            res += str(residual)
        return res[::-1]




class Solution:
    def addBinary(self, a: str, b: str) -> str:
        n1 = len(a) - 1
        n2 = len(b) - 1
        res = ''
        carry = 0
        while n1 >= 0 or n2 >= 0:
            if n1 >= 0:
                carry += int(a[n1])
            if n2 >= 0:
                carry += int(b[n2])
            res += str(carry % 2)
            carry = carry // 2
            n1 = n1 - 1
            n2 = n2 - 1

        if carry != 0:
            res += str(carry)
        return res[::-1]

#Jan 29
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a0 = a[::-1]
        b0 = b[::-1]

        i = 0
        res = ''
        carry = 0

        while i <= max(len(a0), len(b0)) - 1:
            val = carry
            if i <= len(a0) - 1:
                val += int(a0[i])
            if i <= len(b0) - 1:
                val += int(b0[i])
            carry = val // 2
            res += str(val % 2)
            i += 1
        if carry:
            res += str(carry)
        return res[::-1]
