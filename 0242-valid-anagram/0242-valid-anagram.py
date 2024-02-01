class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return self.charCount(s) == self.charCount(t)
        
    
    
    def charCount(self, char):
        dict = {}
        for c in char:
            if c not in dict:
                dict[c] = 0
            dict[c] += 1

        return dict