class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # remove all non-alpha numeric characters
        # convert to all lowercase
        # 2 pointers
        
        fixedS = ''
        
        for char in s:
            if char.isnumeric() or char.isalpha():
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