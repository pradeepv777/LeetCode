class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        max_size = 0
        zeros = 0
        left = 0
        n = len(nums)

        for right in range(n):
            if nums[right] == 0:
                zeros += 1
            while zeros > k:
                if nums[left] == 0:
                    zeros -=1
                left += 1

            size = right - left + 1
            max_size = max(size, max_size)

        return max_size


        