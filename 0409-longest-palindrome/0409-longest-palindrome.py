class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        char_counts = {}
        odd_count = 0
        resLen = 0
        
        for char in s:
            char_counts[char] = char_counts.get(char, 0) + 1
        
        for count in char_counts.values():
            if count % 2 == 0:
                resLen += count
            else:
                resLen += count - 1
                odd_count = 1

        if odd_count:
            resLen += 1

        return resLen