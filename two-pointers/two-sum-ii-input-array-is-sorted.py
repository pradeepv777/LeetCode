class Solution:
    def twoSum(self, n: List[int], target: int) -> List[int]:
        left = 0
        right = len(n) - 1
        total = 0
        while left<right:
            total = n[left] + n[right]
            if total == target:
                return [left+1,right+1]
            elif total>right:
                right -=1
            else:
                left+=1