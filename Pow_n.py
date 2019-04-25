class Solution:
    """
    @param x {float}: the base number
    @param n {int}: the power number
    @return {float}: the result
    """
    def myPow(self, x, n):
        # write your code here
        if n < 0:
            return self.myPow(float(1/x),-n)
        if n == 0:
            return 1
        if n == 1:
            return x
        a = self.myPow(x, n//2)
        b = self.myPow(x, n % 2)
        return a*a*b

# Power(x,n) binary approach