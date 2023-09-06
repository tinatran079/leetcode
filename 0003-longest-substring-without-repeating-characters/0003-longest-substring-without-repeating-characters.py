class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        left = 0
        built_char = set()
        
        for right in range(len(s)):
            # accumulate char from s in set and check for duplicates
            while s[right] in built_char:
                # remove
                built_char.remove(s[left])
                left += 1
            result = max(result, right - left + 1)
            built_char.add(s[right])
        
        return result