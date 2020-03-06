# 这道题是费了很大功夫的一道题, 最后终于写出来了， 对深度搜索又有了新的理解
# coding structure： 我们需要keep 的状态有：
# 1。 ind：当前需要搜索字符对应在word 里面的index
# 2。 current_pos：当前的 position
# 需要keep track of visited 数组。
# design 如下： 我们make sure 每次搜索的时候ind 和position 都是对应的。也就是说如果下一个要找word里面的字符"B"， 那么
#              board 里面position 就一定对应"B"， 这样我们一上来就可以update visited 整个matrix=1
#              然后我们进行深搜（同样保证下一步也是成立的）， 如果有一支深搜成功了，那么就可以了
#              如果都没成功， 这时候重点来了： 要还原visited 将当前这一步mark 成没有 visited, 释放当前的visited cell 使他还能再次得以利用！！！
# 实例：[ABCE][SFES][ADEE] ABCESEEEFS

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board:
            return False

        # find the position of the first letter:
        positions = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    positions.append((i, j))
        for pos in positions:
            visited = [[0 for _ in range(len(board[0]))] for _ in range(len(board))]
            is_exist = self.dfs(0, pos, board, word, visited)
            if is_exist:
                return True
        return False

    def dfs(self, ind, current_pos, board, word, visited):
        visited[current_pos[0]][current_pos[1]] = 1
        if ind == len(word) - 1:
            return True

        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        for dir in dirs:
            new_x = current_pos[0] + dir[0]
            new_y = current_pos[1] + dir[1]
            if self.is_valid(new_x, new_y, board, visited, word, ind):
                is_true = self.dfs(ind + 1, (new_x, new_y), board, word, visited)
                if is_true:
                    return True
        visited[current_pos[0]][current_pos[1]] = 0
        return False

    def is_valid(self, x, y, board, visited, word, ind):
        if x >= 0 and x <= len(board) - 1 and y >= 0 and y <= len(board[0]) - 1 and visited[x][y] == 0:
            if board[x][y] == word[ind + 1]:
                return True
        return False

# 第二种写法：

# 这种写法好像比第一种要容易理解一点
# 我们不需要make sure 每次搜索的时候ind 和position 都是对应的，
# 这时候只需要在一开始判断一下。        if board[x][y] == word[ind]:
# 需要keep track of visited 数组。
# design 如下：
#              termination condition 是ind == len(word) - 1 and board[x][y] == word[-1]
#              然后我们进行深搜（同样保证下一步也是成立的）， 如果有一支深搜成功了，那么就可以了
#              如果都没成功， 这时候重点来了： 要还原visited 将当前这一步mark 成没有 visited, 释放当前的visited cell 使他还能再次得以利用！！！
# 实例：[ABCE][SFES][ADEE] ABCESEEEFS
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board:
            return False
        visited = [[0 for _ in range(len(board[0]))] for _ in range(len(board))]
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    is_exist = self.dfs(i, j, 0, board, word, visited, dirs)
                    if is_exist:
                        return True
        return False

    def dfs(self, x, y, ind, board, word, visited, dirs):
        if ind == len(word) - 1 and board[x][y] == word[-1]:
            return True
            visited[x][y] = 1
        else:
            return False

        for dir in dirs:
            new_x = x + dir[0]
            new_y = y + dir[1]
            if self.is_valid(new_x, new_y, visited):
                is_exist = self.dfs(new_x, new_y, ind + 1, board, word, visited, dirs)
                if is_exist:
                    return True
        visited[x][y] = 0
        return False

    def is_valid(self, x, y, visited):
        if x >= 0 and x <= len(visited) - 1 and y >= 0 and y <= len(visited[0]) - 1:
            if visited[x][y] == 0:
                return True
        return False
