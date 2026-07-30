class Solution:
    def trap(self, height: List[int]) -> int:
        leftmax = [0] * len(height)
        rightmax = [0] * len(height)

        leftmax[0] = height[0]
        for i in range(1, len(height)):
            leftmax[i] = max(leftmax[i - 1], height[i])

        rightmax[len(height) - 1] = height[len(height) - 1]
        for i in range(len(height) - 2, -1, -1):
            rightmax[i] = max(rightmax[i + 1], height[i])

        water = 0
        
        for i in range(len(height)):
            water += min(leftmax[i], rightmax[i]) - height[i]
        return water
