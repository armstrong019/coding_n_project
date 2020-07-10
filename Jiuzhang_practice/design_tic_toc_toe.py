# 算法复杂度： O（1）
class TicTacToe:

    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        self.rows = [0] * n #每一个点记录 实际grid每一行的加和值
        self.cols = [0] * n
        self.diag1 = 0  # 记录 diagonal 的加和值
        self.diag2 = 0  # 记录 reverse diagonal 的加和值
        self.n = n

    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """
        if player == 1:
            int_val = 1 # 如果是第一个player 就在相对位置加1。
        else:
            int_val = -1 # 第二个player 减1

        self.rows[row] += int_val
        self.cols[col] += int_val
        if row == col:
            self.diag1 += int_val
        if row == self.n - col - 1:
            self.diag2 += int_val

        exp = int_val * self.n  # 在这里看 值为n 或者-n 是否存在
        if self.rows[row] == exp or self.cols[col] == exp or self.diag1 == exp or self.diag2 == exp:
            return player
        return 0
------------------- 写法2  line 36-39
        if int_val*self.n in self.rows or int_val*self.n in self.cols or abs(self.diag1)==self.n or  abs(self.diag2)==self.n:
            return player
        return 0

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)

# 之前写的一个brute force版本超时了
from collections import Counter

class TicTacToe(object):

    def __init__(self, n):
        """
        Initialize your data structure here.
        :type n: int
        """
        self.n = n
        self.grid = [[-1 for _ in range(n)] for _ in range(n)]

    def move(self, row, col, player):
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        :type row: int
        :type col: int
        :type player: int
        :rtype: int
        """
        self.grid[row][col] = player
        # check for rows
        is_winning_rows = self.check_rows(player)
        is_winning_columns = self.check_cols(player)
        is_winning_diags = self.check_diags(player)
        result = is_winning_rows or is_winning_columns or is_winning_diags
        if result is not None:
            return result
        return 0

    def check_rows(self, player):
        for i in range(self.n):
            cnt = Counter([self.grid[i][j] for j in range(self.n)])
            if len(cnt) == 1 and list(cnt.keys())[0] != -1:
                return player
        return None

    def check_cols(self, player):

        for i in range(self.n):
            cnt = Counter([self.grid[j][i] for j in range(self.n)])
            if len(cnt) == 1 and list(cnt.keys())[0] != -1:
                return player
        return None

    def check_diags(self, player):
        cnt1 = Counter([self.grid[j][j] for j in range(self.n)])
        if len(cnt1) == 1 and list(cnt1.keys())[0] != -1:
            return player
        cnt2 = Counter([self.grid[j][self.n - j - 1] for j in range(self.n)])
        if len(cnt2) == 1 and list(cnt2.keys())[0] != -1:
            return player
        return None

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
