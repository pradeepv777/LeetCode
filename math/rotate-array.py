class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        def reversal(left,right):
            while left<right:
                nums[left],nums[right] = nums[right],nums[left]
                left +=1
                right -=1

        n = len(nums)
        k = k%n

        reversal(0,n-1)
        reversal(0, k-1)
        reversal(k,n-1)
            
        