class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        longestPrefix = min(strs, key = len)
        
        for i in strs:
            while not i.startswith(longestPrefix):
                longestPrefix = longestPrefix[:-1]
        
        return longestPrefix
        
        
        
        