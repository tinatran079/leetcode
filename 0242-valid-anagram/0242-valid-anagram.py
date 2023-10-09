class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return self.countChar(s) == self.countChar(t)
        
    def countChar(self, anagrams):
        dict = {}
        for char in anagrams:
            if char not in dict:
                dict[char] = 0
            dict[char] += 1
            
        return dict
        