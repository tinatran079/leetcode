class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        # find the first non-repeating character and return its index, if not return -1
        
        dict = {}
        
        for char in s:
            if char in dict:
                dict[char] += 1
            else:
                dict[char] = 1
                
        for i in range(len(s)):
            if dict[s[i]] == 1:
                return i
        
        return -1