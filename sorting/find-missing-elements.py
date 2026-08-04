class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        i =0
        n = len(nums)
        while i <n:
            correct = nums[i]-1
            if (1<= nums[i] < n & nums[i]!= nums[correct]):
                nums[i],nums[correct] = nums[correct] , nums[i]
            else:
                i+=1
        for i in range (len(nums)):
            if i+1!= nums[i]:
                return nums[i] +1

            
        