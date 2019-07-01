"""DFS算法尽可能深的搜索每个树枝，一直搜索到最深的那一个为止。
当DFS走到一条死路（再也没有可能的合法移动的方式）时，它会沿着树返回直到该节点有路可走。然后继续往深处探索。
dfs 的结构特点：
def dfs(a):
    dfs(b)
    dfs(c)

这种结构创建了一种树的结构， 每次搜索到最深的节点 直到最后一个节点完成 返回上一层
"""


class Solution:
    """
    @param grid: a boolean 2D matrix
    @return: an integer
    """

    def numIslands(self, grid):
        # write your code here
        if grid == []:
            return 0
        nrow = len(grid)
        ncol = len(grid[0])
        visited = [[0 for x in range(ncol)] for _ in range(nrow)]
        count = 0
        for i in range(nrow):
            for j in range(ncol):
                if visited[i][j] == 0 and grid[i][j]:
                    count += 1
                    self.dfs(i, j, visited, grid)
        return count

    def dfs(self, i, j, visited, grid):
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        visited[i][j] = 1
        for d in dirs:
            if self.is_valid(i + d[0], j + d[1], grid, visited):
                self.dfs(i + d[0], j + d[1], visited, grid)

    def is_valid(self, i, j, grid, visited):
        if i >= 0 and i <= len(grid) - 1 and j >= 0 and j <= len(grid[0]) - 1:
            if visited[i][j] == 0 and grid[i][j]:
                return True
        return False

x=Solution()
grid = [[1,1,0,0,0],[0,1,0,0,1],[0,0,0,1,1],[0,0,0,0,0],[0,0,0,0,1]]
res = x.numIslands(grid)
print(res)


# 这到题使用了dfs 有几个要点：
# 第一： 我们用一个叫visited的表格记录当前位置是否被询问过，关于这个具体定义有两种： 第一种是将所有点在最后结束时候都mark成1，第二种是只将有island的点mark成1
# 第二种记录方法比较直接
# 第二：什么时候count+1： 当前island第一次被visited （visited[i][j] == 0 and grid[i][j]）
# 第三： 我们用了一个helper function去判断下一个点是否可行，是否需要继续进行dfs搜索： 当前点必须是可以走的点并且没有被visited过 （visited[i][j] == 0 and grid[i][j]）
# 第四： 关于is_valid 的定义：position valid， 是可以走的， 并且没有被visited过