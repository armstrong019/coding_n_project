class Solution:
    """
    @param n: a positive integer
    @return: An integer
    """

    def numSquares(self, n):
        # write your code here
        if n == 1:
            return 1

        f = [0 for f in range(n + 1)]
        f[1] = 1
        for i in range(2, n + 1):
            temp = i  # the maximum value is i
            for j in range(1, i + 1):
                if j ** 2 <= i:
                    v = f[i - j ** 2] + 1
                    if v < temp: temp = v
                else:
                    f[i] = temp
                    break
        return f[n]

# DP solve this problem
# f[i] number of perfect squares sum
# f[i] = min{i, f[i-j**2]+1} (for all j**2<=i)