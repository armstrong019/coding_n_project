"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""
from collections import deque


class Solution:
    """
    @param grid: a chessboard included 0 (false) and 1 (true)
    @param source: a point
    @param destination: a point
    @return: the shortest path
    """

    def shortestPath(self, grid, source, destination):
        # write your code here
        distance = {(source.x, source.y): 0}
        queue = deque([source])
        directions = [(-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2)]

        while queue:
            pt = queue.popleft()
            if pt.x == destination.x and pt.y == destination.y:
                return distance[(pt.x, pt.y)]
            for dir in directions:
                next_x = dir[0] + pt.x
                next_y = dir[1] + pt.y
                if (next_x, next_y) in distance:
                    continue

                if next_x >= 0 and next_x <= len(grid) - 1 and next_y >= 0 and next_y <= len(grid[0]) - 1 and \
                                grid[next_x][next_y] == 0:
                    distance[(next_x, next_y)] = distance[(pt.x, pt.y)] + 1
                    queue.append(Point(next_x, next_y))
        return -1


# find the shortest path between source and destination.
# using BFS search. create a queue with starting point as the source and keep searching.
# condition on when to add the new point to the queue:
# 1. when (new_x,new_y) index is valid, 2. this new point is is valid on the chessboard--0 means can move
# 3. when (new_x and new_y) has not been visited before. If it has been visited, we do not add to the queue, otherwise there maybe infinite loop


# below is an alternative approach without using hashtable
from collections import deque
class Solution:
    """
    @param grid: a chessboard included 0 (false) and 1 (true)
    @param source: a point
    @param destination: a point
    @return: the shortest path
    """

    def shortestPath(self, grid, source, destination):
        # write your code here
        q = deque([source])
        count = -1 # initialize length to have value -1
        dirs = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]
        nrow = len(grid)
        ncol = len(grid[0])
        visited = [[0 for _ in range(ncol)] for _ in range(nrow)] # use is visited to avoid infinite loop.
        while q:
            count += 1 # here we add 1 to the number of steps
            for i in range(len(q)):
                loc = q.popleft()
                if loc.x == destination.x and loc.y == destination.y:
                    return count
                for dr in dirs:
                    x = loc.x + dr[0]
                    y = loc.y + dr[1]
                    if self.isvalid(x, y, grid, visited):
                        visited[x][y] = 1
                        q.append(Point(x, y))
        return -1

    def isvalid(self, x, y, grid, visited):
        if x >= 0 and x <= len(grid) - 1 and y >= 0 and y <= len(grid[0]) - 1:
            if grid[x][y] == 0 and visited[x][y] == 0:
                return True
        return False

