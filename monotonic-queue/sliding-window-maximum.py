class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = collections.deque()
        left = 0
        right = 0
        arr = []

        while right<len(nums):

            while q and nums[q[-1]] < nums[right]:
                q.pop()
            q.append(right)

            if left > q[0]:
                q.popleft()

            if (right+1) >= k:
                arr.append(nums[q[0]])
                left+=1
            right+=1

        return arr

            

      