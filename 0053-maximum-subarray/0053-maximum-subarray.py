class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # want to accumulate the sum of the array until it becomes neg
        current_total = 0
        max_total = float('-inf')
        
        for num in nums:
            current_total += num
            max_total = max(current_total, max_total)
            
            if current_total < 0:
                current_total = 0
                
        return max_total
        