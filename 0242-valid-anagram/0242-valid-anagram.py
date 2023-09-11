class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return self.count_substrings(s) == self.count_substrings(t)
        
    def count_substrings(self, ana):
        char_dict = {}
        for char in ana:
            if char not in char_dict:
                char_dict[char] = 0
            char_dict[char] += 1
            
        return char_dict
            
        
        