# 这道题的主要考察点就是如何记录 每个island的shape。
#具体做法是将每个岛屿的坐标记录 然后sort 然后转化成相对坐标。（选取左上角为基准点）
# 之后我们可以对一个岛屿的相对坐标转化成编码， 然后我们只要查找有多少不同编码就可以，

class Solution(object):
    def numDistinctIslands(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # write your code here
        if grid == []:
            return 0
        nrow = len(grid)
        ncol = len(grid[0])
        visited = [[0 for x in range(ncol)] for _ in range(nrow)]
        res = set()
        for i in range(nrow):
            for j in range(ncol):
                if visited[i][j] == 0 and grid[i][j]:
                    self.island = []
                    self.dfs(i, j, visited, grid)
                    island_code = self.encode_island()
                    res.add(island_code)
        return len(res)

    def dfs(self, i, j, visited, grid):
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        visited[i][j] = 1
        self.island.append([i, j])
        for d in dirs:
            if self.is_valid(i + d[0], j + d[1], grid, visited):
                self.dfs(i + d[0], j + d[1], visited, grid)

    def is_valid(self, i, j, grid, visited):
        if i >= 0 and i <= len(grid) - 1 and j >= 0 and j <= len(grid[0]) - 1:
            if visited[i][j] == 0 and grid[i][j]:
                return True
        return False

    def encode_island(self):
        self.island.sort(key=lambda x: [x[0], x[1]])
        dx = self.island[0][0]
        dy = self.island[0][1]
        encode = ''
        for i in range(len(self.island)):
            encode += str(self.island[i][0] - dx)
            encode += str(self.island[i][1] - dy)
        return encode
