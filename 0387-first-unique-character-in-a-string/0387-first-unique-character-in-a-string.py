class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        # find first non-repeating character and return its index
        # have a dictionary for char and count
        # loop through input with range
        # if character in dict = 1, return index, else -1
        
        dict = {}
        
        for char in s:
            if char not in dict:
                dict[char] = 0
            dict[char] += 1
            
        for i in range(len(s)):
            if dict[s[i]] == 1:
                return i
        
        return -1