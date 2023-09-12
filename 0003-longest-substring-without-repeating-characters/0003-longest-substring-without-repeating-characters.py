class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Find the longest substring without repeating char
        # Need a set for O(n) constant lookup - see if there
        # is any repeating characters
        # While going through each char, if the char is in set
        # that means, there is a repeat
            # remove the most left char from set, and increment left, 
        # otherwise, add the right char to the set, and find the
        # max between prev max and current window.
        
        res = 0
        left = 0
        built_char = set()
        
        for right in range(len(s)):
            while s[right] in built_char:
                built_char.remove(s[left])
                left += 1
            res = max(res, right - left + 1)
            built_char.add(s[right])
        return res