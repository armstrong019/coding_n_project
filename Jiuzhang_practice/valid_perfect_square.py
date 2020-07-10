# 直接套用二分法就可以
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        start = 1
        end = num
        while start + 1 < end:
            mid = (start + end) // 2
            if mid ** 2 == num:
                return True
            elif mid ** 2 < num:
                start = mid
            else:
                end = mid

        if start ** 2 == num or end ** 2 == num:
            return True
        return False
