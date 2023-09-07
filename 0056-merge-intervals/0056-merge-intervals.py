class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        # need to sort the intervals first!!!
        intervals.sort(key = lambda x: x[0]) # sort by the first val in intervals
        merged = [intervals[0]]
        
        for i in range(1, len(intervals)): # iterate through each interval in intervals
            current_interval = intervals[i]
            last_merged_interval = merged[-1] # grab the last interval in merged
            
            if last_merged_interval[1] >= current_interval[0]:
                last_merged_interval[1] = (max(last_merged_interval[1], current_interval[1]))
                
            else:
                merged.append(current_interval)
            
        return merged