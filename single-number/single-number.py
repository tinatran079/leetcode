class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict = {}
        
        for num in nums:
            if num not in dict:
                dict[num] = 0
            dict[num] += 1
            
        for n in dict:
            if dict[n] == 1:
                return n
        
        