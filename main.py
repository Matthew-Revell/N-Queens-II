class Solution:
    def totalNQueens(self, n):
        col = [False] * n
        diag = [False] * (2*n - 1)
        anti_diag = [False] * (2*n - 1)
        return self.solve(col, diag, anti_diag, 0)
        
    def solve(self, col, diag, anti_diag, row):
        n = len(col)
        count = 0
        if row == n:
            return 1
        for column in range(n):
            if not col[column] and not diag[row + column] and not anti_diag[row - column + n - 1]:
                col[column] = diag[row + column] = anti_diag[row - column + n - 1] = True
                count += self.solve(col, diag, anti_diag, row + 1)
                col[column] = diag[row + column] = anti_diag[row - column + n - 1] = False
        return count