class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        # RETURN MIN LENGTH of SUBARRAY WHOSE
        # SUM is >= TARGET, if none return 0
        
        res = float('inf')
        cur_sum = 0
        i = 0
        
        for j in range(len(nums)):
            cur_sum += nums[j]
            while cur_sum >= target:
                cur_sum -= nums[i]
                res = min(res, j - i + 1)
                i += 1
                
        return 0 if res == float('inf') else res