class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        seen = {0:1}
        count  = 0
        sums = 0
        for i in nums:
            sums+=i
            if sums - k in seen:
                count+=seen[sums - k]
            if sums in seen:
                seen[sums]+=1
            else:
                seen[sums] = 1
        return count
         