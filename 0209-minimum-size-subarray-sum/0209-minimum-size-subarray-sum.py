class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        # array of numbers and targett
        # return MIN LENGTH of subarray whose sum
        # is greater than or equal to target
        
        left = 0
        result = float('inf')
        total = 0
        
        for right in range(len(nums)):
            total += nums[right]
            while total >= target: # valid subarray 
                total -= nums[left]
                result = min(result, right - left + 1)
                left += 1
        
        
        return 0 if result == float('inf') else result