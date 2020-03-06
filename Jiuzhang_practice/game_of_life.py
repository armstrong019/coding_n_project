# 就是按照逻辑搞
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return []

        new_board = [[0 for _ in range(len(board[0]))] for _ in range(len(board))]
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1), (-1, -1), (-1, 1), (1, 1), (1, -1)]
        for i in range(len(new_board)):
            for j in range(len(new_board[0])):
                num_live_nbs = 0
                for dir in dirs:
                    nb_position_row = dir[0] + i
                    nb_position_col = dir[1] + j
                    if self.isvalid(nb_position_row, nb_position_row, board):
                        if board[nb_position_row][nb_position_col] == 1:
                            num_live_nbs += 1
                if borad[i][j] == 1:
                    if num_live_nbs < 2:
                        new_board[i][j] = 0
                    elif num_live_nbs == 2 or num_live_nbs == 3:
                        new_board[i][j] = 1
                    elif num_live_nbs > 3:
                        new_board[i][j] = 0
                    else:
                        pass
                else:
                    if num_live_nbs == 3:
                        new_board[i][j] = 1
        return new_board
