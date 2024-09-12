class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # input: array of numbers
        # return indices of num1 + num2 = target
        
        # nested loop to find pairs that add up to target
        result = []
        
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                total = nums[i] + nums[j]
                if total == target:
                    result.append(i)
                    result.append(j)
                    
        return result