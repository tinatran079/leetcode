class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dict = {}
        res = []
        
        for num in nums:
            if num not in dict:
                dict[num] = 0
            dict[num] += 1
            
        for n, count in dict.items():
            if count > 1:
                res.append(n)
                
        return res