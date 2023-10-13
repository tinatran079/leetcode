class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # find subarray with the largest sum
        curSum = 0
        maxSum = float('-inf')
        
        for num in nums:
            curSum += num
            maxSum = max(curSum, maxSum)
            
            if curSum < 0:
                curSum = 0
                
        return maxSum