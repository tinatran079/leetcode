class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        res = []
        prev = {} # num: index
        
        for index, num in enumerate(nums):
            complement = target - num
            if complement in prev:
                res.append(index)
                res.append(prev[complement])
                return res
            else:
                prev[num] = index