class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        # return the length of the longest substring
        # containing the same letter
        # sliding window
        # hash map to keep track of all char
        # want to replace the char that occurs least frequently
        res = 0
        l = 0
        count = {}
        
        for r in range(len(s)):
            count[s[r]] = 1+ count.get(s[r], 0) # add the cur element to the dict
            # see if window is not valid
            while (r - l + 1) - max(count.values()) > k: # if there aren't enough moves
                count[s[l]] -= 1
                l += 1# increase window until find valid window
            res = max(r-l+1 ,res)

        
        return res
        