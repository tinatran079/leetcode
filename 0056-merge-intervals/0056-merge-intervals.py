class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        # sort the intervals
        intervals.sort(key = lambda x: x[0]) # sort by first val in intervals
        merged = [intervals[0]] # intialize
        
        for i in range(1, len(intervals)):
            current_interval = intervals[i]
            last_interval = merged[-1]
            
            if last_interval[1] >= current_interval[0]:
                last_interval[1] = (max(last_interval[1], current_interval[1]))
            else:
                merged.append(current_interval)
                
        return merged
    
    #[1,3],[2,6]
    # [1, 6] take larger of ending values
    # check current and next interval
    # if the beg of next interval is less than current interval's end, merge.