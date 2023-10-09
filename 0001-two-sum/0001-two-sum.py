class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict = {} # num:index
        res = []
        
        for index, num in enumerate(nums):
            complement = target - num # complement + num = target
            if complement in dict:
                res.append(index)
                res.append(dict[complement])
                return res
            else:
                dict[num] = index
        