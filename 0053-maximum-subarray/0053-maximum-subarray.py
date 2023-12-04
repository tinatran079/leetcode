class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # keep track of global and cur max of subarray
        # compare the current index with the max subarray 
        # at prev index.
        
        max_cur = global_max = nums[0]
        
        for i in range(1, len(nums)):
            max_cur = max(nums[i], max_cur + nums[i])
            if max_cur > global_max:
                global_max = max_cur
        return global_max
    
    
        