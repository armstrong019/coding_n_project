# class Solution(object):
#     def exist_path(self, grid, ori, dest):
#         nrow = len(grid)
#         ncol = len(grid[0])
#         if grid[ori[0]][ori[1]] == 1 or grid[dest[0]][dest[1]]==1:
#             return False
#         visited = [[0 for _ in range(ncol)] for _ in range(nrow)]
#         return self.dfs(grid, ori, dest, visited)
#
#     def dfs(self, grid, start, end, visited):
#         visited[start[0]][start[1]] = 1
#         if start == end:
#             return True
#         dirs = [[-1,0],[1,0],[0,-1],[0,1]]
#         for dir in dirs:
#             new_start = [start[0]+dir[0], start[1]+dir[1]]
#             if self.isvalid(grid, new_start, visited):
#                 is_route_exist = self.dfs(grid, new_start, end, visited)
#                 if is_route_exist: # 如果其中一个方向走通了， 那么立刻返回， 其他几个方向则不再考虑了
#                     return True
#         return False # 如果几个方向都没有走通， 那么则返回false
#
#     def isvalid(self, grid, s, visited):
#         nrow = len(grid)
#         ncol = len(grid[0])
#         if s[0]>=0 and s[0]<=nrow-1 and s[1]>=0 and s[1]<=ncol-1:
#             if grid[s[0]][s[1]]!=1 and visited[s[0]][s[1]]!=1:
#                 return True
#         return False
#
# x = Solution()
# Grid = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
# Grid2 = [[0,0,0,0],[0,1,1,1],[0,1,0,0],[0,1,0,0]]
#
# Ori = [0,0]
# Dest = [3,3]
#
# print(x.exist_path(Grid2, Ori, Dest))
# 这道题出自amazon的考试， 类似于the maze 那一道题目。
# 这道题即可以用dfs 也可以用bfs
# 如果选择dfs 那么这种情况容易出现死循环， 需要一个visted 来记录矩阵中的位置是否被走到过
# 另外一点需要考虑 termination condition：
#     假设在某个点有四个方向可以走，如果有一个方向走通了， 那么立刻返回true，其他方向不需要再继续考虑
#     如果四个方向都走不通那么返回false



# 下面的写法是bfs 的方法，两种写法都需要记录已经visited的点 否则会有死循环。
# bfs 写法相对dfs 简单一点
from collections import deque
class Solution2(object):
    def exist_path(self, grid, ori, dest):
        nrow = len(grid)
        ncol = len(grid[0])
        if grid[ori[0]][ori[1]] == 1 or grid[dest[0]][dest[1]] == 1:
            return False
        visited = [[0 for _ in range(ncol)] for _ in range(nrow)]
        return self.bfs(grid, ori, dest, visited)

    def bfs(self, grid, start, end, visited):
        q = deque([start])
        dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        while q:
            i,j = q.pop()
            if [i,j] == end:
                return True
            for dir in dirs:
                new_i = dir[0]+i
                new_j = dir[1]+j
                if self.isvalid(grid, [new_i, new_j], visited):
                    q.append([new_i, new_j])
                    visited[new_i][new_j] = 1
        return False

    def isvalid(self, grid, s, visited):
        nrow = len(grid)
        ncol = len(grid[0])
        if s[0]>=0 and s[0]<=nrow-1 and s[1]>=0 and s[1]<=ncol-1:
            if grid[s[0]][s[1]]!=1 and visited[s[0]][s[1]]!=1:
                return True
        return False

y = Solution2()
Grid = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
Grid2 = [[0,0,0,0],[0,1,1,1],[0,1,0,0],[0,1,0,0]]
Grid3 = [[0,0],[0,0]]
Ori = [0,0]
Dest = [3,3]

print(y.exist_path(Grid2, Ori, Dest))
