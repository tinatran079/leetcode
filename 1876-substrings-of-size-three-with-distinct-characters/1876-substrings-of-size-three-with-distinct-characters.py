class Solution(object):
    def countGoodSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        
        for i in range(2, len(s)):
            currentSubstring = s[i-2:i+1] # get three char
            uniqueSet = set(currentSubstring)
            if len(uniqueSet) == 3:
                count += 1
        
        return count
        