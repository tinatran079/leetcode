class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        
        current_subarray = 0
        max_subarray = float('-inf')
        
        for num in nums:
            current_subarray += num
            max_subarray = max(current_subarray, max_subarray)
            
            if current_subarray < 0:
                current_subarray = 0
                
        return max_subarray