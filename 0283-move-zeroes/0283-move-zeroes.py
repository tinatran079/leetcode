class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # two pointers - i (non zero), j - iterates through array
        l, r = 0, 0
        
        while r < len(nums):
            if nums[r] != 0:
                nums[l], nums[r] = nums[r], nums[l] # move the nonzero to the left
                # increment the left pointer
                l += 1
            r += 1
            
            
            