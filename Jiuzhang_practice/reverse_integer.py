# 这道题比较简单， 主要就是写下来计算过程 然后执行
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = 1
        if x<0:
            sign = -1
            x = -x

        num = 0
        while x>0:
            next_x = x//10
            residual = x % 10
            num = num*10+residual
            x = next_x
            if num > 2**31-1:
                return 0
        return sign*num




