class Solution(object):
    def repeatedCharacter(self, s):
        """
        :type s: str
        :rtype: str
        """
        map = {}
        
        for i in range(len(s)):
            if s[i] in map:
                return s[i]
            else:
                map[s[i]] = i
                