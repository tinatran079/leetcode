class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # find subarray with the largest sum, and return its SUM
        
        max_sum = float('-inf')
        cur_sum = 0
        
        for num in nums:
            cur_sum += num
            max_sum = max(max_sum, cur_sum)
            
            if cur_sum < 0:
                cur_sum = 0
                
        return max_sum
            
            
        