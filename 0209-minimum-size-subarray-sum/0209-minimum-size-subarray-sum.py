class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        # return MINIMAL LENGTH OF SUBARRAY whose SUM is >= than target
        # if there is no subarray return 0
        # use sliding window algo
        
        res = float('inf') # used for length of array
        left = 0
        curSum = 0 # used for sum of subarray
        
        for right in range(len(nums)):
            curSum += nums[right]
            while curSum >= target: # found a valid window
                curSum -= nums[left]
                res = min(right - left + 1, res)
                left += 1
            
        return 0 if res == float('inf') else res
                