class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagrams = {}
        
        
        for s in strs:
            s_sort = ''.join(sorted(s))
            
            if s_sort in anagrams:
                anagrams[s_sort].append(s)
            else:
                anagrams[s_sort] = [s]
                
        return list(anagrams.values())
            