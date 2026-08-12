class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False   
        rows = len(matrix)
        cols = len(matrix[0])
        total_elements = rows * cols
        
        left = 0
        right = total_elements - 1

        while left <= right:
            mid = (left + right) // 2
            row = mid // cols # row Index
            col = mid % cols  # Column Index

            mid_num = matrix[row][col]

            if target == mid_num:
                return True
            elif target > mid_num:
                left = mid + 1
            else:
                right = mid - 1

        return False
