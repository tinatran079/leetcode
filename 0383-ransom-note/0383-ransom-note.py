class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        magazine_counts = [0] * 26

        for letter in magazine:
            magazine_counts[ord(letter) - ord('a')] += 1

        for letter in ransomNote:
            index = ord(letter) - ord('a')
            if magazine_counts[index] > 0:
                magazine_counts[index] -= 1
            else:
                return False
        
        return True