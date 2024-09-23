class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        my_dict = {}
        
        for char in s:
            if char not in my_dict:
                my_dict[char] = 0
            my_dict[char] += 1
            
        for i in range(len(s)):
            if my_dict[s[i]] == 1:
                return i 
        return - 1