class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagrams = {}
        
        for s in strs:
            sortedS = ''.join(sorted(s))
            if sortedS in anagrams:
                anagrams[sortedS].append(s)
            else:
                anagrams[sortedS] = [s]
        return list(anagrams.values())
        