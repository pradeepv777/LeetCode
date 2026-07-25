class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maximum = 0
        minimum = float("inf")
        for i in prices:
            minimum = min(minimum,i)
            maximum = max(maximum,i-minimum)
        return maximum
        