class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # need to set it to something
        res = max(nums) 
        curMin, curMax = 1, 1 # neutral values
        
        # iterate through array
        for n in nums:
            if n == 0:
                # reset
                curMin, curMax = 1, 1
                continue # continue to next iteration
            
            tmp = curMax * n
            curMax = max(n*curMax, n * curMin, n)
            curMin = min(tmp, n * curMin, n) # tmp = curMax before calculated
            res = max(res, curMax)
            
        return res