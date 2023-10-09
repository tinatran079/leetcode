class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # subarray with the largest product
        minPrdt = nums[0]
        maxPrdt = nums[0]
        res = nums[0]
        
        for i in range(1, len(nums)):
            if nums[i] < 0:
                minPrdt, maxPrdt = maxPrdt, minPrdt
            maxPrdt = max(nums[i], nums[i] * maxPrdt)
            minPrdt = min(nums[i], nums[i] * minPrdt)
            
            res = max(res, maxPrdt)
            
        return res