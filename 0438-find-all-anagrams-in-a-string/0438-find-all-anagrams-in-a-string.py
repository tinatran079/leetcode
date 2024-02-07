class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        # check is len of p is bigger than len of s
        if len(p) > len(s):
            return []
        
        pCount, sCount = {}, {}
        
        # inialize hash maps for p & s
        for i in range(len(p)):
            pCount[p[i]] = 1 + pCount.get(p[i], 0)
            sCount[s[i]] = 1 + sCount.get(s[i], 0)
            
        # check if the initalized counts match
        res = [0] if pCount == sCount else []
        
        #intialize window
        l = 0
        
        for r in range(len(p), len(s)):
            # Include the character at position r in the window
            sCount[s[r]] = 1 + sCount.get(s[r], 0)
            # Exclude the character at position l from the window
            sCount[s[l]] -= 1
            
            # remove l if zero
            if sCount[s[l]] == 0:
                sCount.pop(s[l])
            # increase l
            l += 1
            
            # compare hash maps again
            if sCount == pCount:
                res.append(l)
            
        return res