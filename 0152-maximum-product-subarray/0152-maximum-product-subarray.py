class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # find subarray that has the largest product
        res = nums[0]
        maxPrdt = nums[0]
        minPrdt = nums[0]
        
        for i in range(1, len(nums)):
            if nums[i] < 0:
                maxPrdt, minPrdt = minPrdt, maxPrdt
                
            maxPrdt = max(nums[i], maxPrdt*nums[i])
            minPrdt = min(nums[i], minPrdt*nums[i])
            
            res = max(res, maxPrdt)
        return res