class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        answer = [1] * n
        # left traversal - updating each element in answer array for prdt of everything to its left
        left_prdt = 1
        
        for i in range(n):
            answer[i] = left_prdt
            left_prdt *= nums[i]
            
        right_prdt = 1
        for i in range(n-1, -1, -1):
            answer[i] *= right_prdt
            right_prdt *= nums[i]
            
        return answer
        