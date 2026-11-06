class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        
        window_sum = sum(nums[:k])
        max_val = window_sum
        for i in range(k, len(nums)):
            
            window_sum = window_sum + nums[i] - nums[i - k]
            max_val = max(max_val, window_sum)

        return max_val / k


        