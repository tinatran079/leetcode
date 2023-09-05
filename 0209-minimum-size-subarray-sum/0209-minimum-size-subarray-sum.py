class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        # return the minimal LENGTH of a subarray whose sum
        # is greater than or equal to target. 
        l, total = 0, 0
        result = float('inf')
        
        for r in range(len(nums)):
            # calculate the current total
            total += nums[r]
            while total >= target:
                result = min(result, r - l + 1)
                total -= nums[l]
                l += 1
        
        return 0 if result == float('inf') else result
                
                
            
        