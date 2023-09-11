class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # make a new string of only alphanumeric char
        # lowercase the new string
        # have 2 ptrs at each end until it meets in middle
        
        fixedS = ""
        
        for char in s:
            if char.isalpha() or char.isdigit():
                fixedS += char
                
        fixedS = fixedS.lower()
        
        l = 0
        r = len(fixedS) - 1
        
        while l <= r:
            if fixedS[l] != fixedS[r]:
                return False
            l += 1
            r -= 1
        return True
        