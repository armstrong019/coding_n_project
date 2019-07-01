class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        row_check = [[0 for i in range(9)] for i in range(9)]
        col_check = [[0 for i in range(9)] for i in range(9)]
        box_check = [[0 for i in range(9)] for i in range(9)]
        # k,m=0,0
        for i in range(0, 9):
            for j in range(0, 9):
                if board[i][j] != ".":
                    m = int(board[i][j]) - 1
                    k = i // 3 * 3 + j // 3
                    if row_check[i][m] or col_check[j][m] or box_check[k][m]:
                        return False
                    row_check[i][m] = col_check[j][m] = box_check[k][m] = 1
        return True