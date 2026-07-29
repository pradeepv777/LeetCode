class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        i = 0
        n = len(nums)
        while i<n:
            correctid = nums[i] - 1
            if nums[correctid] != nums[i]:
                nums[correctid],nums[i] = nums[i],nums[correctid]
            else:
                i+=1
            for i in range(n):
                if i+1 != nums[i]:
                    
                    return [nums[i],i+1]
                
