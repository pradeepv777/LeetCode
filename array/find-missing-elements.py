class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        s = set(nums)
        left = min(nums)
        right = max(nums)
        ans = []

        for num in range(left, right + 1):
            if num not in s:
                ans.append(num)
        return ans