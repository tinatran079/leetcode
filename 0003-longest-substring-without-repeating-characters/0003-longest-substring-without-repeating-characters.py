class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        longest = 0
        i = 0 
        
        built_chars = set()
        
        for j in range(len(s)):
            while s[j] in built_chars:
                built_chars.remove(s[i])
                i += 1
                
            # if not in built_chars
            built_chars.add(s[j])
            longest = max(longest, j - i + 1)
            
        return longest