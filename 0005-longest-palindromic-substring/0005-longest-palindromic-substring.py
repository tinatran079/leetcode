class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ""
        resLen = 0
        
        for i in range(len(s)): #check ev pos in string
            # odd length
            l,r = i, i # center l and r to i(center)
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l:r+1] # update res
                    resLen = r - l + 1 # update the cur Length
                l -= 1
                r += 1
                
            # even length
            l, r = i , i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l:r + 1]
                    resLen = r - l + 1
                l -= 1
                r += 1
                
        return res