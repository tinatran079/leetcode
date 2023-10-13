class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # convert all upper to lowercase
        # remove all non-alphanumeric char
        # if read same foward and backward, return True
        
        fixedS = ''
        
        for char in s:
            if char.isalpha() or char.isnumeric():
                fixedS += char
                
        # lowercase
        fixedS = fixedS.lower()
        
        left = 0
        right = len(fixedS) - 1
        
        while left <= right:
            if fixedS[left] != fixedS[right]:
                return False
            else:
                left += 1
                right -= 1
                
        return True
        