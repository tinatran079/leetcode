class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if len(p) > len(s):
            return []
        
        sCount, pCount = {}, {}
        res = []
        
        for i in range(len(p)): # get the first subarray
            sCount[s[i]] = 1 + sCount.get(s[i], 0)
            pCount[p[i]] = 1 + pCount.get(p[i], 0)
            
        res = [0] if sCount == pCount else []
    
        # rest of subarray
        left = 0
        
        for right in range(len(p), len(s)):
            sCount[s[right]] = 1 + sCount.get(s[right], 0)
            sCount[s[left]] -= 1
            
            if sCount[s[left]] == 0:
                sCount.pop(s[left])
                
            left += 1
            if sCount == pCount:
                res.append(left)
                
        return res
        