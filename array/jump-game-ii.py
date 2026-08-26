class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) <=1:
            return 0

        overall_sum = nums[0]
        min_jumps = 1
        max_val = float('-inf')

        for i in range(len(nums) -1):
            max_val = max(max_val,nums[i] + i)

            if i == overall_sum:
                min_jumps+=1
                overall_sum = max_val

                if overall_sum >= len(nums) :
                    break

        return min_jumps





      