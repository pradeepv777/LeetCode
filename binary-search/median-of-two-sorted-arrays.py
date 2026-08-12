class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total = 0
        for i in nums1:
            total+=i
        for j in nums2:
            total+=j
        
        return total/(len(nums1)+len(nums2))

        