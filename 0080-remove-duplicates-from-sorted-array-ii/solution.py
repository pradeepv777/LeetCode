class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        k = 0
        count = Counter()
        for num in nums:
            count[num] +=1
            if count[num] <= 2:
                nums[k] = num
                k +=1
        return k
        