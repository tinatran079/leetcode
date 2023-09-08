class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = len(nums) * [1]
        
        left = 1
        for i in range(len(nums)):
            res[i] = left
            left *= nums[i]
            
        right = 1
        for i in range(len(nums) -1, -1, -1):
            res[i] *= right
            right *= nums[i]
            
        return res
        
            