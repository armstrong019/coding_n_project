# 这道题目很简单，基本上就是brute force 计算周围的neighbor的数量。 然后减去
class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    res += 4 # 首先加上四个边
                    num = self.num_neighbours(grid, i, j) # 计算neighbour的数量
                    res -= num # 减掉
        return res

    def num_neighbours(self, grid, i, j):
        num = 0
        if i > 0 and grid[i - 1][j] == 1:
            num += 1
        if i < len(grid) - 1 and grid[i + 1][j] == 1:
            num += 1
        if j > 0 and grid[i][j - 1] == 1:
            num += 1
        if j < len(grid[0]) - 1 and grid[i][j + 1] == 1:
            num += 1
        return num

# the diameter of the island
