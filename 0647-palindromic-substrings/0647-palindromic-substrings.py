class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        # count of palindromic substring
        res = 0
        
        for i in range(len(s)):
            l = r = i
            # found a palindrome
            res += self.countPalindrome(s, l, r)
            
            # even length palindrome
            l = i
            r = i + 1
            res += self.countPalindrome(s, l, r)
                
        return res
    
    def countPalindrome(self, s, l, r):
        res = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
        return res