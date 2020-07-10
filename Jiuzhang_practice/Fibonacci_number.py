

# 简单题
class Solution(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N <= 1:
            return N
        pprev = 0
        prev = 1
        for i in range(2, N + 1):
            val = prev + pprev
            pprev = prev
            prev = val

        return val
