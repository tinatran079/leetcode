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
                
        newString = newString.lower() # O(m) - new string
        
        # 2 ptrs
        left = 0
        right = len(newString) - 1
        
        while left <= right:
            if newString[left] != newString[right]:
                return False
            else:
                left += 1
                right -= 1
                
        return True