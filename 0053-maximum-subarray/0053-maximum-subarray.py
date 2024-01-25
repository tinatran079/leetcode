class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # go through the array and keep count of running total,
        # if the total is < 0, start over 
        # keep checking for the max sum
        
        maxCur = globalMax = nums[0]
        
        for i in range(1, len(nums)):
            maxCur = max(nums[i], maxCur + nums[i])
            if maxCur > globalMax:
                globalMax = maxCur
        return globalMax