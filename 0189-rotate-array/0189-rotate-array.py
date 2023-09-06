class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        nums_length = len(nums)
        
        # mod k because it might be out of bounds
        k %= nums_length
        
        # reverse the entire array
        nums.reverse()
        
        #grab the first part of the array up to k and rev
        nums[:k] = reversed(nums[:k])
        
        # grab the second part of the array k onward and rev
        nums[k:] = reversed(nums[k:])
        