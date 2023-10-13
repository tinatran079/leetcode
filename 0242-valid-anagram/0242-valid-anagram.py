class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # return true if t is an anagram of s
        return self.countChar(s) == self.countChar(t)
        
        
    def countChar(self, string):
        dict = {} # char : count
        for char in string:
            if char not in dict:
                dict[char] = 0
            dict[char] += 1
            
        return dict