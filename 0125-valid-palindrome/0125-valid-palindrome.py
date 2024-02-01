class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        newString = ""
        
        # make a new string that is all lowercase and remove all non-alphanumeric characters
        
        for char in s:
            # O(n)
            if char.isalpha() or char.isnumeric():
                newString += char
                
        newString = newString.lower()
        
        # reverse
        return newString == newString[::-1]