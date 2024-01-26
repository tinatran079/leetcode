class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # initialize the res, maxPrdt, minPrdt
        res = nums[0]
        maxPrdt = nums[0]
        minPrdt = nums[0]
        
        # iterate through the array
        for i in range(1, len(nums)):
            # if num is negative, swap the max and min prdt so might get larger prdt
            if nums[i] < 0:
                minPrdt, maxPrdt = maxPrdt, minPrdt
            
            # find the max and min of num and num * prdt
            maxPrdt = max(nums[i], nums[i]*maxPrdt)
            minPrdt = min(nums[i], nums[i]*minPrdt)
            
            res = max(res, maxPrdt)
            
        return res