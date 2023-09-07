class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        # sort by end points!
        intervals.sort(key = lambda x: x[1])
        count = 0
        prevEnd = intervals[0][1]
        
        for i in range(1, len(intervals)):
            current_start, current_end = intervals[i] # i = [start, end]
            
            if current_start < prevEnd:
                count += 1
            else:
                prevEnd = current_end
                
        return count
         
        