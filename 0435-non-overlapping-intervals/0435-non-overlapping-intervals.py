class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort(key = lambda x: x[1]) # sort by ends
        prevEnd = intervals[0][1] # grab the first end of interval
        res = 0
        
        for i in range(1, len(intervals)):
            # grab the start and end of each interval
            current_start, current_end = intervals[i]
            
            # see if there is overalp - compare prevEnd to start of cur
            if prevEnd > current_start:
                res += 1
            
            # if there is no overlap, update the prevEnd
            else:
                prevEnd = current_end
                
        return res
        