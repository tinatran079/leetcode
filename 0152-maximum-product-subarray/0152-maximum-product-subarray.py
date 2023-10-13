class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxPrdt = nums[0]
        minPrdt = nums[0]
        res = nums[0]
        
        for i in range(1, len(nums)):
            if nums[i] < 0:
                maxPrdt, minPrdt = minPrdt, maxPrdt
                
            maxPrdt = max(nums[i], nums[i]*maxPrdt)
            minPrdt = min(nums[i], nums[i]*minPrdt)
            
            res = max(res, maxPrdt)
            
        return res