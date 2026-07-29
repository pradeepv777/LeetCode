class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        i = 0 
        n = len(nums)
        while i<n:
            correct = nums[i] - 1
            if nums[i]!= nums[correct]:
                nums[i],nums[correct] = nums[correct],nums[i]
            else:
                i+=1
        res = []
        for i in range(n):
            if i+1 != nums[i] :
                res.append(nums[i])
        return res
