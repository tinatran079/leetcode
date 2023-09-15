class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        # anagram - word of phrase formed by rearranging the letters of a diff
        # word or phrase
        
        # return an array of all the start indices of p's anagrams in s
        if len(p) > len(s):
            return []
        
        pCount, sCount = {}, {}
        
        for i in range(len(p)):
            pCount[p[i]] = 1 + pCount.get(p[i], 0)
            sCount[s[i]] = 1 + sCount.get(s[i], 0)
        
        # compare first substring    
        res = [0] if sCount == pCount else []
        l = 0
        for r in range(len(p), len(s)):
            sCount[s[r]] = 1 + sCount.get(s[r], 0)
            sCount[s[l]] -= 1
            
            # if char is zero
            if sCount[s[l]] == 0:
                sCount.pop(s[l])
            l+= 1
            if sCount == pCount:
                res.append(l)
                
        return res
        