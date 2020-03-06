# 这道题写了半天 debug 花了很久是因为细节写错了，image[sr][sc] 写成image[sc][sr] 细节不能错！！！
from collections import deque


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        q = deque([(sr, sc)])
        dirs = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        oldColor = image[sr][sc]
        image[sr][sc] = newColor

        while q:
            level = []
            while q:
                level.append(q.popleft())
            for x, y in level:
                for dir in dirs:
                    new_x = dir[0] + x
                    new_y = dir[1] + y
                    if self.isvalid(image, new_x, new_y, newColor, oldColor):
                        image[new_x][new_y] = newColor
                        q.append((new_x, new_y))
        return image

    def isvalid(self, image, new_x, new_y, newColor, oldColor):
        if new_x >= 0 and new_x <= len(image) - 1 and new_y >= 0 and new_y <= len(image[0]) - 1:
            if image[new_x][new_y] != newColor and image[new_x][new_y] == oldColor:
                return True
        return False

# DFS: 感觉实际操作 还是DFS好写
from collections import deque
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:

        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        oldColor = image[sr][sc]
        self.dfs(image, sr, sc, dirs, newColor, oldColor)
        return image

    def dfs(self, image, x, y, dirs, newColor, oldColor):
        image[x][y] = newColor
        for dir in dirs:
            new_x = dir[0] + x
            new_y = dir[1] + y
            if self.isvalid(image, new_x, new_y, newColor, oldColor):
                self.dfs(image, new_x, new_y, dirs, newColor, oldColor)

    def isvalid(self, image, new_x, new_y, newColor, oldColor):
        if new_x >= 0 and new_x <= len(image) - 1 and new_y >= 0 and new_y <= len(image[0]) - 1:
            if image[new_x][new_y] != newColor and image[new_x][new_y] == oldColor:
                return True
        return False
