class Solution(object):
    def countGoodSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        # return number of substrings of length 3 where there is no repeat
        if len(s) < 3:
            return 0
        
        count = 0
        
        for i in range(2, len(s)): # start at 0, 1, 2 (3 size)
            # current substring window
            current = s[i-2:i+1] #[0-2]
            
            # use a set
            currentSet = set(current)
            if len(currentSet) == 3:
                count += 1
                
        return count
                
        