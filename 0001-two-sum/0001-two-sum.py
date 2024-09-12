class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        prev = {}
        result = []
        
        for index, num in enumerate(nums):
            complement = target - num
            # check to see if complement exists
            if complement in prev:
                result.append(prev[complement])
                result.append(index)
            else:
                prev[num] = index
        
        return result