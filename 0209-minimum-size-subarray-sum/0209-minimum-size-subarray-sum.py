class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        
        left, total = 0, 0
        result = float("inf")
        
        for right in range(len(nums)):
            # sliding window
            total += nums[right]
            while total >= target:
                # size of window
                result = min(result, right - left + 1)
                total -= nums[left]
                left += 1
            
            
        return 0 if result == float("inf") else result
            
        