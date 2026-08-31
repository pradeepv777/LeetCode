class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        if nums[0] > k:
            return 0

        left = 0
        right = len(nums) - 1
        pairs = 0

        while left < right:
            total = nums[left] + nums[right]
            if total == k:
                pairs += 1
                left += 1
                right -= 1

            elif total > k:
                right -=1
                
            else:
                left +=1

        return pairs


        