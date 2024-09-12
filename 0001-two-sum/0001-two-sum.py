class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # input: array of numbers
        # return indices of num1 + num2 = target
        
        # optimized using a hash map
        # num1 + num2 = target
        # complement = target - num
        # as loop through array, find if this is the case
        # use enumrate for index and num
        
        result = []
        seen = {}
        for index, num in enumerate(nums):
            complement = target - num
            # if complement is in hash map, found it!
            if complement in seen:
                result.append(seen[complement])
                result.append(index)
            else:
                seen[num] = index
        
        return result
        