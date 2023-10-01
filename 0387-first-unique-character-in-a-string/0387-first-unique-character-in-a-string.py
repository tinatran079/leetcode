class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict = {}
        
        for char in s:
            if char not in dict:
                dict[char] = 0
            dict[char] += 1
            
        for i in range(len(s)):
            if dict[s[i]] == 1:
                return i
        
        return -1