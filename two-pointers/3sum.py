class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = []
        total = 0
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            elif i> 0 and nums[i-1] == nums[i]:
                continue
            left = i+1
            right = len(nums)-1
            while left < right:
                total  =  nums[left] + nums[right] + nums[i]
                if total == 0:
                    res.append([nums[i],nums[left],nums[right]])
                    left+=1
                    right-=1
                    while left < right and nums[left] == nums[left-1]:
                        left+=1
                    while left < right and nums[right] == nums[right+1]:
                        right -=1
                elif total > 0:
                    right -=1
                else:
                    left +=1
        return res
                    




        