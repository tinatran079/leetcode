class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        fixedS = ""
        
        for char in s:
            if char.isalpha( ) or char.isdigit():
                fixedS += char
                
        fixedS = fixedS.lower()
        
        l = 0
        r = len(fixedS) - 1
        
        while l <= r: # go until the middle
            if fixedS[l] != fixedS[r]: # not a palindrome
                return False
            l += 1
            r -= 1
        return True
        