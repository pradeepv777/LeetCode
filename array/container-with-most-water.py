class Solution:
    def maxArea(self, height: List[int]) -> int:
        leftmax = 0
        rightmax= len(height) - 1
        area = 0
        max_area = float("-inf")

        while leftmax < rightmax:
            area = min(height[leftmax],height[rightmax]) * (rightmax - leftmax)
            if height[leftmax] > height[rightmax]:
                rightmax -=1
            else:
                leftmax+=1
            if area > max_area:
                max_area = area
                
        return max_area


       