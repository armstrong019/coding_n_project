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

# June 9th, 又写了一遍， 多考虑了x是取正还是负，其实不需要
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0
        if n < 0:
            return self.myPow(1 / x, -n)
        if x < 0: # 不需要考虑x 的取值问题
            if n % 2 == 0:
                return self.myPow(-x, n)
            else:
                return -self.myPow(-x, n)
        return self.Pow(x, n)

    def Pow(self, x, n):
        if n == 0:
            return 1
        if n == 1:
            return x
        if n % 2 == 0:
            return self.Pow(x, n // 2) ** 2
        else:
            return x * self.Pow(x, (n - 1) // 2) ** 2
