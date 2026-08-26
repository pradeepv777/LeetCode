class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        num_set = set(nums) 
        current = k
        while True:
            if current not in num_set:
                return current
            current += k  
