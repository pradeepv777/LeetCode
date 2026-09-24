class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Merges nums2 into nums1 in-place, such that nums1 becomes a single sorted array.
        The final sorted array should not be returned by the function, but instead be stored
        inside the array nums1. To accommodate this, nums1 has a length of m + n, where
        the first m elements denote the elements that should be merged, and the last n
        elements are set to 0 and should be ignored. nums2 has a length of n.
        """
        # Initialize pointers for nums1 (real elements), nums2, and the end of nums1
        p1 = m - 1  # Pointer for the last actual element in nums1
        p2 = n - 1  # Pointer for the last element in nums2
        p_merged = m + n - 1  # Pointer for the last position in the merged nums1
        # Iterate from the end of both arrays
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p_merged] = nums1[p1]
                p1 -= 1
            else:
                nums1[p_merged] = nums2[p2]
                p2 -= 1
            p_merged -= 1
        # If there are remaining elements in nums2, copy them to nums1
        # (elements in nums1 are already in place if p1 >= 0)
        while p2 >= 0:
            nums1[p_merged] = nums2[p2]
            p2 -= 1
            p_merged -= 1
        return p_merged
        