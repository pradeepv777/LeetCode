class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        num = len(nums)

        for i in range(len(nums)):
            num ^= i
            num ^= nums[i]

        return num