# Implement int sqrt(int x).
# Compute and return the square root of x, where x is guaranteed to be a non-negative integer.
# Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.
#
# 题目要求是只返回integer value， 而且x是大于一的数字。
# 经典的binary search

class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        start = 1
        end = x
        while start + 1 < end:
            mid = (start + end) // 2
            if mid ** 2 == x:
                return mid
            elif mid ** 2 > x:
                end = mid
            else:
                start = mid
        return start
