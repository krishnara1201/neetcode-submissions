class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        n = len(intervals)
        res = 0
        prev = 0
        for i in range(1,n):
            if intervals[i][0] < intervals[prev][1]:
                res += 1
                prev = i
        
        return res

                
            