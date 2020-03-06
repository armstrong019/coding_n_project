class Solution:
    """
    @param grid: a list of lists of integers
    @return: An integer, minimizes the sum of all numbers along its path
    """

    def minPathSum(self, grid):
        # write your code here
        m = len(grid)  # rows
        n = len(grid[0])
        dp = [[0 for i in range(n)] for j in range(m)]

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[i][j] = grid[i][j]
                elif i == 0 and j > 0:
                    dp[i][j] = dp[i][j - 1] + grid[i][j]
                elif i > 0 and j == 0:
                    dp[i][j] = dp[i - 1][j] + grid[i][j]
                else:
                    dp[i][j] = min([dp[i - 1][j], dp[i][j - 1]]) + grid[i][j]
        return dp[-1][-1]


from collections import deque

# 这道题我同样还用dfs 解了一次, 同样可以解 但是速率差
from collections import deque
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dirs = [(0, 1), (1, 0)]
        dist = {}
        dist[(0, 0)] = grid[0][0]
        q = deque([(0, 0)])
        while q:
            x, y = q.popleft()
            for dir in dirs:
                new_x = dir[0] + x
                new_y = dir[1] + y
                if new_x >= 0 and new_x <= len(grid) - 1 and new_y >= 0 and new_y <= len(grid[0]) - 1:
                    current_path_sum = grid[new_x][new_y] + dist[(x, y)]
                    if (new_x, new_y) not in dist:
                        dist[(new_x, new_y)] = current_path_sum
                        q.append((new_x, new_y))
                    else:
                        if current_path_sum < dist[(new_x, new_y)]:
                            dist[(new_x, new_y)] = current_path_sum
                            q.append((new_x, new_y))
        return dist[(len(grid) - 1, len(grid[0]) - 1)]




