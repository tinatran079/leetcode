class Solution(object):
    def repeatedCharacter(self, s):
        """
        :type s: str
        :rtype: str
        """
        seen = set()
        
        for letter in s:
            if letter in seen:
                return letter
            seen.add(letter)