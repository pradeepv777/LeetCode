class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max1 = float("-inf")
        max2 = float("-inf")
        max1id = 0
        max2id = 0
        
        for i in range(len(nums)):
            if nums[i] > max1:
                max2 = max1
                max2id = max1id
                max1 = nums[i]
                max1id = i

            elif nums[i] > max2:
                max2 = nums[i]
                max2id = i

        return (nums[max1id]-1)*(nums[max2id]-1)
