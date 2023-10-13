class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # return indices of 2 numbers that they add up to target
        
        prev = {} # num: index
        res = []
        
        for index, num in enumerate(nums):
            complement = target - num
            if complement in prev:
                res.append(prev[complement])
                res.append(index)
                return res
            else:
                prev[num] = index