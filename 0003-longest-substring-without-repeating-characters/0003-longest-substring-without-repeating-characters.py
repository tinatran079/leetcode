class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        built_char = set()
        left = 0
        
        for right in range(len(s)):
            while s[right] in built_char:
                built_char.remove(s[left])
                left += 1
            res = max(res, right - left + 1)
            built_char.add(s[right])
            
        return res