class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # keep track of max and min
        
        numsMin = nums[0]
        numsMax = nums[0]
        res = nums[0]
        
        for i in range(1, len(nums)):
            if nums[i] < 0:
                numsMax, numsMin = numsMin, numsMax
            numsMax = max(nums[i], numsMax * nums[i])
            numsMin = min(nums[i], numsMin * nums[i])
            
            res = max(res, numsMax)
            
        return res