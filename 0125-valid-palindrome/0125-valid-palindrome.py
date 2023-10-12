class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # all lowercase
        # remove all non-alphanumeric char
        # reads same foward and backward
        
        fixedS = ''
        
        for char in s:
            if char.isalpha() or char.isnumeric():
                fixedS += char
        
        fixedS = fixedS.lower()
        
        left = 0
        right = len(fixedS) - 1
        
        while left <= right:
            if fixedS[left] != fixedS[right]:
                return False
            left += 1
            right -= 1
            
        return True