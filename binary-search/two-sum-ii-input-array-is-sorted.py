class Solution:
    def twoSum(self, n: List[int], target: int) -> List[int]:
       total = 0
       left = 0
       right = len(n)-1
       while left<right:
           total = n[left] + n[right]
           mid = len(n)//2
           if total == target:
               return [left+1,right+1]
           if total > target:
                right = mid-1
           else:
                left = mid+1