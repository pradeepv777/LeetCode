class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        if len(nums) <= 2:
            if len(nums) == 1:
                return 0
            else:
              return 0 if nums[0] > nums[1] else 1

        left = 0
        right = 2
        i = 1
        while i < len(nums)-1:
            if nums[i] > nums[left] and nums[i] > nums[right]:
                return i
            else:
                left += 1
                right += 1
                i +=1
        return len(nums) - 1 if nums[len(nums) - 1] > nums[len(nums) - 2] else 0

        



        