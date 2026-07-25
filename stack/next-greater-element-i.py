class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        answer = {}
        for i in range(len(nums2)-1,-1,-1):
            while stack and stack[-1]<=nums2[i]:
                stack.pop()
            if stack:
                answer[nums2[i]] = stack[-1]
            else:
                answer[nums2[i]]= -1
            stack.append(nums2[i])
        return [answer[i] for i in nums1]
        

        