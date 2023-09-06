class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # move all the zeros to the front
        # move all the 2's to the back
        # l for the 0's
        # r for the 2's
        # i to iterate
        l, i = 0, 0
        r = len(nums) - 1
        
        while i <= r:
            if nums[i] == 0:
                nums[l], nums[i] = nums[i], nums[l]
                l += 1
            elif nums[i] == 2:
                nums[i], nums[r] = nums[r], nums[i]
                r -= 1
                i -= 1
            i += 1
        