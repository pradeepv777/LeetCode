class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        curr  = 0
        maxi = []
        
        arr = []
        for i in range(k):
            arr.append(nums[i])
        maxi.append(max(arr))
        
        for i in range(k,len(nums)):
            arr.pop(0)
            arr.append(nums[i])
            maxi.append(max(arr))

        return maxi


        
        
        