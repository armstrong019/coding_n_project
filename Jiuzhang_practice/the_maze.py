from collections import deque


class Solution:
    """
    @param maze: the maze
    @param start: the start
    @param destination: the destination
    @return: whether the ball could stop at the destination
    """

    def hasPath(self, maze, start, destination):
        # write your code here
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        stopped = [start]
        q = deque([start])  # stores the possible stopping pts
        while q:
            x, y = q.pop()
            if [x, y] == destination:
                return True
            for dr in dirs:
                new_x = x + dr[0]
                new_y = y + dr[1]
                while self.isvalid(new_x, new_y, maze):
                    new_x += dr[0]
                    new_y += dr[1]
                new_x -= dr[0]
                new_y -= dr[1]
                if [new_x, new_y] not in stopped:
                    q.append([new_x, new_y])
                    stopped.append([new_x, new_y])
        return False

    def isvalid(self, x, y, maze):
        if x >= 0 and x <= len(maze) - 1 and y >= 0 and y <= len(maze[0]) - 1 and maze[x][y] != 1:
            return True
        return False

# 思路是BFS 每次选取一个方向， 一直走直不能走为止。
# BFS：这道题需要注意的点是小球必须要能停到的点才可以， 途径点不能停的不可以。
# stopped 记录所有的停驻点。 如果停驻点曾经走过， 就不能再走 防止死循环，途径点不重要 不需要记录
