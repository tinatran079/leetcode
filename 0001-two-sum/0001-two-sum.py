class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        prev = {}
        res = []
        
        for index, num in enumerate(nums):
            diff = target - num
            if diff in prev:
                res.append(index)
                res.append(prev[diff])
            prev[num] = index
            
        return res
                