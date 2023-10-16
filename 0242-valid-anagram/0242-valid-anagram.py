class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # word or phrase formed by rearranging the letters 
        # if both strings have the same character count, is anagram
        return self.countChar(s) == self.countChar(t)
        
        
        
    def countChar(self, characters):
        dict = {}
        for char in characters:
            if char not in dict:
                dict[char] = 0
            dict[char] += 1
        return dict