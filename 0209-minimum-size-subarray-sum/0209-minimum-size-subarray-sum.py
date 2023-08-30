class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        result = float('inf')
        total = 0
        
        for right in range(len(nums)):
            # find the total to comapre the subarray sum to target
            total += nums[right]
            while total >= target:
                result = min(result, right - left + 1)
                total -= nums[left]
                left += 1
                
        return 0 if result == float('inf') else result
            
            
        