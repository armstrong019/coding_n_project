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
