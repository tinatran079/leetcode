class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxNums = nums[0]
        minNums = nums[0]
        res = nums[0]
        
        for i in range(1, len(nums)):
            if nums[i] < 0:
                maxNums, minNums = minNums, maxNums
            
            maxNums = max(nums[i], maxNums * nums[i])
            minNums = min(nums[i], minNums * nums[i])
            
            res = max(res, maxNums)
            
        return res
        