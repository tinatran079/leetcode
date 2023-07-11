class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # initialize to 1st value of nums
        maxSub = nums[0]
        curSum = 0
        
        for num in nums:
            # if neg prefix, remove
            if curSum < 0:
                curSum = 0
            # add num to curSum
            curSum += num
            maxSub = max(maxSub, curSum)
        return maxSub
        
        
        
        