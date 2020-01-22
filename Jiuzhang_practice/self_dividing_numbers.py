# 两种不同的写法
class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        res = []
        for n in range(left, right + 1):
            if self.self_dividing2(n):
                res.append(n)
        return res

    def self_dividing(self, n):
        number = n
        while n != 0:
            residual = n % 10
            if residual == 0 or number % residual != 0:
                return False
            n = n // 10
        return True

    def self_dividing2(self, n):

        for s in str(n):
            if s == '0' or n % int(s) != 0:
                return False
        return True
