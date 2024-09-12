class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #initialize maxSum to first num
        #initialize curSum to 0 since this is what we are computing
        
        # iterate through nums
        # if curSum is neg, curSum back to zero and we start new subarray
        # else, keep adding num to cur SUm
        # compute the maxSum
        # return maxSum
        
        maxSum = nums[0]
        curSum = 0
        
        for num in nums:
            if curSum < 0:
                curSum = 0
            curSum += num
            maxSum = max(curSum, maxSum)
        
        return maxSum