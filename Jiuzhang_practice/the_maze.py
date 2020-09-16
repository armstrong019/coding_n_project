

# 思路是BFS 每次选取一个方向， 一直走直不能走为止。
# BFS：这道题需要注意的点是小球必须要能停到的点才可以， 途径点不能停的不可以。
# stopped 记录所有的停驻点。 如果停驻点曾经走过， 就不能再走 防止死循环，途径点不重要 不需要记录

# 第一种写法 这种写法的好处是一次处理一层，便于计算步数
from collections import deque

class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        if not maze:
            return False
        visited = [[0 for _ in range(len(maze[0]))] for _ in range(len(maze))]
        visited[start[0]][start[1]] = 1
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        q = deque([(start[0], start[1])])
        while q:
            level = []
            while q:
                current_pos = q.popleft()
                if current_pos[0] == destination[0] and current_pos[1] == destination[1]:
                    return True
                level.append(current_pos)

            # 这里容易出错的点是 一定要定义一个新点new_x and new_y。 不要改变 x and y
            for x,y in level:
                for dir in dirs:
                    temp_x = x
                    temp_y = y
                    while temp_x >= 0 and temp_x <= len(maze) - 1 and temp_y >= 0 and temp_y <= len(maze[0]) - 1 and \
                            maze[temp_x][temp_y] != 1:
                        temp_x += dir[0]
                        temp_y += dir[1]
                    next_x = temp_x - dir[0]
                    next_y = temp_y - dir[1]

                    if visited[next_x][next_y] == 0:
                        visited[next_x][next_y] = 1
                        q.append((next_x, next_y))
        return False


# 第二种写法， 个人比较喜欢第一种写法。
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
