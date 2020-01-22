class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        number = x
        v = 0
        while x > 0:
            residual = x % 10
            v = v * 10 + residual
            x = x // 10

        return v == number
