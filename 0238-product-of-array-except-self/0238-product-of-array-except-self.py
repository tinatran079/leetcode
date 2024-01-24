class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        res = [1] * n
        
        left_prdt = 1
        for i in range(n):
            res[i] *= left_prdt
            left_prdt *= nums[i]
            
        right_prdt = 1
        for i in range(n-1, -1, -1):
            res[i] *= right_prdt
            right_prdt *= nums[i]
        return res
        