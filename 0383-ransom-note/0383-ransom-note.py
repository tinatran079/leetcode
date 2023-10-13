class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        ransomCount = self.countChar(ransomNote)
        magazineCount = self.countChar(magazine)
        
        for char, count in ransomCount.items():
            if char not in magazineCount or magazineCount[char] < count:
                return False
        return True
        
        
        
    def countChar(self, string):
        dict = {}
        for char in string:
            if char not in dict:
                dict[char] = 0
            dict[char] += 1
        return dict
        