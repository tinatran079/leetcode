class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        count = {}
        res = 0
        
        l = 0
        
        for r in range(len(s)):
            # update the count in hash map
            if s[r] not in count:
                count[s[r]] = 0
            count[s[r]] += 1
            
            # check if window is valid
            while (r-l+1) - max(count.values()) > k:
                # shift left ptr, not valid
                count[s[l]] -= 1
                l += 1
                      
            res = max(res, r-l+1)
                      
        
        return res