class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums.sort()
        nums =set(nums)
        nums = list(nums)
        return nums[:k]

        