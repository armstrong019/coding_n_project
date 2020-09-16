# 第一种解法，
class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # row_check[i][number] 记录在第i个row，number 这个数字是否已经被 visit过了，如果是：row_check[i][number]=1
        row_check = [[0 for i in range(9)] for i in range(9)]
        col_check = [[0 for i in range(9)] for i in range(9)]
        box_check = [[0 for i in range(9)] for i in range(9)]
        # k,m=0,0
        for i in range(0, 9):
            for j in range(0, 9):
                if board[i][j] != ".":
                    number = int(board[i][j])-1 # 减1是因为 index 是0-8，而board里面的值是1-9
                    k = i // 3 * 3 + j // 3
                    if row_check[i][number] or col_check[j][number] or box_check[k][number]:
                        return False
                    row_check[i][number] = col_check[j][number] = box_check[k][number] = 1
        return True



# 另一种解法 这种解法在memory上更加优化一点
class Solution:
    """
    @param board: the board
    @return: whether the Sudoku is valid
    """

    def isValidSudoku(self, board):
        used = set()

        # 先枚举行，检查每行是否合法
        for row in range(9):
            used = set()
            for col in range(9):
                if not self.check_valid(board[row][col], used):
                    return False

        # 先枚举列，检查每列是否合法
        for col in range(9):
            used = set()
            for row in range(9):
                if not self.check_valid(board[row][col], used):
                    return False

        # 每个分块的左上角的坐标为(i * 3, j * 3)
        for i in range(3):
            for j in range(3):
                used = set()
                for row in range(i * 3, i * 3 + 3):
                    for col in range(j * 3, j * 3 + 3):
                        if not self.check_valid(board[row][col], used):
                            return False

        return True

    # 检查字符是否有冲突
    def check_valid(self, c, used):
        if c == '.':
            return True
        if c in used:
            return False
        used.add(c)
        return True
