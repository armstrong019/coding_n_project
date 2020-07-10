#简单DP问题 dp[i][j] = min(dp[i][j - 1], dp[i - 1][j]) + grid[i][j]
# maximum path sum 也是可以的
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        nrow = len(grid)
        ncol = len(grid[0])
        dp = [[0 for _ in range(ncol)] for _ in range(nrow)]
        dp[0][0] = grid[0][0]
        for i in range(1, nrow):
            dp[i][0] = dp[i - 1][0] + grid[i][0] # 第一行的其实条件
        for j in range(1, ncol):
            dp[0][j] = dp[0][j - 1] + grid[0][j] # 第一列的起始条件
        for i in range(1, nrow):
            for j in range(1, ncol):
                dp[i][j] = min(dp[i][j - 1], dp[i - 1][j]) + grid[i][j] # 从上边来或者左边来最小的那个 加上当前值
        return dp[-1][-1]
