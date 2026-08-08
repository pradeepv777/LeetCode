class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        num_set = set(nums)
        max_length = 0
        
        for num in nums:
            if (num-1) not in num_set:
                curr_length = 0

                while (curr_length + num) in num_set:
                    curr_length +=1
                    max_length = max(curr_length,max_length)

        return max_length
        