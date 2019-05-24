class Solution:
    """
    @param obstacleGrid: A list of lists of integers
    @return: An integer
    """

    def uniquePathsWithObstacles(self, obstacleGrid):
        # write your code here
        m = len(obstacleGrid )
        n = len(obstacleGrid[0])
        dp = [[0 for i in range(n)] for j in range(m)]
        print(dp)
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[m - 1][n - 1]


x=Solution()
x.uniquePathsWithObstacles([[0,0],[0,0],[0,0],[1,0],[0,0]])
