class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # start at end
        goal = len(nums) - 1
        
        for i in range(len(nums) -1, -1, -1):
            # go backwards
            if i + nums[i] >= goal:
                # i is pos we are jumping to
                goal = i
                
        return True if goal == 0 else False