class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # nums - integer array
        # find subarray with largest sum, return its sum
        
        if len(nums) == 1:
            return nums[0] # return single element itself
        
        max_sum = float('-inf')
        current_total = 0
        
        for num in nums:
            current_total += num
            max_sum = max(max_sum, current_total)
            
            if current_total < 0:
                current_total = 0
            
        return max_sum
        
        