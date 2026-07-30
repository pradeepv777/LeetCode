class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        currentsum = 0
        for i in range(k):
            currentsum+=nums[i]
        maxavg = currentsum
        for i in range(k,len(nums)):
            currentsum = currentsum + nums[i] - nums[i-k]
            maxavg = max(maxavg,currentsum)
        maxavg = maxavg/k
        return maxavg

        