# refer to knight shortest path： 从开始到结束的最短路径
# 这个是层遍历的典型题目， 另外这道题不需要单独记录visited， 直接改变grid即可

from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        all_rotten = self.find_all_rotten_oranges(grid)
        # 如果没有坏的，那么看里面是否有好的， 如果有， 返回-1， 否则返回0
        if not all_rotten:  # take care of the special case
            if any(1 in row for row in grid):
                return -1
            else:
                return 0
        q = deque([])
        for x0, y0 in all_rotten:
            q.append((x0, y0))
        dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        count = 0
        while q:
            count += 1
            level = []
            while q:
                level.append(q.popleft())
            for x, y in level:
                for dir in dirs:
                    new_x = x + dir[0]
                    new_y = y + dir[1]
                    if self.is_valid(grid, new_x, new_y):
                        q.append((new_x, new_y))
                        grid[new_x][new_y] = 2

        if any(1 in row for row in grid):
            return -1
        return count - 1

    def find_all_rotten_oranges(self, grid):
        List = []
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == 2:
                    List.append((x, y))
        return List

    def is_valid(self, grid, x, y):
        if x >= 0 and x <= len(grid) - 1 and y >= 0 and y <= len(grid[0]) - 1:
            if grid[x][y] == 1:
                return True
        return False

# 另一种写法
from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        all_rotten = self.find_all_rotten_oranges(grid)
        if not all_rotten:
            if any(1 in row for row in grid):
                return -1
            else:
                return 0
        q = deque([])
        for x0, y0 in all_rotten:
            q.append((x0, y0, 0))
        dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        count = 0
        while q:
            x, y, day = q.popleft()
            for dir in dirs:
                new_x = x + dir[0]
                new_y = y + dir[1]
                if self.is_valid(grid, new_x, new_y):
                    grid[new_x][new_y] = 2
                    q.append((new_x, new_y, day + 1))

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1
        return day

    def find_all_rotten_oranges(self, grid):
        List = []
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == 2:
                    List.append((x, y))
        return List

    def is_valid(self, grid, x, y):
        if x >= 0 and x <= len(grid) - 1 and y >= 0 and y <= len(grid[0]) - 1:
            if grid[x][y] == 1:
                return True
        return False
