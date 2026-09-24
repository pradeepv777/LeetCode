import math

class Solution:
    def pivotInteger(self, n: int) -> int:
        # Sum of all elements from 1 to n
        total_sum = (n * (n + 1)) // 2
        
        # Take the integer square root
        x = math.isqrt(total_sum)
        
        # If its a perfect square, x is our pivot integer
        if x * x == total_sum:
            return x
            
        return -1
