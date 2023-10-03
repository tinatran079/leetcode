class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagrams = {} # ana:[its anas]
        
        for s in strs:
            sSort = ''.join(sorted(s))
            
            if sSort in anagrams:
                anagrams[sSort].append(s)
            else:
                anagrams[sSort] = [s]
        return list(anagrams.values())
                
            
        