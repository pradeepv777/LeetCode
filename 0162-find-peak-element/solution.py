class Solution:
    def findPeakElement(self, nums: list[int]) -> int: ## O(log n) sol
        n = len(nums)
        left = 0
        right = n - 1
        
        while left < right :
            mid = (left + right)  // 2
            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            else: # if mid + 1 is greater than right most num
                 right = mid
                 
        return left


        



        