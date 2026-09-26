class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # Edge case: If only 1 row or string is too short, return it as-is
        if numRows == 1 or len(s) <= numRows:
            return s
        
        # Initialize containers for each row
        rows = [""] * numRows
        curr_row = 0
        direction = 1  # 1 means moving down, -1 means moving up
        
        # Distribute characters into their respective rows
        for char in s:
            rows[curr_row] += char
            
            # Switch direction when hitting the top or bottom boundaries
            if curr_row == 0:
                direction = 1
            elif curr_row == numRows - 1:
                direction = -1
                
            curr_row += direction
            
        # Combine all rows to get the transformed result
        return "".join(rows)
