class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numsMin = nums[0]
        numsMax = nums[0]
        res = nums[0]
        
        for i in range(1, len(nums)):
            if nums[i] < 0:
                numsMin, numsMax = numsMax, numsMin
            numsMax = max(nums[i], nums[i]*numsMax)
            numsMin = min(nums[i], nums[i]*numsMin)
            
            res = max(res, numsMax)
            
        return res
        