class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        # set for substring window
        charSet = set()
        
        #sliding window
        l = 0
        
        for r in range(len(s)):
            # get duplicate
            while s[r] in charSet:
                # update window by removing the left char
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r-l+1)
            
        return res
            