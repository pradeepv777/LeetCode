class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
       q = collections.deque()
       left = 0
       right = 0
       res = []
       # 1. If deq not empty and last element is less than incoming elment
       # --> pop the last elments [-1] in deq until true if less append new val  
       while right<len(nums):
            while q and nums[q[-1]] < nums[right]:
                q.pop()
            q.append(right)

            # 2. REMOVE EXPIRED ELEMENTS
            # If the oldest index at the front of the queue falls behind the 
            # left boundary of our current window, remove it.
            if left > q[0]:
                q.popleft()

            if (right+1)>=k:
                res.append(nums[q[0]])
                left+=1 # MOve left ptr to decrease the window size
            right+=1  # if window size is not k add elemts till it is
       return res
            
        
