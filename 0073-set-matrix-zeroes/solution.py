class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        row, col = set(), set()
        row_len = len(matrix)
        col_len = len(matrix[0])

        for i in range(row_len):
            for j in range(col_len):
                if matrix[i][j] == 0:
                   row.add(i) # if zero is found add the position idx to sets
                   col.add(j)

        for i in range(row_len): # Traverse through matrix -> if col or row have zero, set the index to zero
            for j in range(col_len):
                if i in row or j in col:
                    matrix[i][j] = 0
    


