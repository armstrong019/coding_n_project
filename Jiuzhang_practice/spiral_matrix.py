class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if matrix == []:
            return []
        dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        visited = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        n = len(matrix) * len(matrix[0])
        res = []

        # initial condition
        curr_dir = dirs[0]
        i = 0
        j = 0
        while len(res) < n:
            # current step, note that all the directions here are valid
            visited[i][j] = 1
            res.append(matrix[i][j])
            # update the next step
            if self.is_next_valid(i + curr_dir[0], j + curr_dir[1], matrix, visited):
                i += curr_dir[0]
                j += curr_dir[1]
            else:
                next_dir_index = (dirs.index([curr_dir[0], curr_dir[1]]) + 1) % 4
                i += dirs[next_dir_index][0]
                j += dirs[next_dir_index][1]
                curr_dir = dirs[next_dir_index]  # don't forget to update the current direction
        return res

    def is_next_valid(self, i, j, matrix, visited):
        if i >= 0 and i <= len(matrix) - 1 and j >= 0 and j <= len(matrix[0]) - 1 and visited[i][j] == 0:
            return True
        else:
            return False

# 第二种方法是纯数学计算， 没有additional的space需求， 居然做对了 佩服自己
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        res = [x for x in matrix[0]] # 第一步先假如第一行
        m = len(matrix)
        n = len(matrix[0])
        dirs = [[1, 0], [0, -1], [-1, 0], [0, 1]] # 四个direction交替进行
        steps = [m - 1, n - 1, m - 2, n - 2] # 四个方向的分别需要走的步子。例子：下m-1，左n-1，上m-2，右n-2，下m-3，左n-3 etc。
        x = 0
        y = n - 1
        i = 0
        while len(res) < m * n:
            current_dir = dirs[i]
            current_steps = steps[i]
            for t in range(current_steps):
                x = x + current_dir[0]
                y = y + current_dir[1]
                res.append(matrix[x][y])
            steps[i] = steps[i] - 2
            i = (i + 1) % 4
        return res
