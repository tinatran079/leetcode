class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # accumulate the longest window without repeats
        i = 0 
        result = 0
        built_char = set()
        
        for j in range(len(s)):
            while s[j] in built_char:
                built_char.remove(s[i])
                i += 1
            built_char.add(s[j])
            result = max(result, j - i + 1)
            
        return result
            
            
        