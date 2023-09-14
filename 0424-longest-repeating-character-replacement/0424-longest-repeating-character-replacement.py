class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        # return the longest substring containing the same letter
        maxLen = 0
        # hash map to keep track of all char
        count = {}
        l = 0
        
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            while (r-l+1) - max(count.values()) > k: # window not valid
                count[s[l]] -= 1
                l += 1
            maxLen = max(maxLen, r - l +1)
    
        return maxLen