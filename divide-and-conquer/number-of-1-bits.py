class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 1
        while n >1 : 
           rem =  n % 2
           n = n // 2
           if rem == 1:
             count += 1
        return count

        