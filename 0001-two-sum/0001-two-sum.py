class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        res = []
        prev = {}
        
        for index, num in enumerate(nums):
            complement = target - num
            if complement in prev:
                res.append(prev[complement])
                res.append(index)
                return res 
            prev[num] = index
            