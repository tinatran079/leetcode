class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # compare s's and t's dictionary
        return self.countChar(s) == self.countChar(t)
        
        
        
    # function to keep track of each char and its count
    def countChar(self, string):
        dict = {} # char : count
        
        for char in string:
            if char not in dict:
                dict[char] = 0
            dict[char] += 1
            
        return dict