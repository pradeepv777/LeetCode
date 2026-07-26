class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        maxi = 1
        mini = 1
        for i in range(len(nums)-1,len(nums)-4,-1):
            maxi*=nums[i]
        for i in range(2):
            mini = mini *nums[i]
        mini *= nums[-1] 

        return max(mini,maxi)
        