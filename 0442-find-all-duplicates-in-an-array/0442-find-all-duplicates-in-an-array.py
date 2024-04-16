class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dict= {}
        res = []
        
        for n in nums:
            if n not in dict:
                dict[n] = 0
            dict[n] += 1
            
        for k, count in dict.items():
            if count > 1:
                res.append(k)
                
        return res