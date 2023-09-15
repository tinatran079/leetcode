class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        # return MIN LEN of subarray whose sum is >= target
        
        minLen = float('inf')
        curSubarrayLen = 0 # sum of subarray
        left = 0
        
        for right in range(len(nums)):
            curSubarrayLen += nums[right]
            while curSubarrayLen >= target:
                minLen = min(right - left + 1, minLen)
                curSubarrayLen -= nums[left]
                left += 1
                
        return 0 if minLen == float('inf') else minLen
        