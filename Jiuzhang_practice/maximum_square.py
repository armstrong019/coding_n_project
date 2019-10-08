
# this version is dynamic programming
# time complexity O(mn), space complexity O(mn)
class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """

        if not matrix:
            return 0
        m = len(matrix)
        n = len(matrix[0])
        dp = [[0 for i in range(n)] for j in range(m)]
        maxlen = 0

        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    dp[i][j] = int(matrix[i][j])
                else:
                    if matrix[i][j] == "1":
                        dp[i][j] = min([dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]]) + 1
                    else:
                        dp[i][j] = 0
                if dp[i][j] > maxlen:
                    maxlen = dp[i][j]
        return maxlen ** 2


# this version is brute force, time complexity is O((mn)^2), space is O(1)
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # this time try brute force method
        self.maxlen = 0
        if not matrix:
            return 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == '1':
                    self.check_square(i, j, matrix) # check all possible squares
                else:
                    continue
        return self.maxlen

    def check_square(self, i, j, matrix):
        max_side_len = min(len(matrix) - i, len(matrix[0]) - j)
        for side_len in range(1, max_side_len + 1):
            is_all = self.is_all_ones(i, j, side_len, matrix) #check if all value equal to 1
            if is_all:
                self.maxlen = max(self.maxlen, side_len ** 2)

    def is_all_ones(self, i, j, side_len, matrix):
        for k in range(i, i + side_len):
            for l in range(j, j + side_len):
                if matrix[k][l] != "1":
                    return False
        return True



