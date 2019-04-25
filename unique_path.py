
class Solution:
    """
    @param m: positive integer (1 <= m <= 100)
    @param n: positive integer (1 <= n <= 100)
    @return: An integer
    """

    def uniquePaths(self, m, n):
        # write your code here
        dp = {} # using a hashtable
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    dp[(i,j)] = 1
                else:
                    dp[(i,j)] = dp[(i-1,j)] + dp[(i,j-1)]
        return dp[(m-1,n-1)]



x=Solution()
x.uniquePaths(3,3)