class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        jumps = 0
        # window
        l = r = 0
        
        while r < len(nums) - 1:
            farthest = 0
            for i in range(l, r+1):
                # who can jump farthest
                farthest = max(farthest, i+nums[i])
            l = r + 1
            r = farthest
            jumps += 1
            
        return jumps