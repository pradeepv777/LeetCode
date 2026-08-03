class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest = nums[0] 
        for i in range(len(nums)):
            if i > farthest:
                return False
            else:
                farthest = max(farthest, i + nums[i])
        return True
        