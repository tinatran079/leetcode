class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        left = 0
        charSet = set()
        
        for right in range(len(s)):
            # get duplicate
            while s[right] in charSet:
                charSet.remove(s[left])
                left += 1
                

            # if unique character, add the right char to set and calculate length of window
            charSet.add(s[right])
            res = max(res, right-left+1)
                
        return res
            