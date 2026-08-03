class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[1])
        merged = [intervals[0]]
        prev_end = intervals[0][1]
        count = 0
        for current in intervals[1:]:
            if current[0]<prev_end:
                count+=1
            else:
                prev_end = current[0]
        return count
        
