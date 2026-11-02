import heapq

class MedianFinder:

    def __init__(self):
        # small: Max-heap to store the smaller half of the numbers.
        # multiply values by -1 since py has min heap only
        # large: Min-heap to store the larger half of the numbers.
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        """
        1. Default push: Always add the new number to the max-heap -(small) first,
        negating it to maintain max-heap order.
        """
        heapq.heappush(self.small, -num)
        """
        # 2. Order invariant check: Every element in 'small' must be <= every element in 'large'.
        # Compare the largest value in 'small' (-1 * self.small[0]) with the smallest in 'large' (self.large[0]).
        """
        if self.small and self.large and (-1 * self.small[0] > self.large[0]):
            val = -heapq.heappop(self.small)  # Pop largest from small and restore positive sign
            heapq.heappush(self.large, val)   # Push into large
        """
        # 3. Size invariant check: The heaps can differ in size by at most 1 element.
        # Case A: 'small' has 2 more elements than 'large' -> move top of 'small' to 'large'
        """
        if len(self.small) > len(self.large) + 1:
            val = -heapq.heappop(self.small)  # Restore positive sign before moving to min-heap
            heapq.heappush(self.large, val)

        # Case B: 'large' has 2 more elements than 'small' -> move top of 'large' to 'small'
        if len(self.small) + 1 < len(self.large):
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)  # Negate before moving into max-heap

    def findMedian(self) -> float:
        # Odd total elements: The heap with 1 extra element holds the exact median at its root.
        if len(self.small) > len(self.large):
            return -self.small[0]  # Negate back to original value
        if len(self.small) < len(self.large):
            return self.large[0]
            
        # Even total elements: Median is the average of the largest in 'small' and smallest in 'large'.
        if len(self.small) == len(self.large):
            return (-self.small[0] + self.large[0]) / 2.0