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
        
        
        
    def countChar(self, str):
        dict = {}
        for s in str:
            if s not in dict:
                dict[s] = 0
            dict[s] += 1
        return dict
        