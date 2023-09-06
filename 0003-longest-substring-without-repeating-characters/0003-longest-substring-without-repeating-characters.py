class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # accumulate the longest window without repeats
        left, result = 0, 0
        built_char = set()
        
        for right in range(len(s)):
            while s[right] in built_char: # duplicate
                built_char.remove(s[left])
                left += 1
            built_char.add(s[right])
            result = max(result, right - left + 1)
            
        return result
            
            
        