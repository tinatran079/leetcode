class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        # Integer array nums, return true if any value appears at least twice
        # in the array, and false if every element is unique
        
        set_nums = set(nums)
        
        return len(set_nums) != len(nums)