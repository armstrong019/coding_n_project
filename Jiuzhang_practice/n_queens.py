class Solution:
    """
    @param: n: The number of queens
    @return: All distinct solutions
    """

    def solveNQueens(self, n):
        # write your code here
        result = []
        perm = []
        visited = {"col": set(), "sum": set(), "diff": set()}
        self.dfs(n, perm, visited, result)
        return result

    def dfs(self, n, perm, visited, result):
        if n == len(perm):
            result.append(self.draw(perm))
            return

        row = len(perm)
        for col in range(n):
            if not self.isvaild(col, row, visited):
                continue
            perm.append(col)
            visited["col"].add(col)
            visited["sum"].add(row + col)
            visited["diff"].add(row - col)

            self.dfs(n, perm, visited, result)
            perm.pop()
            visited["col"].remove(col)
            visited["sum"].remove(row + col)
            visited["diff"].remove(row - col)

    def isvaild(self, col, row, visited):
        if col in visited["col"]:
            return False
        if row + col in visited["sum"]:
            return False
        if row - col in visited["diff"]:
            return False
        return True

    def draw(self, perm):
        board = []
        n = len(perm)
        for col in perm:
            row_string = ''.join(['Q' if c == col else '.' for c in range(n)])
            board.append(row_string)
        return board